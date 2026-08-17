# Decisions and questions

## Working assumptions

- The engine must represent a Service Domain even when it has no published API.
- The stated R14 counts (258 Service Domains and 242 published API specs) are a
  requirement to verify against an authorised source during M2, not data baked
  into the code or used as proof of source completeness.
- Stable identifiers should come from authoritative sources when available;
  adapter-created IDs must be namespaced and disclosed.
- Customer mappings and inferred relationships are separate assertions with
  distinct provenance, never mutations presented as BIAN facts.
- Determinism means identical source bytes plus engine/generator versions yield
  byte-identical canonical and projection outputs.
- A solo/small team benefits from a modular monolith until operational scaling
  or organisational ownership provides evidence for service decomposition.

## Licensing and source-data gates

No official BIAN artefacts have been downloaded or copied into this repository.
The fixture is synthetic and labelled as such. Before authoritative ingestion
or commercialisation, obtain and record answers to:

- Which BIAN licence/terms govern each source package and release?
- May source artefacts be cached, transformed, embedded in generated outputs,
  redistributed to customers, or used in a hosted multi-tenant product?
- What attribution, notices, access controls, and deletion obligations apply?
- Are repository files, portal exports, schemas, diagrams, and documentation
  governed by the same terms?
- Can conformance test fixtures include excerpts, or must tests use hashes and
  locally supplied customer copies?
- Who is authorised to assert that an imported package is complete and genuine?

Answers need legal/commercial review. The architecture cannot settle them.

## Questions to resolve during M2

- What are the authoritative R14 package locations, formats, checksums, and
  identifiers, and are machine-readable artefacts internally consistent?
- Which 5–10 domains provide the best structural coverage: APIs present/absent,
  schemas, behaviour qualifiers, events, and cross-domain relationships?
- Does BIAN provide identifiers stable enough across releases for semantic diff,
  or is a documented identity reconciliation layer required?
- Which relationships are explicit in sources versus inferred from naming or
  schemas? Inferences must never default to authoritative status.
- How should corrections and errata be represented within the same release?
- What source locations can be retained as provenance without leaking protected
  URLs, credentials, or local operator paths?

## Decisions to revisit before commercialisation

- file snapshots versus PostgreSQL/object storage and migration tooling;
- Python plugin execution versus a language-neutral, sandboxed extension model;
- canonical-schema governance and compatibility guarantees;
- tenant, identity, key-management, audit, and data-residency architecture;
- supply-chain controls, plugin signing, and generator reproducibility attestations;
- the allowed wording and review workflow for alignment and assurance claims;
- API/SDK language targets and the support/version matrix; and
- product/module naming and any trademark implications.

