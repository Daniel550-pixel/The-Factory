# Factory Architecture

**Status: Working hypothesis — subject to validation during repository extraction.**

## Kernel

The current candidate kernel contains four reusable primitives.

### 1. Event Ledger

Provides canonical, ordered, integrity-verifiable state transitions and the basis for replay and audit.

### 2. Policy Gate

Controls the transition from AI-generated proposals to authorized execution. It evaluates evidence, verification, confidence/risk, policy, and authorization requirements.

### 3. Agent Runtime

Provides agent registration, invocation, lifecycle management, specialist assessment, and arbitration.

### 4. Context / Memory

Provides provenance-linked context, episodic experience, distilled knowledge, and retrieval.

## Supporting capabilities

These should remain libraries or runtime capabilities until evidence shows they deserve kernel status:

- intent parsing
- reasoning strategies
- world-state schemas
- forecasting
- simulation
- evaluation
- resource planning
- external tool adapters
- user interfaces

## Universal control flow

```text
CLAIM / PROPOSAL
       ↓
EVIDENCE
       ↓
PROVENANCE / ATTESTATION
       ↓
VERIFICATION
       ↓
CONFIDENCE / RISK
       ↓
POLICY DECISION
       ↓
ALLOW / DENY / ESCALATE
       ↓
EXECUTE
       ↓
EVENT
       ↓
REPLAY / AUDIT
```

The objective is to establish one consistent control boundary across products without forcing every product into the same domain model.

## Non-goals during extraction

- Do not blindly merge complete source repositories.
- Do not make domain-specific telemetry part of the kernel.
- Do not introduce Kafka, Kubernetes, or microservices solely for architectural appearance.
- Do not allow an LLM to become the authoritative source for deterministic security or integrity decisions.
- Do not freeze the architecture before the historical AIOS lineage is audited.

## Initial runtime target

The initial implementation target is a self-hosted, single-operator, Python-based modular runtime with durable storage and explicit process boundaries. Docker compatibility is expected. PostgreSQL is the preferred durable data layer unless extraction evidence indicates otherwise.

Distributed deployment can be introduced later without making it a prerequisite for the kernel.
