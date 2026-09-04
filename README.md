# The Factory

**The Factory is an AI-native systems platform for building, orchestrating, verifying, and deploying intelligent applications through shared runtime primitives.**

> **Status: Architecture audit and extraction in progress.**

The Factory consolidates reusable architecture from a collection of AI, security, finance, intelligence, automation, and systems projects into one canonical engineering platform.

## Core hypothesis

The current working kernel hypothesis consists of four primitives:

```text
AGENT RUNTIME
registry · invocation · arbitration
          │
          ▼
POLICY GATE
proposal · evidence · verification · risk · authorization
          │
          ▼
EVENT LEDGER
canonical state · integrity · provenance · replay
          │
          ▼
CONTEXT / MEMORY
episodic experience · knowledge · retrieval · provenance
```

This architecture is **not yet considered final**. It is being derived and falsified through repository audits and extraction from the project's historical systems.

## Design principles

### AI decides ≠ AI executes

AI systems may analyze, reason, assess, and propose. Authorization and execution remain explicit system boundaries.

### Evidence before authority

Claims and proposals should be traceable to evidence, provenance, verification state, confidence, and policy.

### Everything important is replayable

State-changing operations should produce canonical events that can be reconstructed, verified, and audited.

### Deterministic controls remain deterministic

Probabilistic models should not silently replace deterministic security, policy, integrity, or authorization mechanisms.

### Products consume the kernel

Domain applications should use Factory primitives rather than independently rebuilding their own runtime, policy, memory, and audit mechanisms.

## Repository structure

The structure will evolve as the audit completes. The intended separation is:

```text
The-Factory/
├── kernel/          # stable reusable primitives
├── runtime/         # orchestration and lifecycle
├── intelligence/   # reasoning, forecasting, simulation, evaluation
├── products/       # domain applications built on the Factory
├── domains/        # domain-specific adapters and models
├── memory/         # contextual knowledge infrastructure
├── interfaces/     # APIs and external interfaces
├── infrastructure/ # deployment and operational infrastructure
├── tests/           # unit, integration, replay, and verification tests
└── docs/            # architecture, audits, and lineage
```

Directories are introduced only when their abstractions have been validated by the audit.

## Source projects

The Factory is being reconstructed from existing work rather than copying repositories wholesale. Current source lineages include:

- **BitMiner AI** — event ledger, deterministic replay, arbitration, risk, memory, and execution gating.
- **SecureOS** — deterministic trust, evidence, policy, integrity, and security enforcement.
- **ArchOS** — agent runtime, evidence chains, action gating, world state, simulation, and intelligence orchestration.
- **AI Venture Radar** — opportunity discovery, evidence-driven analysis, and continuous validation.
- **FinSight Global AI** — financial forecasting, trading, simulation, and SaaS product lineage.
- **FinSight Global AI 2** — experimental backend/product lineage.
- **FinSight Global AI Dashboard** — dashboard, paper-trading, forecasting, backtesting, and operational scripts.
- **NetworkLab** — reproducible network configuration, diagnostics, health checks, evidence collection, and operational runbooks.

Historical projects remain useful as source and provenance records. The Factory is the canonical destination for validated reusable architecture.

## Extraction workflow

Each source project follows the same process:

1. Inventory the implementation.
2. Identify state, event, and lifecycle primitives.
3. Identify verification and provenance mechanisms.
4. Identify agent/runtime abstractions.
5. Identify policy and authorization boundaries.
6. Identify memory and context mechanisms.
7. Identify replay and recovery capabilities.
8. Separate generic infrastructure from domain-specific behavior.
9. Extract reusable contracts and interfaces.
10. Reconstruct missing components directly in The Factory.
11. Preserve source lineage.
12. Validate the resulting kernel against multiple products.

## Project status

| Area | Status |
|---|---|
| Repository inventory | Complete |
| Cross-repository audit | In progress |
| BitMiner extraction analysis | Complete / first pass |
| SecureOS extraction analysis | Complete / first pass |
| ArchOS extraction analysis | Complete / first pass |
| AI Venture Radar analysis | Initial pass |
| FinSight lineage analysis | Initial pass |
| NetworkLab analysis | Initial pass |
| AIOS historical lineage | Pending deeper audit |
| Factory kernel implementation | Pending architecture lock |
| Product migrations | Pending kernel implementation |

## License

The Factory is released under the **Apache License 2.0**. See [LICENSE](LICENSE).

## Provenance

Every extracted primitive should be traceable through the following lineage:

```text
Historical project
      ↓
source / reconstruction
      ↓
Factory extraction
      ↓
generic primitive
      ↓
product / domain module
```

This provenance is part of the architecture, not optional documentation.
