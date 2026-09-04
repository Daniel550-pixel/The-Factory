from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable
from .policy import Proposal

@dataclass(frozen=True)
class AgentSpec:
    agent_id: str
    capabilities: tuple[str, ...] = ()

@dataclass(frozen=True)
class AgentResult:
    agent_id: str
    proposal: Proposal
    rationale: str = ""

class AgentRuntime:
    def __init__(self) -> None:
        self._agents: dict[str, tuple[AgentSpec, Callable[..., AgentResult]]] = {}

    def register(self, spec: AgentSpec, handler: Callable[..., AgentResult]) -> None:
        if spec.agent_id in self._agents:
            raise ValueError(f"agent already registered: {spec.agent_id}")
        self._agents[spec.agent_id] = (spec, handler)

    def invoke(self, agent_id: str, **kwargs: Any) -> AgentResult:
        if agent_id not in self._agents:
            raise KeyError(f"unknown agent: {agent_id}")
        return self._agents[agent_id][1](**kwargs)

    def list_agents(self) -> tuple[AgentSpec, ...]:
        return tuple(spec for spec, _ in self._agents.values())

@dataclass(frozen=True)
class ArbitrationResult:
    selected_agent: str | None
    score: float
    rationale: str

class Arbitrator:
    @staticmethod
    def select(results: list[AgentResult]) -> ArbitrationResult:
        if not results:
            return ArbitrationResult(None, 0.0, "no results")
        ranked = sorted(results, key=lambda r: (-r.proposal.confidence * (1-r.proposal.risk), r.agent_id))
        top = ranked[0]
        return ArbitrationResult(top.agent_id, top.proposal.confidence * (1-top.proposal.risk), "highest confidence-adjusted safety score")
