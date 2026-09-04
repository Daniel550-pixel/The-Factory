# The Factory — Cross-Repository Extraction Audit

Date: 2026-09-04
Status: active architectural audit

## Method

Each existing repository is treated as source evidence. We extract reusable primitives, separate domain/UI/infrastructure code, preserve lineage, and reconstruct missing systems directly in The Factory. No repository is copied wholesale.

## 1. BitMiner AI

### Verified implementation
- Canonical event store: ordered events, previous-event hash chaining, SHA-256 event hashes, verification, hydration.
- Deterministic replay: reconstructs canonical event representations and compares replay hashes.
- Agent arbitration: specialist assessments, supporters/rejections, agreement, consensus state, confidence.
- Risk engine: derives LOW/GUARDED/HIGH/CRITICAL and execution posture RECOMMEND_ONLY/APPROVAL_REQUIRED/BLOCK.
- Memory: episodic records plus distilled knowledge rules with confidence and verification-cycle metadata.
- Execution: proposal/authorization/execution lifecycle with risk gating.

### Factory extraction
`kernel/event_ledger`, `kernel/replay`, `kernel/arbitration`, `kernel/policy`, `kernel/context`.

### Keep domain-specific
ASIC fleet state, mining economics, thermal controls, pool failover, rack operations and mining-specific heuristics remain under a BitMiner product/domain module.

### Assessment
**Highest-value kernel source discovered so far.**

## 2. SecureOS

### Verified implementation
- Deterministic baseline comparison is authoritative.
- Trust engine produces the numeric trust score and risk classification.
- AI analysis is explicitly advisory/read-only and cannot alter the ground-truth score.
- Telemetry is normalized before evaluation.
- Persistent JSONL event ledger uses canonicalized records, SHA-256 hash chaining and verification.
- Ledger records cover telemetry, trust snapshots, scenarios and actions.
- HTTP telemetry ingestion includes optional agent authentication and payload bounds.
- Action execution exists as an explicit API boundary.

### Factory extraction
- `kernel/event_ledger`: generic hash-chain ledger contract.
- `kernel/policy`: deterministic authority boundary and action authorization model.
- `kernel/provenance`: telemetry/evidence lineage.
- `kernel/arbitration`/risk interfaces: trust/risk outputs can feed policy without granting LLM authority.

### Keep domain-specific
Host integrity baselines, endpoint telemetry, Windows/PowerShell collection, MITRE mappings, security remediation and security UI remain SecureOS domain modules.

### Architectural significance
SecureOS independently validates a key Factory principle: **probabilistic AI must not overwrite deterministic ground truth**.

## 3. ArchOS

### Verified implementation/documentation
ArchOS describes an AI operating-system-style architecture combining experience modules, multimodal interaction, JARVIS orchestration, specialist agents, swarm infrastructure, world-model runtime, action gating, simulation, governance and infrastructure. The repository contains explicit agent runtime, evidence, action-gating and world-model components.

### Factory extraction candidates
- Agent registry/runtime and invocation.
- Action gate / governed execution.
- Evidence objects and evidence chains.
- Evidence ledger/persistence.
- Intent-to-command convergence.
- World-state interfaces.
- Scenario/simulation interfaces.
- Multimodal input as an adapter layer, not a kernel primitive.

### Keep domain/product-specific
3D experience/UI, UAE world model schemas, geographic/spatial intelligence, gesture interaction and presentation-specific components.

### Assessment
**Second major kernel source.** It is broader than BitMiner and therefore useful for identifying interfaces, but its architectural breadth must be flattened rather than copied as a tall sequential stack.

## 4. AI Venture Radar

### Verified implementation/documentation
Repository is currently architecture/product-definition stage. It defines a pipeline:
world data → observations → signals/anomalies → problems/friction → gap discovery → opportunity hypothesis → market/competition/feasibility analysis → adversarial validation → opportunity score → venture thesis → continuous re-evaluation.

It explicitly separates observation, signal, problem, gap, opportunity and validation. Derived claims are intended to retain provenance, confidence and counter-evidence. It also defines an opportunity graph with supports/contradicts/causes/depends_on/competes_with/affects relationships.

### Factory extraction
- Evidence/claim model.
- Provenance and confidence contracts.
- Adversarial evaluation/validator interface.
- Continuous re-evaluation lifecycle.
- Graph relationships as a generic knowledge/context capability.
- Agent roles as runtime consumers.

### Keep domain-specific
Market-gap detection, business opportunity scoring, competition analysis and venture thesis generation.

### Assessment
**Best validation consumer for the Factory kernel**, but not currently a major implementation source.

## 5. FinSight Global AI

### Verified implementation
The repository is an early Streamlit/Python deployment with a dashboard-oriented application and cloud/container scaffolding. The current repository tree is small and does not establish a reusable autonomous kernel comparable to BitMiner/SecureOS/ArchOS.

### Factory extraction
- Historical financial-analysis concepts only where they correspond to generic forecasting, evaluation or task interfaces.
- Deployment/container conventions may inform product adapters.

### Keep domain-specific
Financial dashboards, trading/forecasting logic, finance data ingestion and SaaS presentation.

### Assessment
**Product/ancestor lineage, not a kernel source.**

## 6. FinSight Global AI 2

### Verified implementation
The repository is Python-based and currently exposes a minimal FastAPI backend with a root health-style response and a `/run` endpoint. Repository metadata describes it as a newer generation AI creation/revolution project, but the verified code does not justify treating it as a mature kernel implementation.

### Factory extraction
No confirmed kernel primitive from the currently verified implementation.

### Keep domain-specific
FinSight/product experimentation.

### Assessment
**Historical/experimental lineage.** Architecture should be reconstructed from project history only where useful, not inferred from the repository name.

## 7. FinSight Global AI Dashboard

### Verified implementation
The repository is a Streamlit/Python trading dashboard lineage containing authentication, broker API, backtesting, deep-RL, Monte Carlo, sentiment, portfolio hedging, SaaS projection and numerous upgrade/restore scripts. The main dashboard explicitly defaults to paper mode.

### Factory extraction
- Paper-mode/safe execution concepts may inform generic execution-mode contracts.
- Backtesting/simulation concepts may inform the generic simulation interface.
- Alert/auth boundaries may inform adapters.

### Keep domain-specific
Trading, broker integrations, portfolio logic, market sentiment, RL and financial projections.

### Assessment
**Finance product lineage; useful for simulation/execution semantics, not kernel ownership.**

## 8. NetworkLab

### Verified implementation
Controlled, reproducible infrastructure lab for installation, configuration, management, monitoring, diagnostics, testing, reporting and evidence. Network-changing operations are disabled by default and require explicit lab-scope controls and an interface. GitHub Actions provides validation.

### Factory extraction
- Guarded execution / explicit scope controls.
- Reproducible runbook/evidence pattern.
- Configuration-driven validation.
- Testable infrastructure task contracts.

### Keep domain-specific
Network adapters, PowerShell administration, topology configuration and stage-specific procedures.

### Assessment
**Separate engineering lineage**, but its safety and evidence patterns are useful to Factory execution policy.

## Consolidated findings

### Strong kernel evidence
1. Event Ledger — BitMiner + SecureOS independently implement it.
2. Policy/Execution Gate — BitMiner + SecureOS + ArchOS independently converge on it.
3. Agent Runtime/Arbitration — BitMiner + ArchOS provide concrete evidence.
4. Context/Memory — BitMiner provides episodic + distilled knowledge; ArchOS provides evidence persistence and world-model context.
5. Replay — BitMiner provides deterministic replay; ArchOS provides replayable intelligence as an architectural requirement.
6. Provenance/Evidence — SecureOS, ArchOS and Venture Radar converge on this.

### Revised Factory kernel hypothesis

```text
EVENT LEDGER
    canonical state / events / integrity / replay anchor

POLICY GATE
    evidence / verification / risk / authorization / execution boundary

AGENT RUNTIME
    registry / invocation / arbitration / specialist execution

CONTEXT + MEMORY
    evidence / episodic memory / distilled knowledge / retrieval / provenance
```

Replay and provenance are currently best treated as cross-cutting kernel capabilities rather than necessarily independent top-level runtime layers.

### Important conclusion

The original four-primitive hypothesis is becoming stronger, but it is not yet final. The next architectural task is to inspect the AIOS lineage (GSCIE, FGSE, AI-mainframe, AIOS-Core-Architect and historical J.A.R.V.I.S.) and determine whether those projects contain an earlier implementation of the same contracts.

## Lineage rule

```text
historical project
      ↓
verified implementation / reconstructed specification
      ↓
Factory extraction
      ↓
generic contract
      ↓
product/domain implementation
```

No historical codename is treated as a required final Factory component name.
