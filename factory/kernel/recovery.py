from __future__ import annotations
from dataclasses import dataclass
from .events import Event, EventLedger

@dataclass(frozen=True)
class ReplayResult:
    valid: bool
    event_count: int
    last_sequence: int

class ReplayEngine:
    @staticmethod
    def inspect(ledger: EventLedger) -> ReplayResult:
        events: tuple[Event, ...] = ledger.replay()
        return ReplayResult(bool(ledger.verify()), len(events), events[-1].sequence if events else 0)
