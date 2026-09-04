# Contributing to The Factory

## Architecture first

The Factory is under active architectural extraction. Do not introduce a new subsystem merely because a source project contains it. First establish whether the capability is generic, domain-specific, experimental, or historical.

## Change principles

- Keep kernel primitives small and composable.
- Preserve the distinction between proposal, authorization, and execution.
- Prefer deterministic verification for integrity and policy decisions.
- Make important state transitions observable through canonical events.
- Preserve provenance when extracting code or concepts from source projects.
- Keep product/domain logic outside the kernel unless it is demonstrably reusable.
- Add tests for replay, authorization, integrity, and failure paths where applicable.
- Avoid premature distributed infrastructure.

## Source lineage

When extracting from an existing project, document the source repository and original component in the relevant audit or lineage documentation.

## Pull requests

A useful change should explain:

1. What capability is being added or changed.
2. Why it belongs in The Factory.
3. Which source lineage or requirement motivated it.
4. Whether it is kernel, runtime, intelligence, product, domain, or infrastructure code.
5. How the change is tested.

Architecture changes should include an updated design document when they alter a stable interface or kernel boundary.
