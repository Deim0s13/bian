# ADR-0001: Use a canonical typed graph

- Status: Accepted
- Date: 2026-08-17

## Context

BIAN concepts and relationships extend beyond OpenAPI, while future outputs need
stable identities, provenance, release comparison, and customer extensions.

## Decision

Represent the imported model as immutable snapshots containing typed artefacts
and typed directed relationships. Keep kind-specific data in validated
attributes/projection models. Do not make OpenAPI the canonical schema.

## Consequences

Multiple projections can share one source of truth and semantic diffs can work
at model level. We must govern identifiers, vocabularies, migrations, and
validation carefully; graph convenience may later justify indexed storage.

