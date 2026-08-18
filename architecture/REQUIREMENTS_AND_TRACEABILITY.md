# Requirements and traceability

## Document status

**Status:** Accepted working baseline under `DEC-017`

**Scope:** Cross-cutting project and architecture requirements

**Excluded:** Satisfaction evidence, Application Architecture, Technology
Architecture, solution requirements, technology selection, and implementation
specifications. Data Architecture requirements are linked from this view rather
than duplicated here.

## Purpose

This document defines how requirements are derived, classified, reviewed,
traced, and changed across the BIAN Adoption & Engineering Platform. The
[Architecture Register](../governance/ARCHITECTURE_REGISTER.md#requirements) is
the sole authoritative record for requirement wording, ownership, status,
acceptance evidence, and review state.

This document is a requirements-management view. It must not become a competing
requirements catalogue.

## Requirements model

The current baseline uses three requirement levels:

| Identifier | Level | Purpose |
|---|---|---|
| `REQ` | Overarching project and architecture requirement | Governs enduring cross-cutting outcomes and constraints across architecture domains and lifecycle stages |
| `BAR` | Business Architecture requirement | Expresses the business behaviour, governance, value, information, and operating-model needs derived from the Business Architecture |
| `DAR` | Data Architecture requirement | Refines the information meaning, identity, authority, provenance, relationship, lifecycle, quality, exchange, and governance obligations needed by the platform |

Future Application, Technology, security, operational, and solution requirements
will be introduced only when the relevant architecture work needs them. They
must refine or trace to an accepted `REQ`, `BAR`, `DAR`, stakeholder concern, or
approved scope change. They must not silently weaken an overarching requirement.

Requirements Management remains continuous through the tailored lifecycle in
[Architecture lifecycle and ADM tailoring](ARCHITECTURE_LIFECYCLE.md).
Opportunities, work packages, migration priorities, implementation deviations
and change signals must trace back to governed requirements rather than create a
parallel delivery backlog with unrecorded architecture obligations.

Principles guide judgement; requirements state something that must be satisfied
or evaluated. A principle is not treated as implemented merely because a
requirement references it.

Every requirement record also carries one accountable canonical role, one
canonical delivery gate, acceptance evidence, related register records and a
last-reviewed date. These control fields are maintained only in the
Architecture Register.

## Traceability thread

The intended thread is:

```text
Product outcome and stakeholder concern
        -> project principle
        -> overarching requirement
        -> domain or solution requirement
        -> architecture view and decision
        -> work item and implementation
        -> test, operational measure, or review
        -> evidence, finding, exception, and change impact
```

Not every record needs every link. Each material conclusion must retain enough
of the thread to explain why it exists, who owns it, how it will be assessed,
and what is affected when it changes.

## Baseline coverage

The accepted `REQ-001` through `REQ-020` baseline covers:

| Concern | Requirement references |
|---|---|
| Bounded value and investment discipline | `REQ-001` |
| Authoritative BIAN use and authority separation | `REQ-002`, `REQ-003` |
| Canonical model, identity, provenance, and connected traceability | `REQ-004` through `REQ-006` |
| Human decision rights and evidence-based claims | `REQ-007`, `REQ-008` |
| Security, privacy, resilience, and synthetic validation | `REQ-009`, `REQ-010` |
| Open-source trust and bank readiness | `REQ-011`, `REQ-012` |
| Enterprise coexistence, customer control, and runtime neutrality | `REQ-013` through `REQ-015` |
| Extensibility, deterministic generation, and change impact | `REQ-016` through `REQ-018` |
| Consumable experience and proportionate operability | `REQ-019`, `REQ-020` |

This coverage is deliberately architectural. It does not specify a deployment
topology, programming language, database, user-interface framework, cloud,
container platform, service decomposition, or product integration.

## Initial relationship to Business Architecture requirements

The existing Business Architecture requirements refine the cross-cutting
baseline as follows:

The relationships are many-to-many: one `BAR` may refine more than one
overarching requirement. Repeated `BAR` identifiers are therefore intentional,
not duplicate requirement records. Their necessity and wording remain subject
to the controlled disposition review under `DEC-022` and `WRK-022`.

| Overarching requirement | Principal Business Architecture refinements |
|---|---|
| `REQ-001` | `BAR-001`, `BAR-006`, `BAR-010` |
| `REQ-002`, `REQ-003` | `BAR-003`, `BAR-011` |
| `REQ-004` through `REQ-006` | `BAR-002`, `BAR-005`, `BAR-007` |
| `REQ-007` | `BAR-004` |
| `REQ-008` | `BAR-008` |
| `REQ-010` | `BAR-011` |
| `REQ-011`, `REQ-012` | `BAR-012` |
| `REQ-013`, `REQ-014` | `BAR-005`, `BAR-014` |
| `REQ-017` | `BAR-009` |
| `REQ-019` | `BAR-013` |

The absence of a direct `BAR` refinement does not make an overarching
requirement optional. Some concerns will be refined primarily through later
Data, Application, Technology, security, or operational architecture work.

## Initial relationship to Data Architecture requirements

The proposed and deferred `DAR-001` through `DAR-028` requirements are maintained only in the
[Architecture Register](../governance/ARCHITECTURE_REGISTER.md#data-architecture-requirements).
They refine the accepted baseline in these principal groups:

| Data Architecture concern | Principal requirement relationships |
|---|---|
| Identity, namespaces, source identity, and time | `DAR-001`, `DAR-002`, `DAR-006`, `DAR-011`, `DAR-015`, `DAR-028`; refining `REQ-004`, `REQ-005`, `BAR-002`, and `BAR-005` |
| Authority, assertions, relationships, mappings, and review | `DAR-003`, `DAR-007`, `DAR-008`, `DAR-012`, `DAR-018`, `DAR-019`; refining `REQ-002`, `REQ-003`, `REQ-007`, `BAR-003`, `BAR-004`, and `BAR-007` |
| Provenance, immutable capture, evidence, reproducibility, views, and impact | `DAR-004`, `DAR-005`, `DAR-013`, `DAR-017`, `DAR-020`, `DAR-024`, `DAR-026`, `DAR-027`; refining `REQ-006`, `REQ-008`, `REQ-017`, `REQ-018`, and `BAR-008` through `BAR-010` |
| Quality, systems of record, and reconciliation | `DAR-009`, `DAR-010`, `DAR-021`; refining `REQ-003`, `REQ-013`, `BAR-005`, and `BAR-014` |
| Information protection, portability, rights, and lifecycle | `DAR-014`, `DAR-016`, `DAR-022`, `DAR-023`, `DAR-025`; refining `REQ-009`, `REQ-011`, `REQ-012`, `REQ-014`, `REQ-016`, `BAR-011`, and `BAR-012` |

Each `DAR` record identifies a canonical `GAT` delivery event and the register
records that constrain, support or refine it. `DAR-021`, `DAR-022` and
`DAR-025` are explicitly deferred. The remaining records stay proposed until
review. Neither status nor sequencing authorises implementation or proves that
a future product satisfies a requirement.

## Initial relationship to trust and security architecture

The
[Trust-boundary and security architecture](TRUST_BOUNDARY_AND_SECURITY_ARCHITECTURE.md)
does not create a competing security-requirements catalogue. It applies the
accepted requirements to the first proposition through these principal groups:

| Trust and security concern | Principal requirement relationships |
|---|---|
| Source authenticity, operational validation and BIAN authority | `REQ-002`, `REQ-003`, `REQ-005`; `DAR-002` through `DAR-005`, `DAR-023` |
| Ownership, sensitivity, access and tenant scope | `REQ-009`, `REQ-014`; `DAR-014`, `OQ-034` |
| Participant privacy and accountable decision history | `REQ-009`; `DAR-012`, `DAR-022`, `OQ-052`, `RSK-024` |
| Inference, human decision and point-of-use authority | `REQ-007`, `REQ-008`, `REQ-019`; `DAR-008`, `DAR-012`, `DAR-018`, `DAR-019`, `DAR-026` |
| Extension, generation, export and external integration | `REQ-013` through `REQ-017`; `DAR-015` through `DAR-017`, `DAR-027` |
| Intake safety, failure, impact and recovery | `REQ-009`, `REQ-018`, `REQ-020`; `DAR-020`, `DAR-024`, `RSK-041`, `EVD-012` |
| Open-source and production-supported trust | `REQ-011`, `REQ-012`; `RSK-039`, `RSK-040`, `GAT-009`, `GAT-010` |

Logical enforcement and interaction responsibilities remain `OQ-050`,
`DEP-014` and `WRK-013`. No security product or physical control is selected by
this traceability.

## Requirement quality tests

Before acceptance, a requirement should:

- identify a required outcome, constraint, behaviour, or quality rather than a
  preferred technology;
- have an accountable owner and traceable source or rationale;
- name the canonical `GAT` event by which it must be satisfied;
- be sufficiently bounded to assess without claiming universal coverage;
- define credible acceptance evidence or an explicit evidence gap;
- avoid combining unrelated obligations that need different owners or gates;
- avoid discretionary qualifiers unless their scope rule and decision authority
  are explicit;
- preserve BIAN, project, bank, inference, and evidence authority boundaries;
- identify dependencies, risks, conflicts, evidence gaps, blockers and
  exceptions through related register records;
- be understandable to the stakeholders responsible for approving or meeting it;
- remain compatible with the governing principles or record an explicit
  decision where a conflict exists; and
- be testable, reviewable, measurable, or otherwise verifiable at the stage
  where it is required.

## Lifecycle and change control

Requirement status is governed by the Architecture Register vocabulary:
`Proposed`, `Accepted`, `Deferred`, `Rejected`, or `Superseded`.

- Proposed requirements do not authorise implementation.
- Acceptance confirms that the requirement belongs in the governed baseline;
  it does not prove that the product already satisfies it.
- A deferred requirement retains its rationale and required gate.
- A rejected requirement retains the decision and evidence that rejected it.
- A superseded requirement remains traceable to its replacement.
- Exceptions identify the owner, scope, rationale, risk, compensating control,
  approval, expiry, and removal condition.
- Material requirement changes trigger review of related principles, decisions,
  architecture views, risks, work items, tests, evidence, and downstream assets.

## Review outcome

The project owner accepted `PRN-001` through `PRN-017` and `REQ-001` through
`REQ-020` as evolving working baselines under `DEC-017`. Acceptance confirms
that they govern subsequent architecture work. It does not prove that the
future product satisfies them or authorise implementation.

`DEC-022` has reopened the accepted `REQ` and `BAR` baselines for controlled
normalisation. `WRK-020` and `WRK-022` will test bundled obligations, weak or
duplicate refinements, qualifiers, ownership, gates and blocker links. Existing
statuses remain authoritative until the project owner records explicit retained,
revised, rejected or superseded outcomes. This prevents a review comment from
silently rewriting an accepted baseline.

Material changes must retain their previous outcome, record the supporting
decision and evidence, and review affected Business, Data, Application,
Technology, security, operational, and solution requirements.
