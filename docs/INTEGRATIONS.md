# Integration status

The Factory now has provider-neutral seams for the requested integration set.

| Integration | Status | Boundary |
|---|---|---|
| Agent Runtime | Implemented | `factory/kernel/agents.py` |
| Context / Memory | Implemented | `context.py`, `memory.py` |
| Provenance / Evidence | Implemented | `provenance.py` |
| Execution Boundary | Implemented | `execution.py` |
| Arbitration / Consensus | Implemented | `agents.py` |
| Replay / Recovery | Implemented | `recovery.py` |
| PostgreSQL | Adapter implemented | `factory/postgres.py` |
| Observability | Implemented | `observability.py` |
| Tool / API adapters | Implemented | `adapters.py`, `api.py` |
| Human approval | Implemented | `human.py` |
| Model-provider abstraction | Implemented | `providers.py` |
| Workflow / Scheduler | Implemented | `scheduler.py` |
| Authentication / RBAC seam | Implemented | `security.py` |
| Docker | Implemented | `Dockerfile` |
| CI/CD quality | Implemented | `.github/workflows/ci.yml` |
| Security scanning | Implemented | `.github/workflows/security.yml` |
| Simulation / Evaluation | Implemented | `simulation.py` |
| Multi-tenant isolation | Contract implemented | `tenancy.py` |
| Worker layer | Implemented | `workers.py` |
| Distributed queue seam | Implemented | `queue.py` |
| Product integration | Boundaries created | `products/` |

## Important distinction

These are integration contracts and reference implementations, not claims that every external production service is fully deployed. External credentials, managed infrastructure, and vendor-specific drivers remain deployment concerns.

The kernel remains provider-neutral and preserves the invariant: **AI proposes; policy authorizes; execution is a separate boundary; the ledger records the resulting state transition.**
