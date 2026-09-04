# The Factory — Reference Architecture Benchmark

This document records high-level architecture patterns reviewed before implementation. References are used as benchmarks, not as implementation templates.

## Benchmarks

### Temporal

Temporal demonstrates a strong durable-execution model built around durable Event History, Workers, task queues, persistence, deterministic replay, and recovery. The Factory should adopt the architectural principle that execution state must be reconstructable from durable history, while keeping the Factory kernel smaller and domain-neutral.

Reference: https://github.com/temporalio/temporal
Architecture documentation: https://github.com/temporalio/documentation/blob/main/docs/encyclopedia/architecture/temporal-architecture.mdx

### LangGraph

LangGraph provides a low-level runtime for long-running, stateful agents with durable execution, persistence, memory, streaming, and human-in-the-loop control. Its checkpoint/thread model is particularly relevant to Factory Context, workflow state, interruption, and time-travel debugging.

Reference: https://github.com/langchain-ai/langgraph
Persistence documentation: https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/README.md

### OpenTelemetry

OpenTelemetry provides a vendor-neutral observability model for traces, metrics, logs, semantic conventions, and collection/export pipelines. Factory observability should follow the same separation between instrumentation semantics and backend implementations.

Reference: https://github.com/open-telemetry/opentelemetry-specification

## What The Factory takes from these systems

1. **Durable execution** — workflows must survive process failure and resume from recorded state.
2. **Event history as a system primitive** — state transitions must be inspectable and replayable.
3. **Deterministic replay** — replay must be a first-class verification capability.
4. **Explicit worker/runtime separation** — application/agent code should not be inseparably coupled to the persistence authority.
5. **Checkpointed context** — long-running agent state needs durable checkpoints and identifiable execution threads.
6. **Human-in-the-loop as a runtime primitive** — approval is part of execution governance, not a UI-only feature.
7. **Observability as infrastructure** — logs, metrics, traces, provenance, and audit events must remain distinguishable concepts.

## What The Factory does NOT copy

The Factory is not intended to become a clone of Temporal, LangGraph, OpenTelemetry, or another framework. Their abstractions are reference points used to pressure-test the Factory design.

The Factory must preserve its own core invariant:

> AI may propose, reason, assess, and plan. Authority to mutate external state belongs to an explicit, verifiable execution boundary.

## Current architectural direction

The working kernel remains:

```text
AGENT RUNTIME
      |
POLICY GATE
      |
EVENT LEDGER
      |
CONTEXT / MEMORY
```

The benchmark review strengthens the need for additional supporting capabilities around this kernel:

```text
                 FACTORY RUNTIME
                       |
       +---------------+---------------+
       |               |               |
   Scheduler       Workers        Observability
       |               |               |
       +---------------+---------------+
                       |
                  Agent Runtime
                       |
                  Policy Gate
                       |
                  Event Ledger
                       |
                Context / Memory
                       |
               Replay / Recovery
```

These are architectural directions, not final implementation commitments. They will be validated against the existing project lineage before the kernel API is frozen.
