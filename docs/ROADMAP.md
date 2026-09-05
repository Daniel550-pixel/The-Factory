# The Factory Roadmap

## Phase 0 — Architecture audit

- [x] Register all known source repositories
- [x] Establish migration and provenance rules
- [x] Audit BitMiner AI
- [x] Audit SecureOS at architectural level
- [x] Audit ArchOS lineage at architectural level
- [x] Audit FinSight repositories
- [x] Audit AI Venture Radar
- [x] Audit NetworkLab
- [x] Benchmark high-level agent/runtime architectures
- [x] Reconstruct the current AIOS lineage as a documented lineage item

## Phase 1 — Kernel contracts

- [x] Event model and append-only ledger contract
- [x] Provenance and evidence model
- [x] Policy proposal/decision contract
- [x] Authorization and execution boundary
- [x] Agent registry and invocation contract
- [x] Arbitration and confidence contract
- [x] Context/memory contract
- [x] Replay and recovery contract
- [x] Human approval/interruption contract

## Phase 2 — Reference implementation

- [x] Python kernel package
- [x] In-memory implementation for deterministic tests
- [x] PostgreSQL persistence adapter
- [x] Worker/runtime abstraction
- [x] Task lifecycle
- [x] Structured observability
- [x] Security controls
- [x] Provider and tool adapter registries
- [x] Scheduler and queue abstractions
- [x] Single-process end-to-end orchestration runtime

## Phase 3 — Product extraction

- [ ] BitMiner product adapter
- [ ] SecureOS product adapter
- [ ] AI Venture Radar product adapter
- [ ] FinSight product adapter
- [ ] Additional historical projects reconstructed where no repository survives

## Phase 4 — Production hardening

- [x] Contract test suite foundation
- [x] Deterministic replay foundation
- [ ] Failure injection
- [ ] Idempotency guarantees
- [ ] Authorization audit tests
- [x] Supply-chain security automation
- [x] Containerized deployment baseline
- [x] CI/CD quality and security baseline
- [x] Documentation and reference examples

## Phase 5 — Scale

- [x] Distributed worker abstraction
- [x] Durable queue abstraction
- [x] Multi-tenant isolation contract
- [ ] Horizontal scaling validation
- [x] Pluggable model providers
- [x] Simulation and evaluation foundation

Scaling remains an implementation concern: the reference runtime is intentionally
single-process until failure semantics, idempotency, and persistence guarantees
are demonstrated under test.
