# The Factory — Project & Repository Migration

## Purpose

The Factory is the canonical implementation repository for reusable architecture extracted from the user's historical and current AI/system projects.

The migration rule is:

1. Existing repository → inspect actual implementation, extract reusable primitives, separate domain-specific code, preserve provenance.
2. No repository → reconstruct the project from the available historical architecture/specification/context, then implement it in The Factory.
3. Do not blindly copy projects. Rebuild reusable capabilities around the Factory kernel.
4. Preserve original repositories as historical/source references unless explicitly retired later.

## Current repository inventory

| Project | Repository | Initial classification |
|---|---|---|
| ArchOS | `Daniel550-pixel/ArchOS-Repo` | Architecture/world-model/runtime lineage |
| SecureOS | `Daniel550-pixel/SecureOS` | Security / integrity domain + kernel candidates |
| BitMiner AI | `Daniel550-pixel/BitMiner-AI` | Strongest current kernel candidate |
| AI Venture Radar | `Daniel550-pixel/AI-Venture-Radar` | Kernel consumer / validation product |
| FinSight Global AI | `Daniel550-pixel/FinSight-Global-AI` | Finance product/domain |
| FinSight Global AI 2 | `Daniel550-pixel/FinSight-Global-AI-2` | Finance product/domain / later lineage |
| FinSight Global AI Dashboard | `Daniel550-pixel/FinSight_Global_AI_Dashboard` | Experience/UI layer |
| NetworkLab | `Daniel550-pixel/NetworkLab` | Separate networking/stage engineering lineage |

Additional historical projects without a verified dedicated repository will be reconstructed directly under The Factory when their architecture is sufficiently specified.

## Audit workflow

For every repository:

- inventory the implementation;
- identify event/state primitives;
- identify verification/provenance mechanisms;
- identify agent/runtime mechanisms;
- identify policy/authorization boundaries;
- identify memory/context mechanisms;
- identify replay/recovery mechanisms;
- identify reasoning/simulation capabilities;
- classify domain-specific code;
- identify reusable contracts/interfaces;
- identify missing pieces;
- extract or reconstruct the reusable implementation in The Factory;
- attach source lineage to the resulting module.

## Working kernel hypothesis

The current hypothesis is four core primitives:

- Event Ledger — canonical state, append-only events, replay and audit.
- Policy Gate — proposal, evidence, verification, authorization and execution boundary.
- Agent Runtime — registration, invocation, lifecycle and arbitration.
- Context / Memory — retrieval, knowledge, episodic state and provenance-linked context.

This is a hypothesis, not a final architecture. Repository audits are explicitly intended to falsify or refine it.

## BitMiner AI — first extraction findings

The BitMiner implementation contains strong candidates for generic Factory infrastructure:

- canonical event storage and integrity chaining;
- deterministic replay and replay verification;
- agent assessment and consensus;
- confidence and risk assessment;
- proposal → authorization → execution separation;
- execution logging;
- episodic memory;
- distilled knowledge/rules with confidence and verification-cycle metadata.

Mining fleet telemetry, ASIC-specific state, hashrate, cooling, curtailment, mining economics and other Bitcoin-specific mechanisms remain domain-level concerns unless later audits prove otherwise.

## Reconstruction policy

Historical names such as J.A.R.V.I.S., ULTRON and IRIS are treated as project lineage/codenames rather than mandatory Factory product names. Their surviving technical concepts may be reconstructed under neutral Factory modules.

## Status

Architecture audit and extraction are in progress. The Factory repository is the canonical destination for validated reusable implementations; source repositories remain evidence and historical lineage.
