# The Factory — AIOS Lineage Audit

Date: 2026-09-04
Status: active

## Scope

This audit isolates the reusable runtime ideas represented by the historical AIOS / J.A.R.V.I.S. / ArchOS lineage. Historical names are treated as lineage, not as required Factory components.

## Verified ArchOS implementation evidence

`ArchOS-Repo/src/aios/runtime.ts` implements a concrete event-driven runtime state machine. It maintains runtime state, subscriptions, initialization/shutdown, command dispatch, system-state transitions and context transitions. Commands and state transitions carry trace IDs and optional parent trace IDs. The runtime is therefore evidence for a generic **runtime + event + execution-context** contract.

`ArchOS-Repo/src/aios/events.ts` defines a typed event map covering command input, gestures, system state, system context, world updates, agent lifecycle and intelligence lifecycle. It also provides subscription, emission and cleanup semantics and protects other observers when one observer throws. This is evidence for a typed **event contract / event bus** capability.

## Architectural extraction

### 1. Event contract

Factory should distinguish the event **contract** from the durable Event Ledger.

```text
Event Contract
  typed event name
  payload
  timestamp
  trace_id
  parent_trace_id
       |
       v
Event Ledger
  durable ordering
  integrity
  replay
  provenance
```

The ArchOS event bus is an in-process transport/observer mechanism. BitMiner and SecureOS provide the stronger evidence for durable canonical storage and hash-chained integrity. These must not be conflated.

### 2. Execution context / correlation

ArchOS explicitly propagates `traceId` and `parentTraceId` through command, state, context, agent and intelligence events. This should become a first-class Factory context contract rather than a UI-specific field.

Target concept:

```text
ExecutionContext
  execution_id
  trace_id
  parent_id
  actor / agent
  capability
  policy_context
  causation
  correlation
```

### 3. Agent lifecycle

The event taxonomy explicitly represents agent creation, start, completion and failure. This supports the Factory Agent Runtime, but lifecycle telemetry must remain separate from agent business logic.

### 4. Intelligence lifecycle

ArchOS models intent → reasoning → planning → verification as lifecycle phases. This is useful as a workflow/telemetry convention, but these phases should **not** become mandatory kernel layers. Different products may skip, merge or reorder reasoning strategies while retaining the same runtime/policy/event contracts.

### 5. World updates

ArchOS includes entity, spatial, temporal and simulation update events. These validate that domain state changes can flow through the event contract. World-model semantics remain a product/domain concern and are not promoted into the kernel.

## Lineage conclusion

The AIOS lineage adds an important missing distinction to the Factory model:

```text
                    FACTORY KERNEL

  AGENT RUNTIME ──── Execution Context
       │                    │
       ├──────────────┐     │
       ▼              ▼     ▼
   POLICY GATE ─── EVENT CONTRACT
       │              │
       ▼              ▼
   EXECUTION      EVENT LEDGER
                      │
                 replay / audit
                      │
                context / memory
```

The durable Event Ledger remains authoritative. The in-process event bus is an adapter/transport implementation, not the ledger itself.

## High-level reference check

The extracted model was compared against established architectures:

- **Temporal:** durable execution and recovery are centered on persisted workflow history; this reinforces durable history/replay as a platform primitive rather than ordinary logging.
- **LangGraph:** checkpointed state, persistence, durable execution and human-in-the-loop reinforce explicit execution state and resumability for agentic workflows.
- **Kubernetes:** reconciliation loops reinforce the pattern of observing state, computing a desired transition, and producing controlled state-changing events rather than treating an agent's internal reasoning as authority.
- **OpenTelemetry:** trace context, resource context and structured logs/events reinforce the need for cross-system correlation and a standardized telemetry/context layer without making observability itself the source of truth.

These are reference validations, not dependencies. The Factory should implement its own contracts and use adapters where interoperability is useful.

## Kernel impact

### Promoted
- Event contract
- Execution/correlation context
- Agent lifecycle model
- Intelligence lifecycle as optional workflow metadata
- Event bus as a transport adapter

### Not promoted
- ULTRON UI/experience layer
- UAE world model schema
- spatial/temporal domain models
- presentation-specific state
- historical J.A.R.V.I.S. naming
- mandatory intent/reasoning/planning layer decomposition

## Current confidence

| Capability | Confidence | Evidence |
|---|---:|---|
| Event Ledger | High | BitMiner + SecureOS |
| Policy / Execution Gate | High | BitMiner + SecureOS + ArchOS |
| Agent Runtime | High | BitMiner + ArchOS |
| Arbitration | High | BitMiner + ArchOS |
| Context / Memory | High | BitMiner + ArchOS |
| Provenance / Evidence | High | SecureOS + ArchOS + Venture Radar |
| Replay | High | BitMiner + ArchOS |
| Execution Context | High | ArchOS + external architecture references |
| Event Bus / Transport | High | ArchOS |
| World Model | Domain-specific | ArchOS |

## Result

The Factory kernel should remain **small and composable**. The AIOS lineage does not justify adding more top-level layers. Instead, it strengthens the contracts around events, execution context and agent lifecycle while confirming that world-model, reasoning and experience concerns belong above the kernel.
