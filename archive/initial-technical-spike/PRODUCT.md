# Product

## Thesis

The BIAN Adoption & Engineering Platform treats BIAN releases as versioned
model/compiler inputs, not merely as collections of OpenAPI files. A canonical
BIAN Model Registry records what was imported, where it came from, how items
relate, and which release they belong to. APIs are one projection of that
model; architecture, adoption, governance, security, and assurance views can
become other projections without redefining the source of truth.

The product's promise is traceability: every conclusion and generated asset
must be explainable from imported sources, customer-owned mappings, or an
explicit extension. It must never present invented semantics as BIAN content.

## Phase 1 scope

Build a trustworthy model engine that can:

- ingest a small representative input through a replaceable source adapter;
- normalise it into an extensible canonical graph;
- retain release and source provenance on every artefact and relationship;
- distinguish Service Domains with published API specifications from those
  without them;
- validate identity, references, provenance, and API-operation consistency;
- emit deterministic canonical JSON and a useful catalogue summary; and
- separate generated output from developer-owned code.

The checked-in input is synthetic. It proves the pipeline without implying a
right to copy, modify, or redistribute BIAN material.

## Non-goals for Phase 1

- generating all R14 services or production-ready banking implementations;
- claiming conformity, certification, regulatory compliance, or security from
  generated code;
- inventing API operations for Service Domains without published operations;
- building a graphical portal or coupling the core to Backstage/RHDH;
- multi-tenant workflow, approvals, identity, or enterprise deployment;
- automated mapping of a bank's applications and APIs; and
- an R14-to-R15 comparison before a licensed, authoritative R15 source exists.

## Product modules over time

1. **Model Registry / Core Engine** — canonical, versioned source of truth.
2. **BIAN Engineer** — API/event/service projections, SDKs, tests, golden paths.
3. **BIAN Architect** — landscape mappings, scenarios, and target states.
4. **BIAN Align** — evidence-backed mapping of existing assets to BIAN.
5. **BIAN Govern** — ownership, lifecycle, duplication, policy, and scorecards.
6. **BIAN Assure** — profiles, controls, evidence, and scoped attestations.
7. **BIAN Transform** — sequenced modernisation roadmaps.

Delivery is phased: prove provenance and regeneration first; add a real licensed
R14 adapter next; then introduce richer projections and version diffs. Customer
mapping and assurance follow only after the underlying evidence model is sound.

