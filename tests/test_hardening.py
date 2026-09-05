from factory.kernel.hardening import (
    AuthorizationAudit,
    AuthorizationAuditLog,
    FailureInjector,
    IdempotencyConflict,
    IdempotencyStore,
)


def test_idempotency_reuses_completed_result_without_reexecution() -> None:
    store = IdempotencyStore[str]()
    calls: list[str] = []

    def operation() -> str:
        calls.append("called")
        return "ok"

    assert store.execute_once("run-1", "fp-1", operation) == "ok"
    assert store.execute_once("run-1", "fp-1", operation) == "ok"
    assert calls == ["called"]


def test_idempotency_rejects_key_reuse_for_different_operation() -> None:
    store = IdempotencyStore[str]()
    store.execute_once("run-1", "fp-1", lambda: "ok")

    try:
        store.execute_once("run-1", "fp-2", lambda: "bad")
    except IdempotencyConflict:
        pass
    else:
        raise AssertionError("expected IdempotencyConflict")


def test_authorization_audit_is_append_only() -> None:
    audit = AuthorizationAuditLog()
    audit.record(AuthorizationAudit("run-1", "operator", "ALLOW", "p1", "policy passed"))
    audit.record(AuthorizationAudit("run-2", "operator", "DENY", "p2", "risk too high"))

    entries = audit.entries()
    assert [entry.decision for entry in entries] == ["ALLOW", "DENY"]


def test_failure_injector_is_deterministic() -> None:
    injector = FailureInjector()
    injector.fail("after-policy")

    try:
        injector.checkpoint("after-policy")
    except RuntimeError as exc:
        assert str(exc) == "injected failure: after-policy"
    else:
        raise AssertionError("expected injected failure")

    injector.clear("after-policy")
    injector.checkpoint("after-policy")
