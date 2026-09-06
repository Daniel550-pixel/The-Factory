# Provider-Independent Knowledge Layer

## Status

**Accepted architectural direction — implementation pending.**

The Factory must not depend on a Claude subscription or on any single model provider for its persistent knowledge, provenance, memory, or orchestration architecture.

The open-source `claude-obsidian` project may be used as a reference implementation and optional knowledge-management adapter, but it is not a Factory runtime dependency.

## Objective

Provide The Factory with a persistent engineering knowledge layer that can:

- retain architecture decisions and rationale;
- preserve source-project lineage and provenance;
- store audit findings and unresolved questions;
- support retrieval across historical and current Factory knowledge;
- maintain human-readable Markdown knowledge where appropriate;
- remain usable when Claude is unavailable;
- allow multiple model providers to operate against the same knowledge layer;
- keep runtime memory separate from development/engineering knowledge.

## Architectural rule

```text
AI PROVIDER != KNOWLEDGE STORE != FACTORY RUNTIME
```

A model provider is replaceable infrastructure. Persistent knowledge and Factory runtime semantics must remain provider-independent.

## Reference integration: claude-obsidian v2.1.1

`claude-obsidian` is an open-source, local-first Obsidian knowledge companion. Its product package and user-owned vault are separate concepts. The Factory may adopt compatible ideas from the project without making Claude Code a hard dependency.

Reference release:

- Repository: https://github.com/AgriciDaniel/claude-obsidian
- Target release: `v2.1.1`

The reference project provides useful patterns for persistent Markdown knowledge, wiki indexing, provenance-oriented notes, ingestion, retrieval, linting, session context, and Agent Skills. These capabilities should be treated as an adapter/reference layer rather than copied wholesale into the Factory kernel.

## Factory architecture

```text
                         THE FACTORY
                              │
             ┌────────────────┴────────────────┐
             │                                 │
       FACTORY RUNTIME                  ENGINEERING KNOWLEDGE
             │                                 │
    Agent Runtime / Policy              Knowledge Adapter API
    Event Ledger / Runtime Memory               │
             │                       ┌─────────┼─────────┐
             │                       │         │         │
             │                    Obsidian   Files    Database
             │                    adapter    adapter   adapter
             │                       │
             │                  claude-obsidian
             │                       │
             └──────────────┬────────┘
                            │
                    Provider Abstraction
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
        OpenAI            Gemini           Claude
          │                 │                 │
          └─────────────────┴─────────────────┘
```

## Separation of memory types

The Factory must distinguish at least two memory domains.

### 1. Engineering knowledge

Persistent, human-auditable knowledge about the construction of The Factory:

- architecture decisions;
- source lineage;
- audits;
- design rationale;
- rejected alternatives;
- security assumptions;
- invariants;
- contracts;
- test requirements;
- unresolved questions;
- research and evidence.

This may be represented in Obsidian/Markdown and indexed by a provider-neutral retrieval layer.

### 2. Runtime memory

Machine-readable state associated with Factory execution:

- events;
- execution state;
- agent episodes;
- task context;
- evidence references;
- replay data;
- authorization state;
- recovery state.

Runtime memory belongs to the Factory kernel/runtime and must not depend on an Obsidian vault being present.

## Provider abstraction

All model-dependent functionality must cross an explicit provider interface.

Conceptually:

```text
ModelProvider
├── generate()
├── structured_generate()
├── embed()
├── inspect_capabilities()
└── health()
```

Possible implementations include:

```text
OpenAIProvider
GeminiProvider
ClaudeProvider
LocalModelProvider
MockProvider
```

The kernel must depend on the interface, never on a provider-specific SDK directly.

## Knowledge adapter abstraction

Persistent engineering knowledge should likewise cross an adapter boundary.

```text
KnowledgeStore
├── ingest()
├── search()
├── get()
├── upsert()
├── link()
├── list_sources()
├── record_provenance()
└── health()
```

Possible implementations:

```text
ObsidianKnowledgeStore
FilesystemKnowledgeStore
DatabaseKnowledgeStore
GitKnowledgeStore
```

`claude-obsidian` can therefore become an `ObsidianKnowledgeStore` implementation/reference without becoming part of the Factory kernel itself.

## Provenance requirements

Every important extracted architectural claim should retain:

```text
source
  ↓
location / artifact
  ↓
observation
  ↓
interpretation
  ↓
Factory primitive
  ↓
validation status
```

Claims must be distinguishable as:

- `implemented`
- `observed`
- `inferred`
- `proposed`
- `rejected`
- `unresolved`

The knowledge layer must never turn an inference into an implementation claim merely because an AI model generated it.

## Claude subscription independence

The Factory knowledge architecture remains fully usable without a Claude subscription.

Without Claude, users may still:

- use Obsidian;
- store and version Markdown knowledge;
- use the Factory knowledge APIs;
- run deterministic indexing and validation;
- use other supported model providers;
- run tests and audits;
- inspect and modify the knowledge base manually.

Claude becomes an optional model/agent adapter rather than a prerequisite for the platform.

## Development workflow

The intended Factory workflow is:

```text
1. Inspect source repository
        ↓
2. Extract observations
        ↓
3. Record provenance
        ↓
4. Store engineering knowledge
        ↓
5. Cross-project comparison
        ↓
6. Architecture lock
        ↓
7. Define kernel contracts
        ↓
8. Implement deterministic kernel
        ↓
9. Verify and replay
        ↓
10. Migrate products
```

AI may accelerate steps 2–6, but it must not silently bypass deterministic verification or authorization boundaries.

## Non-goals

This integration does **not** mean:

- copying the `claude-obsidian` repository into The Factory;
- making Claude Code mandatory;
- storing runtime state only in Obsidian;
- treating Markdown as the authoritative runtime event ledger;
- allowing an AI provider to become the authorization layer;
- replacing deterministic Factory controls with AI instructions.

## Decision

The Factory adopts **provider-independent knowledge architecture** as a core design constraint.

`claude-obsidian v2.1.1` is an optional reference/adapter candidate for the engineering knowledge layer. The Factory kernel remains independent of Claude, Obsidian, and any other specific AI or knowledge product.
