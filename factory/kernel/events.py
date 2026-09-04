"""Deterministic event primitives for the Factory kernel.

The in-memory ledger is a reference implementation. A durable adapter can
persist the same contract without changing callers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
import json
from typing import Any


@dataclass(frozen=True)
class Event:
    sequence: int
    event_type: str
    payload: dict[str, Any]
    timestamp: str
    correlation_id: str | None = None
    causation_id: str | None = None
    previous_hash: str | None = None
    event_hash: str = field(default="")

    def canonical_bytes(self) -> bytes:
        body = {
            "sequence": self.sequence,
            "event_type": self.event_type,
            "payload": self.payload,
            "timestamp": self.timestamp,
            "correlation_id": self.correlation_id,
            "causation_id": self.causation_id,
            "previous_hash": self.previous_hash,
        }
        return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

    def with_hash(self) -> "Event":
        return Event(**{**self.__dict__, "event_hash": sha256(self.canonical_bytes()).hexdigest()})


class EventLedger:
    """Append-only, hash-chained reference ledger."""

    def __init__(self) -> None:
        self._events: list[Event] = []

    def append(
        self,
        event_type: str,
        payload: dict[str, Any],
        timestamp: str,
        *,
        correlation_id: str | None = None,
        causation_id: str | None = None,
    ) -> Event:
        previous_hash = self._events[-1].event_hash if self._events else None
        event = Event(
            sequence=len(self._events) + 1,
            event_type=event_type,
            payload=payload,
            timestamp=timestamp,
            correlation_id=correlation_id,
            causation_id=causation_id,
            previous_hash=previous_hash,
        ).with_hash()
        self._events.append(event)
        return event

    def events(self) -> tuple[Event, ...]:
        return tuple(self._events)

    def verify(self) -> bool:
        previous: str | None = None
        for expected_sequence, event in enumerate(self._events, start=1):
            if event.sequence != expected_sequence or event.previous_hash != previous:
                return False
            if event.with_hash().event_hash != event.event_hash:
                return False
            previous = event.event_hash
        return True

    def replay(self) -> tuple[Event, ...]:
        if not self.verify():
            raise ValueError("event ledger integrity verification failed")
        return self.events()
