"""Policy and execution-boundary contracts.

Policy decides whether a proposal may proceed. It never executes the action.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable


class PolicyDecision(str, Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    ESCALATE = "ESCALATE"


@dataclass(frozen=True)
class Proposal:
    proposal_id: str
    actor_id: str
    action: str
    target: str
    parameters: dict[str, Any]
    confidence: float
    risk: float
    evidence_ids: tuple[str, ...] = ()


class PolicyGate:
    """Deterministic policy evaluator separated from execution."""

    def __init__(self, evaluator: Callable[[Proposal], PolicyDecision]) -> None:
        self._evaluator = evaluator

    def evaluate(self, proposal: Proposal) -> PolicyDecision:
        if not 0.0 <= proposal.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        if not 0.0 <= proposal.risk <= 1.0:
            raise ValueError("risk must be between 0 and 1")
        return self._evaluator(proposal)
