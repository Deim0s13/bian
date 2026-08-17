# Roadmap

## Phase 1 — Trustworthy model engine

### M1: Foundation (implemented in this repository)

- architecture, product boundaries, and decision records;
- synthetic source adapter with explicit classification;
- canonical artefact/relationship graph with per-element provenance;
- validation and deterministic JSON/summary generation;
- reproducibility manifest and automated tests.

### M2: Authoritative R14 ingestion

- confirm BIAN access, licence, attribution, caching, and derived-output terms;
- inventory official R14 artefact formats and stable identifiers;
- implement adapters without changing the canonical model unnecessarily;
- select 5–10 actual domains based on source availability;
- reconcile the established 258-domain/242-published-API distinction from the
  authoritative inventory and record evidence for the result;
- create conformance fixtures that contain only redistributable material.

Exit: a reproducible snapshot whose every item traces to an authorised R14
source and whose import report explains rejected or unsupported items.

### M3: First engineering projection

- generate normalised OpenAPI for domains that actually publish API operations;
- preserve upstream operation/schema traceability in extensions or manifests;
- create generated contract packages and owned implementation examples;
- add golden-file, schema, and regeneration tests;
- define compatibility policy for generator upgrades.

Exit: one useful service/API artefact can be regenerated without modifying
owned implementation code.

### M4: Release-aware foundation

- ingest a second authorised source release when available;
- implement identity-aware semantic diff and impact classifications;
- connect changed model elements to generated outputs;
- publish a machine-readable and human-readable impact report.

## Deferred explicitly

- full R14 breadth, AsyncAPI, SDKs, test harness generation, and deployment IaC;
- Backstage/RHDH plugins, templates, and catalogue publication;
- application discovery and AI-assisted BIAN alignment;
- business-scenario modelling and current/target-state visualisation;
- multi-user workflows, governance scorecards, and portfolio roadmaps;
- security profiles, control libraries, evidence stores, and attestations;
- production API, PostgreSQL, object storage, queues, and cloud deployment;
- certification or compliance claims of any kind.

