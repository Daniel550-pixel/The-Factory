from factory.kernel import (
    AgentResult,
    AgentRuntime,
    AgentSpec,
    ExecutionBoundary,
    ExecutionContext,
    Evidence,
    EvidenceStore,
    FactoryRuntime,
    PolicyDecision,
    PolicyGate,
    Proposal,
)


def test_factory_runtime_completes_governed_execution_and_records_memory() -> None:
    agents = AgentRuntime()
    evidence = EvidenceStore()
    evidence.add(Evidence("e1", "test", "verified claim", 0.95))

    proposal = Proposal(
        proposal_id="p1",
        actor_id="agent.test",
        action="example.action",
        target="example.target",
        parameters={"value": 42},
        confidence=0.95,
        risk=0.1,
        evidence_ids=("e1",),
    )
    agents.register(
        AgentSpec("agent.test", ("example.action",)),
        lambda **_: AgentResult("agent.test", proposal, "verified test proposal"),
    )

    executed: list[str] = []
    runtime = FactoryRuntime(
        agents,
        PolicyGate(lambda p: PolicyDecision.ALLOW if p.risk < 0.5 else PolicyDecision.ESCALATE),
        ExecutionBoundary(lambda p: executed.append(p.proposal_id) or "ok"),
        evidence=evidence,
    )

    result = runtime.run(
        ExecutionContext("run-1", "trace-1", "operator-1"),
        ["agent.test"],
    )

    assert result.decision is PolicyDecision.ALLOW
    assert result.execution.executed is True
    assert executed == ["p1"]
    assert runtime.ledger.verify()
    assert len(runtime.ledger.events()) == 4
    assert runtime.memory.recall("agent.test")[0].outcome == "executed"


def test_factory_runtime_does_not_execute_denied_proposals() -> None:
    agents = AgentRuntime()
    proposal = Proposal("p2", "agent.test", "danger", "target", {}, 0.9, 0.9)
    agents.register(AgentSpec("agent.test"), lambda **_: AgentResult("agent.test", proposal))

    executed: list[str] = []
    runtime = FactoryRuntime(
        agents,
        PolicyGate(lambda _: PolicyDecision.DENY),
        ExecutionBoundary(lambda p: executed.append(p.proposal_id)),
    )

    result = runtime.run(ExecutionContext("run-2", "trace-2", "operator-1"), ["agent.test"])

    assert result.execution.executed is False
    assert executed == []
    assert runtime.ledger.verify()
