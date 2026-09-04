"""Deterministic execution context and provenance-aware memory primitives."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class ExecutionContext:
    execution_id: str
    trace_id: str
    actor_id: str
    agent_id: str | None = None
    parent_id: str | None = None
    capability: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class ContextItem:
    item_id: str
    content: Any
    provenance_ids: tuple[str, ...] = ()
    confidence: float = 1.0

class ContextStore:
    def __init__(self) -> None:
        self._items: dict[str, ContextItem] = {}

    def put(self, item: ContextItem) -> None:
        if not 0.0 <= item.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        self._items[item.item_id] = item

    def get(self, item_id: str) -> ContextItem | None:
        return self._items.get(item_id)

    def assemble(self, item_ids: list[str]) -> tuple[ContextItem, ...]:
        return tuple(self._items[i] for i in item_ids if i in self._items)
