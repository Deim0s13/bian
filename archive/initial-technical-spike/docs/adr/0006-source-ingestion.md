# ADR-0006: Ingest BIAN through release-specific adapters

- Status: Accepted
- Date: 2026-08-17

## Context

Official packages may contain multiple formats and evolve between releases.
Their availability does not imply redistribution rights, and the engine must
not invent missing operations.

## Decision

Each adapter consumes source bytes, computes a digest, validates an explicit
release/classification envelope, and maps supported assertions into the
canonical graph with per-element provenance. Unsupported and absent content is
reported, not synthesised. Raw sources are not committed unless their terms
explicitly allow it. Synthetic fixtures use their own classification.

## Consequences

Source changes are isolated and auditable, and real BIAN packages can replace
fixtures without replacing the core. Adapters require release-specific tests
and completeness reports. Source licensing remains an operational gate.

