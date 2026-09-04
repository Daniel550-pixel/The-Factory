"""Evidence and provenance contracts."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    source: str
    claim: str
    strength: float
    observed_at: str | None = None
    parent_ids: tuple[str, ...] = ()
    reality_pointer: str | None = None
    metadata: dict[str, Any] | None = None

    def __post_init__(self) -> None:
        if not 0.0 <= self.strength <= 1.0:
            raise ValueError("strength must be between 0 and 1")

class EvidenceStore:
    def __init__(self) -> None:
        self._items: dict[str, Evidence] = {}

    def add(self, evidence: Evidence) -> None:
        if evidence.evidence_id in self._items:
            raise ValueError(f"duplicate evidence id: {evidence.evidence_id}")
        self._items[evidence.evidence_id] = evidence

    def get(self, evidence_id: str) -> Evidence | None:
        return self._items.get(evidence_id)

    def require(self, evidence_ids: tuple[str, ...]) -> tuple[Evidence, ...]:
        missing = [i for i in evidence_ids if i not in self._items]
        if missing:
            raise KeyError(f"missing evidence: {', '.join(missing)}")
        return tuple(self._items[i] for i in evidence_ids)
