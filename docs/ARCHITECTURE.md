# Factory Architecture

**Status: Working kernel contract — validated against current repository evidence; implementation remains subject to contract tests.**

## Design target

The Factory is an AI-native systems runtime. Products are composed from a small set of durable, governable primitives instead of each product inventing its own agent infrastructure.

## Kernel

The current candidate kernel contains four reusable primitives plus two cross-cutting contracts.

### 1. Event Ledger

Provides canonical, ordered, integrity-verifiable state transitions and the basis for replay and audit. The ledger is the durable source of truth; an in-process event bus or message transport is not equivalent to the ledger.

### 2. Policy Gate

Controls the transition from AI-generated proposals to authorized execution. It evaluates evidence, verification, confidence/risk, policy, and authorization requirements.

Core invariant: **AI decides ≠ AI executes.**

### 3. Agent Runtime

Provides agent registration, invocation, lifecycle management, specialist assessment, arbitration, and controlled access to tools/capabilities.

### 4. Context / Memory

Provides provenance-linked context, episodic experience, distilled knowledge, retrieval, and context assembly.

## Cross-cutting contracts

### Execution Context

Every meaningful operation should be correlatable through stable execution/trace/parent identifiers and actor/agent/capability metadata where applicable.

### Event Contract

Events should have explicit names, typed payloads, timestamps, causation/correlation context and provenance hooks. Transport may be in-process initially and distributed later.

## Supporting capabilities

These remain libraries or runtime capabilities rather than top-level kernel primitives:

- intent parsing
- reasoning strategies
- planning
- world-state schemas
- forecasting
- simulation
- evaluation
- resource planning
- external tool adapters
- observability exporters
- user interfaces

## Universal control flow

```text
OBSERVATION / CLAIM / REQUEST
              ↓
        CONTEXT ASSEMBLY
              ↓
       AGENT REASONING
              ↓
        PROPOSAL / PLAN
              ↓
     EVIDENCE + PROVENANCE
              ↓
         VERIFICATION
              ↓
        CONFIDENCE / RISK
              ↓
        POLICY DECISION
              ↓
     ALLOW / DENY / ESCALATE
              ↓
          EXECUTION
              ↓
       CANONICAL EVENT
              ↓
        REPLAY / AUDIT
              ↓
      MEMORY / LEARNING
```

Not every product needs every stage. The kernel guarantees the boundaries and contracts; products compose the stages they require.

## Reference architecture validation

The design has been cross-checked against mature high-level systems rather than treated as an isolated invention.

- **Temporal:** durable execution and recovery center on persisted workflow history, reinforcing durable history and replay as a platform concern.
- **LangGraph:** persistence/checkpointing and durable execution reinforce explicit state, resumability and human approval for agentic workflows.
- **Kubernetes:** reconciliation loops reinforce observe → determine desired transition → controlled mutation → observe again.
- **OpenTelemetry:** trace/resource context and structured logs/events reinforce universal correlation across runtime components without replacing the system of record.

These projects are architectural references, not Factory dependencies.

## Layering rule

```text
PRODUCT / DOMAIN
       ↓
WORKFLOWS / REASONING / SIMULATION
       ↓
FACTORY KERNEL CONTRACTS
       ↓
STORAGE / PROCESS / NETWORK ADAPTERS
       ↓
OPERATING ENVIRONMENT
```

The kernel must not absorb product schemas merely because a large product needs them.

## Non-goals during extraction

- Do not blindly merge complete source repositories.
- Do not make domain-specific telemetry part of the kernel.
- Do not introduce Kafka, Kubernetes, or microservices solely for architectural appearance.
- Do not allow an LLM to become the authoritative source for deterministic security or integrity decisions.
- Do not make a world model a mandatory kernel primitive.
- Do not make a particular LLM vendor or model a kernel dependency.

## Initial runtime target

The initial implementation target is a self-hosted, single-operator, Python-based modular runtime with durable storage and explicit process boundaries. Docker compatibility is expected. PostgreSQL is the preferred durable data layer unless extraction evidence indicates otherwise.

Distributed deployment can be introduced later without making it a prerequisite for the kernel.
