# ADR-0005: Use explicit extension registries and declarative profiles

- Status: Accepted
- Date: 2026-08-17

## Context

Source adapters, generators, validation rules, and security requirements vary.
Hard-coding security/compliance into BIAN artefacts would mix independent
concerns and make assertions misleading.

## Decision

Use small typed extension interfaces and an explicit in-process registry first.
Introduce package entry-point discovery only when external plugins exist.
Represent security and policy profiles declaratively; profiles reference model
elements and generator hooks but do not mutate imported BIAN assertions.

## Consequences

The core stays cloud/runtime neutral and profiles can evolve independently.
Third-party code is a trust boundary; allowlisting, version pinning, capability
limits, signing, and possibly out-of-process execution are required before an
open plugin ecosystem.

