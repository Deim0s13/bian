# ADR-0004: Store immutable canonical snapshots as files first

- Status: Accepted
- Date: 2026-08-17

## Context

Phase 1 needs reproducibility and inspection, while query shapes, tenancy, and
workflow requirements are unknown.

## Decision

Persist canonical, content-addressed JSON snapshots and manifests through a
repository boundary. Keep raw authorised inputs outside generated output.
Adopt PostgreSQL for indexed metadata and object storage for source/generated
blobs only when real query and multi-user requirements emerge.

## Consequences

Files are transparent, diffable, and operationally trivial. They do not provide
concurrency, rich graph queries, or access control. The repository port and
immutable snapshot semantics reduce later migration risk.

