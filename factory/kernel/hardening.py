"""Production-hardening primitives for deterministic governed execution."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class IdempotencyConflict(ValueError):
    """Raised when one idempotency key is reused for a different operation."""


@dataclass(frozen=True)
class ExecutionReceipt(Generic[T]):
    key: str
    fingerprint: str
    result: T


class IdempotencyStore(Generic[T]):
    """Small deterministic receipt store; adapters can replace it with durable storage."""

    def __init__(self) -> None:
        self._receipts: dict[str, ExecutionReceipt[T]] = {}

    def get(self, key: str) -> ExecutionReceipt[T] | None:
        return self._receipts.get(key)

    def execute_once(self, key: str, fingerprint: str, operation: Callable[[], T]) -> T:
        existing = self._receipts.get(key)
        if existing is not None:
            if existing.fingerprint != fingerprint:
                raise IdempotencyConflict(f"idempotency key reused: {key}")
            return existing.result
        result = operation()
        self._receipts[key] = ExecutionReceipt(key, fingerprint, result)
        return result


@dataclass(frozen=True)
class AuthorizationAudit:
    execution_id: str
    actor_id: str
    decision: str
    proposal_id: str
    reason: str


class AuthorizationAuditLog:
    """Append-only in-memory audit surface for authorization decisions."""

    def __init__(self) -> None:
        self._entries: list[AuthorizationAudit] = []

    def record(self, entry: AuthorizationAudit) -> None:
        self._entries.append(entry)

    def entries(self) -> tuple[AuthorizationAudit, ...]:
        return tuple(self._entries)


class FailureInjector:
    """Deterministic failure hooks used by recovery and resilience tests."""

    def __init__(self) -> None:
        self._failures: set[str] = set()

    def fail(self, point: str) -> None:
        self._failures.add(point)

    def clear(self, point: str) -> None:
        self._failures.discard(point)

    def checkpoint(self, point: str) -> None:
        if point in self._failures:
            raise RuntimeError(f"injected failure: {point}")
