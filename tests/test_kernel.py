from factory.kernel import EventLedger, PolicyDecision, PolicyGate, Proposal


def test_event_ledger_is_hash_chained_and_replayable() -> None:
    ledger = EventLedger()
    first = ledger.append("proposal.created", {"id": "p1"}, "2026-09-04T00:00:00Z")
    second = ledger.append(
        "policy.evaluated",
        {"decision": "ALLOW"},
        "2026-09-04T00:00:01Z",
        causation_id=first.event_hash,
    )

    assert first.sequence == 1
    assert second.previous_hash == first.event_hash
    assert ledger.verify()
    assert ledger.replay() == ledger.events()


def test_policy_gate_is_not_an_executor() -> None:
    gate = PolicyGate(lambda proposal: PolicyDecision.ALLOW if proposal.risk < 0.5 else PolicyDecision.ESCALATE)
    proposal = Proposal(
        proposal_id="p1",
        actor_id="agent.test",
        action="example.action",
        target="example.target",
        parameters={},
        confidence=0.9,
        risk=0.2,
    )

    assert gate.evaluate(proposal) is PolicyDecision.ALLOW
