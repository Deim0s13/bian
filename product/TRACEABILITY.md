# Product vision traceability

This document ensures the BIAN Adoption & Engineering Platform remains aligned
to its north-star structure as product discovery and architecture evolve.

The platform is defined affirmatively from BIAN Sources, the BIAN Model
Registry, three product pillars, Platform Control, and Runtime Targets.

## North-star structure

| Platform structure | Product definition | Primary location |
|---|---|---|
| BIAN Sources | Authoritative, rights-reviewed BIAN artefacts and relationships for declared releases | `BIAN_ALIGNMENT_POLICY.md` |
| BIAN Model Registry | Canonical BIAN model, relationships, releases, customer extensions and mappings, regulatory mappings, provenance, review, and evidence | `PRODUCT_VISION.md`, FDN-01 in `USE_CASE_CATALOGUE.md` |
| Service Generator | REST and asynchronous API artefacts, models, SDKs, tests, infrastructure definitions, policies, documentation, and safe regeneration | UC-01, UC-02, UC-03 |
| Adoption & Architecture | Application and API mapping, capability views, Business Scenario overlays, current and target states, vendor analysis, modernisation, and roadmaps | UC-07 through UC-12 |
| Assurance & Compliance | Security profiles, policies, requirements, controls, implementations, tests, evidence, attestations, exceptions, and scorecards | UC-04, UC-05, UC-14 |
| Platform Control | Catalogue, templates, ownership, lifecycle, architecture governance, scorecards, documentation, policy, and workflow | UC-06, UC-13 and cross-cutting support |
| Runtime Targets | Local or Docker, OpenShift or Kubernetes, AWS, Azure, and customer-controlled delivery contexts where later approved | Architecture and production-readiness work |

## Fourteen-use-case coverage

| Use case | North-star placement |
|---|---|
| UC-01: model-driven engineering artefact generation | Service Generator |
| UC-02: safe regeneration with owned implementation preserved | Service Generator |
| UC-03: BIAN release impact and upgrade management | Service Generator with cross-pillar impact |
| UC-04: consistent security profiles | Assurance & Compliance with generated and runtime enforcement |
| UC-05: evidence-based scoped control assurance | Assurance & Compliance |
| UC-06: developer and architect self-service | Platform Control |
| UC-07: customer landscape mapping | Adoption & Architecture |
| UC-08: existing API alignment analysis | Adoption & Architecture |
| UC-09: current, transition, and target-state design | Adoption & Architecture |
| UC-10: Business Scenario overlays | Adoption & Architecture |
| UC-11: evidence-backed modernisation advice | Adoption & Architecture |
| UC-12: vendor and product capability mapping | Adoption & Architecture |
| UC-13: BIAN-informed architecture governance | Platform Control with all-pillar evidence |
| UC-14: multidimensional adoption reporting | Assurance & Compliance with Platform Control presentation |

## Cross-cutting relationships

- The authoritative project principles are `PRN-001` through `PRN-017` in
  [PROJECT_PRINCIPLES.md](PROJECT_PRINCIPLES.md). Architecture and product work
  references those identifiers rather than restating the principles.
- The cross-cutting requirements are `REQ-001` through `REQ-020` in the
  [Architecture Register](../governance/ARCHITECTURE_REGISTER.md#requirements).
  Their derivation and use are explained in the
  [requirements and traceability view](../architecture/REQUIREMENTS_AND_TRACEABILITY.md).
- The first working proposition is the bounded responsibility-allocation
  decision accepted under `DEC-018` and described in the
  [Business Architecture](../architecture/BUSINESS_ARCHITECTURE.md#13-accepted-working-proposition-and-decision-boundary).
- The full platform structure is a north-star, not build authorisation. Each
  proposed increment must pass the applicable tests and preserve the stop
  conditions in
  [VALUE_AND_VALIDATION.md](VALUE_AND_VALIDATION.md).
- The BIAN Model Registry is the shared foundation and source of truth.
- Service Generator outputs retain model, release, profile, and generation
  lineage.
- Generated and owned implementation boundaries govern UC-01 and UC-02.
- BIAN release change can affect generation, mappings, controls, evidence,
  scorecards, and runtime consumers.
- Security profiles connect Assurance & Compliance to generated assets,
  Platform Control policy, and Runtime Targets.
- Platform Control provides the governed experience without replacing the BIAN
  Model Registry.
- HSB scenarios should cross pillars instead of validating each as an isolated
  tool.

## Traceability rule for future changes

If a platform block or use case is merged, removed, or materially reinterpreted,
record:

- the project decision and supporting evidence;
- the affected principles and overarching requirements;
- the impact on the value hypothesis, alternatives, validation tests, and stop
  conditions;
- what customer problem and north-star responsibility remain covered;
- which platform block and use case now own it;
- the impact on shared model, control, runtime, and evidence relationships; and
- what is explicitly no longer in product scope.
