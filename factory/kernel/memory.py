from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class MemoryRecord:
    memory_id: str
    agent_id: str
    content: Any
    provenance_ids: tuple[str, ...] = ()
    confidence: float = 1.0
    outcome: str | None = None

class MemoryStore:
    def __init__(self) -> None:
        self._records: dict[str, MemoryRecord] = {}

    def remember(self, record: MemoryRecord) -> None:
        if not 0.0 <= record.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        self._records[record.memory_id] = record

    def recall(self, agent_id: str | None = None) -> tuple[MemoryRecord, ...]:
        values = tuple(self._records.values())
        return tuple(r for r in values if agent_id is None or r.agent_id == agent_id)
