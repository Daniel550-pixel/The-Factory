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
- [ ] Complete deep AIOS lineage reconstruction: GSCIE → FGSE → AI-mainframe → AIOS-Core-Architect → ArchOS

## Phase 1 — Kernel contracts

- [ ] Event model and append-only ledger contract
- [ ] Provenance and evidence model
- [ ] Policy proposal/decision contract
- [ ] Authorization and execution boundary
- [ ] Agent registry and invocation contract
- [ ] Arbitration and confidence contract
- [ ] Context/memory contract
- [ ] Replay and recovery contract
- [ ] Human approval/interruption contract

## Phase 2 — Reference implementation

- [ ] Python kernel package
- [ ] In-memory implementation for deterministic tests
- [ ] PostgreSQL persistence adapter
- [ ] Worker/runtime abstraction
- [ ] Task lifecycle
- [ ] Structured observability
- [ ] Security controls

## Phase 3 — Product extraction

- [ ] BitMiner product adapter
- [ ] SecureOS product adapter
- [ ] AI Venture Radar product adapter
- [ ] FinSight product adapter
- [ ] Additional historical projects reconstructed where no repository survives

## Phase 4 — Production hardening

- [ ] Contract test suite
- [ ] Deterministic replay test suite
- [ ] Failure injection
- [ ] Idempotency guarantees
- [ ] Authorization audit tests
- [ ] Supply-chain security
- [ ] Containerized deployment
- [ ] CI/CD hardening
- [ ] Documentation and examples

## Phase 5 — Scale

- [ ] Distributed worker execution
- [ ] Durable queues where justified
- [ ] Multi-tenant isolation if required
- [ ] Horizontal scaling
- [ ] Pluggable model providers
- [ ] Advanced simulation and evaluation

Scaling is intentionally deferred until the single-node kernel contracts are proven.
