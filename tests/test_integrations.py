from factory.kernel import (
    AgentResult, AgentRuntime, AgentSpec, Arbitrator, ContextItem, ContextStore,
    Evidence, EvidenceStore, ExecutionBoundary, MemoryRecord, MemoryStore,
    PolicyDecision, PolicyGate, Proposal, ReplayEngine, SimulationEngine,
)


def proposal(pid: str = "p1", risk: float = .2) -> Proposal:
    return Proposal(pid, "agent.test", "test.action", "test.target", {}, .9, risk, ("e1",))


def test_context_provenance_memory_and_runtime() -> None:
    context = ContextStore()
    context.put(ContextItem("c1", {"signal": 1}, ("e1",), .9))
    evidence = EvidenceStore()
    evidence.add(Evidence("e1", "test", "signal observed", .95))
    memory = MemoryStore()
    memory.remember(MemoryRecord("m1", "agent.test", "learned", ("e1",)))
    runtime = AgentRuntime()
    runtime.register(AgentSpec("agent.test", ("test",)), lambda **_: AgentResult("agent.test", proposal()))
    result = runtime.invoke("agent.test")
    assert context.get("c1") is not None
    assert evidence.require(("e1",))[0].strength == .95
    assert memory.recall("agent.test")
    assert Arbitrator.select([result]).selected_agent == "agent.test"


def test_policy_execution_and_replay() -> None:
    gate = PolicyGate(lambda p: PolicyDecision.ALLOW if p.risk < .5 else PolicyDecision.ESCALATE)
    p = proposal()
    decision = gate.evaluate(p)
    executed = ExecutionBoundary(lambda _: "ok").execute(p, decision)
    assert executed.executed
    from factory.kernel import EventLedger
    ledger = EventLedger()
    ledger.append("execution.committed", {"proposal_id": p.proposal_id}, "2026-09-04T00:00:00Z")
    assert ReplayEngine.inspect(ledger).valid


def test_simulation_does_not_mutate_source() -> None:
    state = {"value": 1}
    result = SimulationEngine().run("double", state, lambda s: {**s, "value": s["value"] * 2})
    assert state["value"] == 1
    assert result.state["value"] == 2
