"""Reference orchestration path joining the Factory kernel contracts.

The orchestrator coordinates primitives; it does not replace them. In
particular, policy evaluation remains separate from execution and every
state transition is represented in the event ledger.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from .agents import AgentRuntime, Arbitrator
from .context import ExecutionContext
from .events import EventLedger
from .execution import ExecutionBoundary, ExecutionResult
from .memory import MemoryRecord, MemoryStore
from .policy import PolicyDecision, PolicyGate, Proposal
from .provenance import EvidenceStore


@dataclass(frozen=True)
class RunResult:
    execution_context: ExecutionContext
    proposal: Proposal
    decision: PolicyDecision
    execution: ExecutionResult
    selected_agent: str


class FactoryRuntime:
    """Minimal single-process reference runtime for the Factory kernel."""

    def __init__(
        self,
        agents: AgentRuntime,
        policy: PolicyGate,
        executor: ExecutionBoundary,
        *,
        ledger: EventLedger | None = None,
        evidence: EvidenceStore | None = None,
        memory: MemoryStore | None = None,
    ) -> None:
        self.agents = agents
        self.policy = policy
        self.executor = executor
        self.ledger = ledger or EventLedger()
        self.evidence = evidence or EvidenceStore()
        self.memory = memory or MemoryStore()

    @staticmethod
    def _timestamp() -> str:
        return datetime.now(timezone.utc).isoformat()

    def run(self, context: ExecutionContext, agent_ids: list[str], **inputs: Any) -> RunResult:
        self.ledger.append(
            "execution.started",
            {"execution_id": context.execution_id, "agent_ids": agent_ids},
            self._timestamp(),
            correlation_id=context.trace_id,
        )

        results = [self.agents.invoke(agent_id, **inputs) for agent_id in agent_ids]
        arbitration = Arbitrator.select(results)
        if arbitration.selected_agent is None:
            raise ValueError("agent runtime produced no result")

        selected = next(r for r in results if r.agent_id == arbitration.selected_agent)
        proposal = selected.proposal
        self.evidence.require(proposal.evidence_ids)

        self.ledger.append(
            "proposal.created",
            {"proposal_id": proposal.proposal_id, "agent_id": selected.agent_id},
            self._timestamp(),
            correlation_id=context.trace_id,
        )

        decision = self.policy.evaluate(proposal)
        self.ledger.append(
            "policy.evaluated",
            {"proposal_id": proposal.proposal_id, "decision": decision.value},
            self._timestamp(),
            correlation_id=context.trace_id,
        )

        execution = self.executor.execute(proposal, decision)
        self.ledger.append(
            "execution.completed",
            {"proposal_id": proposal.proposal_id, "executed": execution.executed},
            self._timestamp(),
            correlation_id=context.trace_id,
        )

        self.memory.remember(
            MemoryRecord(
                memory_id=f"run:{context.execution_id}",
                agent_id=selected.agent_id,
                content={"proposal_id": proposal.proposal_id, "decision": decision.value},
                provenance_ids=proposal.evidence_ids,
                confidence=proposal.confidence,
                outcome="executed" if execution.executed else decision.value.lower(),
            )
        )
        return RunResult(context, proposal, decision, execution, selected.agent_id)
