# Architecture

## System context

The platform sits between authoritative BIAN release artefacts, bank-owned
architecture data, and tools that consume generated engineering or governance
outputs. BIAN inputs remain external intellectual property. The engine imports
only sources the operator is entitled to use, records their identity and
digest, normalises their semantics, and exposes projections through ports.

```text
Official/licensed BIAN sources     Customer extensions and mappings
              |                                  |
       source adapters                      extension adapters
              +---------------+------------------+
                              v
                 parse -> normalise -> validate
                              |
                              v
                  Canonical Model Snapshot
                   (versioned graph + provenance)
                              |
               +--------------+----------------+
               |              |                |
          JSON/CLI API    generators       diff/analysis
                         (projections)       (later)
               |              |                |
          internal tools  service/API/     architecture,
                          catalog output    impact, evidence
```

Backstage/RHDH is a future consumer and workflow surface, not the owner of the
canonical model.

## Major components

- **Source adapters** convert one external representation into a source-neutral
  import document. The first adapter accepts the synthetic JSON fixture.
- **Normaliser** creates stable identifiers, typed artefacts and relationships,
  attaching source provenance during creation rather than afterwards.
- **Validator** rejects missing provenance, duplicate identifiers, dangling
  relationships, and contradictions such as operations without an API spec.
- **Canonical snapshot** is an immutable, release-scoped graph. Its serial form
  is canonical JSON, suitable for hashing, tests, and future storage adapters.
- **Repository port** will store and retrieve snapshots. Phase 1 uses files;
  later adapters may use PostgreSQL/object storage without changing the model.
- **Projection generators** read a validated snapshot and produce disposable
  output. The first projection is a catalogue summary.
- **CLI adapter** is the first application boundary. HTTP, build-system, and
  Backstage adapters can invoke the same application service later.

## Canonical domain model

The model is a small typed graph rather than a copy of OpenAPI.

### ModelSnapshot

- `schemaVersion`: version of this platform's canonical schema.
- `snapshotId`: content-derived identity of the normalised graph.
- `bianRelease`: declared BIAN release or fixture analogue.
- `sourceSet`: one or more imported source records and their SHA-256 digests.
- `artifacts`: stable, sorted artefacts.
- `relationships`: typed, directed, sorted edges.

### Artifact

- `id`: stable namespace-qualified identity.
- `kind`: extensible kind, initially `service-domain`, `api-specification`, and
  `service-operation`.
- `name`, `description`, `lifecycleStatus`.
- `release`: the release in which the artefact is asserted.
- `attributes`: kind-specific structured values that do not redefine identity.
- `provenance`: one or more assertions identifying source, source item, source
  digest, classification, and optional location within that source.

### Relationship

- `id`, `type`, `sourceId`, `targetId`, and optional attributes.
- `release` and `provenance`, with the same traceability rules as artefacts.
- Initial types: `exposes-api`, `contains-operation`, and `relates-to`.

Kinds and relationship types are controlled vocabulary values at validation
boundaries, but the serial model allows later vocabulary versions. OpenAPI
paths, schemas, examples, and extensions belong in an API projection-specific
model or attributes, not at the canonical graph's centre.

## Data and model flow

1. An adapter reads a byte-for-byte source and computes its digest.
2. It validates the source envelope, classification, release, and item IDs.
3. The normaliser creates graph elements and attaches provenance to every one.
4. Validation runs before a snapshot can be persisted or projected.
5. Stable sorting and canonical JSON serialisation produce a content hash.
6. The snapshot ID is derived from that hash, excluding the snapshot ID itself.
7. Generators consume only a validated snapshot and write to a dedicated output
   root. A manifest records source and output digests.

No runtime timestamps, filesystem paths, random IDs, or map insertion order are
allowed to influence deterministic outputs.

## Generation and ownership model

Generated files are disposable build products under `out/` (or another
explicit output directory), carry a generated marker where the format permits,
and are never edited to implement business behaviour. Future service templates
must produce two layers:

- a regenerable contract/scaffold package derived from the canonical snapshot;
- an owned implementation/adapters/configuration package depending on that
  contract through stable interfaces.

Regeneration replaces only the generated layer. Merge-based code generation is
not the default because it obscures ownership and makes upgrades unsafe.

## Versioning strategy

Four versions are independent and explicit:

- **Source release**: for example `R14`; never inferred from a filename.
- **Canonical schema version**: starts at `1.0`; changes follow semantic
  compatibility rules and use migrations when persistence begins.
- **Generator version**: identifies projection behaviour and participates in
  the build manifest.
- **Customer extension version**: later recorded separately so it is never
  confused with a BIAN assertion.

Snapshots are immutable and content-addressed. A future diff engine compares
artefacts and relationships by stable identity, classifies additions/removals/
changes, and traces affected projections and customer mappings. It does not
compare only rendered OpenAPI text.

## Extension points

- source adapters for official repository exports or other licensed packages;
- canonical validators for vocabulary and cross-artefact invariants;
- projection generators discovered through an explicit registry initially and
  Python entry points only when third-party plugins are needed;
- declarative security profiles that map controls to generated policy hooks;
- customer mapping namespaces whose provenance distinguishes asserted,
  inferred, reviewed, and verified mappings; and
- storage and API adapters behind application ports.

Extensions may add assertions, validations, and projections. They may not
silently alter imported BIAN assertions.

## Trust boundaries

- **External source boundary:** inputs are untrusted data. Digests establish
  identity, not authenticity. Authenticity requires a trusted channel/signature.
- **Licensing boundary:** source availability is not redistribution permission.
  Import and generated-output rights must be established before commercial use.
- **Extension boundary:** plugins execute code and therefore require allowlists,
  version pinning, and isolation before third-party loading is enabled.
- **Customer-data boundary:** future architecture mappings may expose sensitive
  topology and ownership information and need tenant isolation and access logs.
- **Generator boundary:** generated code is not trusted as production-ready;
  normal secure SDLC, review, testing, and deployment controls still apply.
- **Assurance boundary:** tests provide evidence for scoped control statements;
  they do not establish broad compliance. Unverified requirements remain
  explicit in any attestation.

## Deployment evolution

Phase 1 is a local library and CLI. A later service can wrap the application
ports with FastAPI and persist metadata in PostgreSQL while keeping large raw
source packages and generated bundles in object storage. This split is a
deployment choice, not a core-domain dependency.

