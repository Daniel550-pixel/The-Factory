from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable
from .policy import PolicyDecision, Proposal

@dataclass(frozen=True)
class ExecutionResult:
    proposal_id: str
    executed: bool
    result: Any = None

class ExecutionBoundary:
    """Only executes proposals after an explicit ALLOW decision."""
    def __init__(self, executor: Callable[[Proposal], Any]) -> None:
        self._executor = executor

    def execute(self, proposal: Proposal, decision: PolicyDecision) -> ExecutionResult:
        if decision is not PolicyDecision.ALLOW:
            return ExecutionResult(proposal.proposal_id, False)
        return ExecutionResult(proposal.proposal_id, True, self._executor(proposal))
