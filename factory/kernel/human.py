from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class ApprovalRequest:
    request_id: str
    proposal_id: str
    reason: str

@dataclass(frozen=True)
class Approval:
    request_id: str
    approved: bool
    reviewer_id: str
    reason: str = ""

class ApprovalStore:
    def __init__(self) -> None:
        self._approvals: dict[str, Approval] = {}

    def record(self, approval: Approval) -> None:
        self._approvals[approval.request_id] = approval

    def get(self, request_id: str) -> Approval | None:
        return self._approvals.get(request_id)
