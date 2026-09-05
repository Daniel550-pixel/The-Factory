# Runtime Hardening

The Factory separates reference contracts from deployment infrastructure. This document records the deterministic safeguards implemented in the kernel.

## Idempotency

`IdempotencyStore` records an execution receipt keyed by an operation key and fingerprint. Repeating the same operation returns the original result without re-running it. Reusing a key with a different fingerprint raises `IdempotencyConflict`.

The in-memory store is a reference implementation; durable adapters can persist receipts transactionally.

## Authorization audit

`AuthorizationAuditLog` provides an append-only audit surface for authorization decisions. Production adapters should persist these entries alongside the canonical event ledger.

## Failure injection

`FailureInjector` provides named deterministic checkpoints for resilience and recovery tests. It is deliberately small so tests can model failures without coupling the kernel to a specific worker or queue implementation.

## Design boundary

These primitives do not claim distributed durability by themselves. PostgreSQL, queue, worker, and observability integrations remain replaceable adapters. Production readiness additionally requires transactional persistence, retry semantics, failure-injection coverage, and authorization audit tests.
