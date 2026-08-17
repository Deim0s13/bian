# Project principles

## Status and authority

This is the authoritative catalogue of overarching principles for the BIAN
Adoption & Engineering Platform. The catalogue is proposed for project-owner
review. It consolidates existing non-negotiable product constraints, accepted
decisions, and architecture direction without authorising implementation.

These are project-defined principles. They are not presented as BIAN, TOGAF,
CNCF, regulatory, Red Hat, or bank principles. Detailed policies and
architecture guidance interpret this catalogue for their own concerns but must
not create competing overarching principles.

Each identifier is stable. A principle may be clarified through review, but it
must not be silently redefined or reused. A material change requires a decision
in the
[Architecture Register](../governance/ARCHITECTURE_REGISTER.md#decisions).

## PRN-001: Lead with a bounded user outcome

**Statement:** Every product increment and material architecture investment
must address a named user, trigger, decision or task, intended outcome, existing
alternative, required information, evidence of value, and stop or narrow
condition.

**Rationale:** A broad platform can accumulate features without solving a
problem well enough to justify adoption.

**Implications:**

- The full north-star platform is not build authorisation.
- Capabilities are evaluated through connected journeys, not isolated feature
  demonstrations.
- Work that cannot explain its user and decision value is deferred or stopped.

## PRN-002: Attribute BIAN content only to authoritative sources

**Statement:** Anything represented as BIAN must preserve the exact authorised
source, release, identity, terminology, relationship, lifecycle state, meaning,
rights position, and material source limitations.

**Rationale:** Trust in the platform depends on distinguishing BIAN-defined
content from project interpretation and customer context.

**Implications:**

- The project never invents, silently changes, or fills gaps in BIAN semantics.
- A Service Domain without published BIAN Service Operations is not represented
  as having a BIAN-defined API.
- Source rights and integrity are reviewed before import, transformation, or
  redistribution.
- Claims are release-qualified and do not imply BIAN affiliation or endorsement.

## PRN-003: Keep classes of truth visibly separate

**Statement:** Authoritative BIAN assertions, mechanical projections, project
extensions, bank or HSB assertions, inferences, recommendations, third-party
assertions, and verified evidence must remain distinguishable throughout their
lifecycle.

**Rationale:** Combining different authorities into one undifferentiated model
creates misleading conclusions and unsafe decisions.

**Implications:**

- Each assertion records its authority, provenance, owner, version, review
  state, confidence or limitations where applicable.
- Automated findings never become authoritative BIAN or bank facts by
  implication.
- Storage, APIs, exports, user experiences, and reports preserve the distinction.

## PRN-004: Treat the connected model as the foundation

**Statement:** The BIAN Model Registry and its connected information model are
the foundation from which APIs, events, engineering assets, architecture views,
mappings, governance results, and assurance evidence are projected.

**Rationale:** Treating BIAN as a collection of OpenAPI files would constrain
the adoption, architecture, change, and assurance outcomes that define the
product.

**Implications:**

- The canonical model is not a copy of one source format or one BIAN artefact.
- APIs and generated services are projections rather than the product centre.
- Relationships, authority, provenance, version, history, ownership, and review
  are first-class model concerns.

## PRN-005: Preserve accountable human decision rights

**Statement:** Material mappings, architecture decisions, exceptions,
recommendations, control conclusions, and risk acceptances require an explicit
accountable human or authorised governance body.

**Rationale:** Automation can accelerate analysis, but cannot assume a bank's
accountability or decision authority.

**Implications:**

- Recommendations expose evidence, method, uncertainty, conflicts, and review
  state.
- Approval, rejection, dispute, supersession, and exception history are retained.
- AI and rules support decisions without concealing who remains accountable.

## PRN-006: Make claims only from scoped evidence

**Statement:** BIAN alignment, security, compliance, control effectiveness,
cloud-native qualities, and production readiness may be claimed only for the
scope, version, method, evidence, responsible reviewer, limitations, and period
actually assessed.

**Rationale:** Broad claims derived from narrow tests create false assurance and
unacceptable risk.

**Implications:**

- Regulation maps to requirements, controls, implementations, tests, evidence,
  findings, gaps, exceptions, and scoped attestations.
- Failed, expired, partial, and unverified areas remain explicit.
- Passing automated checks is evidence for those checks, not proof of general
  compliance or fitness.

## PRN-007: Build security, privacy, and resilience into the architecture

**Statement:** Security, privacy, identity, tenancy, least privilege, supply-chain
integrity, failure handling, recovery, and operational resilience are design
inputs from the first increment.

**Rationale:** A product intended for regulated banks cannot add trust and
operability after its core boundaries and information flows are fixed.

**Implications:**

- Trust boundaries, threats, abuse cases, sensitive flows, failure modes, and
  recovery responsibilities are explicit before affected implementation.
- Secure defaults and data minimisation apply even when HSB uses synthetic data.
- Delivery scope is reduced rather than bypassing a required security or
  resilience control.

## PRN-008: Validate repeatably with a fictional bank

**Statement:** Horizon Synthetic Bank and synthetic information provide the
repeatable internal environment for scenario, functional, security,
operational, and outcome validation.

**Rationale:** The project will not depend on participating banks or customer
data for development and validation.

**Implications:**

- HSB data is versioned, reproducible, explicitly synthetic, imperfect, and
  capable of exercising conflict and change.
- Synthetic evidence cannot establish customer demand, real-bank adoption,
  regulatory acceptance, procurement fit, or realised benefit.
- Unvalidated external outcomes remain labelled as evidence gaps.

## PRN-009: Operate as a sustainable open-source project

**Statement:** Open source includes transparent governance, clear contribution
rights, secure maintenance, reproducible releases, source and dependency rights,
support boundaries, and honest lifecycle status.

**Rationale:** Publishing source code without a sustainable trust and operating
model is insufficient for enterprise adoption.

**Implications:**

- Public release depends on reviewed licensing, contribution, security,
  maintenance, disclosure, release, and support processes.
- The project does not imply Red Hat, BIAN, community, or maintainer support
  beyond published evidence.
- Maintainer capacity constrains supported scope.

## PRN-010: Design for credible bank adoption and operation

**Statement:** Architecture must consider the controls, integration,
operability, deployment, upgrade, recovery, support, accessibility, and evidence
needs of a regulated bank from the outset.

**Rationale:** A demonstration that cannot be governed or operated safely does
not provide a credible adoption path.

**Implications:**

- Production supported is an evidenced lifecycle state, not an aspiration.
- Self-managed and restricted-network contexts remain valid architecture
  considerations until product requirements narrow them.
- Installation, migration, backup, restore, upgrade, rollback, observability,
  audit, incident response, and exit require explicit ownership and evidence.

## PRN-011: Preserve customer control and portability

**Statement:** Banks retain authority over their assertions, mappings,
decisions, configuration, evidence, and owned implementation, with governed
export and exit paths.

**Rationale:** Adoption should not require surrendering accountability or
creating avoidable dependency on this platform.

**Implications:**

- Customer-owned information remains identifiable and exportable with
  provenance and history.
- The architecture identifies systems of record, reconciliation, retention,
  deletion, and conflict responsibilities.
- Project workflows do not silently become the authority for bank facts.

## PRN-012: Complement established enterprise systems

**Statement:** Integrate with established architecture, API, source-control,
delivery, identity, security, GRC, CMDB, developer-platform, and runtime systems
through governed interfaces unless evidence justifies owning a capability.

**Rationale:** Recreating mature products would increase scope and reduce
enterprise fit without improving the platform's connected differentiation.

**Implications:**

- Build-versus-integrate decisions identify the system of record and lifecycle
  owner.
- Adapters isolate external products and source formats from the core model.
- Red Hat Developer Hub or another experience layer may be a front door but
  does not dictate the core architecture.

## PRN-013: Preserve a runtime-neutral core while applying cloud-native qualities

**Statement:** The core model and domain behaviour remain independent of a
particular cloud, container platform, portal, or deployment topology while the
architecture pursues secure, resilient, manageable, observable, sustainable,
and repeatable operation.

**Rationale:** Banks have varied runtime, sovereignty, isolation, and support
constraints, and cloud-native outcomes do not require one topology.

**Implications:**

- Kubernetes, OpenShift, public cloud, microservices, and containers require an
  evidenced fit rather than becoming universal mandates.
- Platform-specific capabilities attach through adapters, profiles, packaging,
  or deployment projections.
- Portability does not mean every environment is supported without qualification.

## PRN-014: Make change deterministic, versioned, and impact-aware

**Statement:** Imported sources, mappings, decisions, transformations,
projections, profiles, generated assets, and evidence must be versioned so that
material outputs can be reproduced and change impacts explained.

**Rationale:** BIAN releases, bank estates, controls, and engineering assets all
evolve; untracked change would invalidate trust and safe regeneration.

**Implications:**

- Deterministic operations record source and tool versions, configuration, and
  relevant digests.
- Superseded information and decisions remain traceable.
- Change analysis identifies affected relationships, owners, assets, controls,
  evidence, and actions within the maintained scope.

## PRN-015: Protect developer-owned content from generation

**Statement:** Generated artefacts are disposable projections. Developer-owned
business logic, adapters, decisions, configuration, and extensions remain
outside generated boundaries and survive regeneration.

**Rationale:** Safe model evolution is impossible if generation overwrites
owned behaviour or creates ambiguous responsibility.

**Implications:**

- Generated and owned boundaries are explicit in architecture, packaging, and
  tests.
- Regeneration is repeatable and never relies on manual edits to generated
  content.
- Compatibility and migration consequences are reported before replacement.

## PRN-016: Prefer the simplest credible architecture

**Statement:** Add components, services, dependencies, abstractions, extension
points, and technology only for named requirements, risks, or independently
valuable operating boundaries.

**Rationale:** Premature breadth and distribution increase security,
operational, maintenance, and contributor costs.

**Implications:**

- A modular deployment is acceptable when it preserves boundaries more safely
  than distributed services.
- Experiments are time-bound and state the decision they inform.
- Obsolete paths and duplicated sources of truth are removed when safe.

## PRN-017: Maintain architecture traceability and explicit gates

**Statement:** Stakeholder concerns, principles, requirements, decisions,
architecture views, work items, risks, tests, and evidence must form a navigable
thread throughout the project lifecycle.

**Rationale:** Traceability makes change reviewable, prevents architecture from
becoming disconnected documentation, and supports defensible decisions.

**Implications:**

- TOGAF guides method and viewpoint discipline while BIAN supplies authorised
  banking reference content.
- A stage progresses only when its stated gate is satisfied or an explicit
  decision records the remaining uncertainty.
- Context documents reference the Architecture Register rather than creating
  competing lifecycle records.

## Governing decision rule

When schedule or breadth conflicts with value, provenance, source rights,
security, privacy, resilience, maintainability, customer control, or truthful
claims, reduce or defer scope. Do not weaken the principle or conceal the
limitation.

## Supporting policies and guidance

- [BIAN alignment policy](BIAN_ALIGNMENT_POLICY.md)
- [Fictional bank and synthetic validation policy](FICTIONAL_BANK_AND_SYNTHETIC_VALIDATION.md)
- [Open-source governance and production-readiness policy](OPEN_SOURCE_AND_PRODUCTION_READINESS.md)
- [Value proposition and validation strategy](VALUE_AND_VALIDATION.md)
- [Architecture and engineering application guidance](../governance/ARCHITECTURE_AND_ENGINEERING_PRINCIPLES.md)
- [Quality and review model](../governance/QUALITY_AND_REVIEW.md)
