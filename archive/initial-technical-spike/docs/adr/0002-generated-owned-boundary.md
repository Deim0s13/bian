# ADR-0002: Enforce a generated-versus-owned code boundary

- Status: Accepted
- Date: 2026-08-17

## Context

BIAN release and generator upgrades must not overwrite bank-specific behaviour.
Merge markers and hand-edited generated files make provenance ambiguous.

## Decision

Treat generated outputs as disposable. Future service generators emit contract/
scaffold packages behind stable interfaces; developer-owned implementations,
adapters, policies, and configuration live in separate packages/directories.

## Consequences

Regeneration is safe and testable, and ownership is obvious. Interface design
and compatibility discipline become mandatory. Some frameworks that expect
inline generated/owned code will need adapters.

