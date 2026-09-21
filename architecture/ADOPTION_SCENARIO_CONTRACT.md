# Adoption scenario contract

## Document status

**Status:** Revised conceptual contract under `DEC-031`, `DEC-032`, `DEC-033`
and `DEC-034`

**Architecture stage:** Information Systems Architecture

**Scope:** Reusable structure and validation rules for bounded HSB adoption
scenarios

**First reference use case:** HSB fragmented-payments modernisation assessment

**Subordinate validation thread:** HSB customer-payment initiation
responsibility allocation

**Excluded:** Exact BIAN source selection, complete scenario evidence, logical
Application Architecture, technology selection, implementation and universal
support claims

## 1. Purpose

This contract prevents the first HSB payments scenario from becoming the
implicit domain model, workflow or application structure of the BIAN Adoption
& Engineering Platform.

It defines the project-authored adoption kernel that every bounded scenario
must exercise, the information that may vary by scenario and the evidence
needed to test domain transferability. It is an architecture validation
contract, not a deployable component, physical schema, user-interface flow or
BIAN-defined construct.

The contract supports `REQ-026`, mitigates `RSK-042`, governs the scope of
`WRK-012` and supplies the domain-transferability evidence required by
`GAT-003`.

## 2. Claim boundary

One deep scenario cannot demonstrate support for every possible BIAN adoption
journey. The current claim is narrower:

> The shared architecture is intended to support bounded BIAN adoption
> scenarios without embedding the banking domain, source shape, adoption
> decision or reference instance into shared platform semantics.

Evidence for that claim requires both:

1. one deep payments reference scenario that exercises the connected adoption
   path; and
2. one materially different, non-payment and non-API-dominant transferability
   probe that reuses the same adoption kernel without changing shared semantic
   meaning or logical responsibilities.

Further representative scenarios must expand the validated envelope over time.
The project must always report which scenario structures have and have not been
exercised.

## 3. Separation model

### 3.1 Canonical adoption kernel

<!-- domain-neutral:start adoption-kernel -->

**Kernel version:** `ADOPTION-KERNEL/v1`

This subsection is the sole canonical definition of the adoption kernel. The
version covers the behaviour catalogue, stage catalogue and their mapping. Any
semantic change to a behaviour, stage or mapping requires a recorded
architecture decision, an impact review and a new kernel version. Editorial
changes that do not alter meaning retain the version and record an empty
semantic diff.

#### Behaviour catalogue

| ID | Stable logical behaviour |
|---|---|
| `KB-01` | Qualify, capture, quarantine and validate source context |
| `KB-02` | Register identity, preserve assertions and reconcile without destructive merge |
| `KB-03` | Propose and analyse attributable relationships and mappings |
| `KB-04` | Evaluate purpose-bounded views, evidence, uncertainty, conflict and findings |
| `KB-05` | Control participant access, review, delegated decision authority and recorded outcomes |
| `KB-06` | Record current, target and transition options, selection rationale and owned actions |
| `KB-07` | Produce, verify, exchange and reconcile participating projections, exports and external outcomes |
| `KB-08` | Analyse governed change, identify maintained dependants and route impact review |
| `KB-09` | Retain provenance, audit, limitation, failure and recovery evidence across every participating stage |

#### Stage-to-behaviour mapping

| ID | Kernel stage | Required behaviours |
|---|---|---|
| `AK-01` | Bounded adoption question, trigger, decision authority and intended outcome | `KB-05`, `KB-09` |
| `AK-02` | Source-qualified BIAN context or explicit unresolved scope | `KB-01`, `KB-09` |
| `AK-03` | Customer or HSB estate assertions and source-system boundaries | `KB-01`, `KB-02`, `KB-09` |
| `AK-04` | Proposed relationships and mappings | `KB-02`, `KB-03`, `KB-09` |
| `AK-05` | Evidence, uncertainty and conflict | `KB-03`, `KB-04`, `KB-09` |
| `AK-06` | Accountable review and decision | `KB-04`, `KB-05`, `KB-09` |
| `AK-07` | Current-state finding | `KB-04`, `KB-09` |
| `AK-08` | Target, transition and justified no-change options | `KB-04`, `KB-06`, `KB-09` |
| `AK-09` | Selected decision, rationale and owned actions | `KB-05`, `KB-06`, `KB-09` |
| `AK-10` | Participating projection, assurance, governance or external outcome | `KB-07`, `KB-09` |
| `AK-11` | Source, estate, policy or evidence change and downstream impact | `KB-08`, `KB-09` |

A scenario may declare a stage non-participating or unsupported when the
decision does not require it, subject to the transferability floor in section
7. The architecture must not manufacture records or semantics merely to make
every stage appear populated.

<!-- domain-neutral:end adoption-kernel -->

### 3.2 Scenario instance

A scenario instance supplies the bounded, versioned records that vary:

- banking question, trigger and intended decision;
- organising decision-subject shape or an explicit statement that the decision
  requires no separate subject record;
- authorised BIAN release, artefacts and source-supported relationships;
- customer or HSB applications, APIs, events, integrations, data assets,
  products, vendors and other estate context;
- participants, ownership, delegated decision rights and escalation paths;
- candidate mappings, evidence, conflicts, uncertainty and review outcomes;
- current, target and transition options;
- security, assurance, policy and operating context;
- scenario-specific View Definitions, mapping methods, quality or confidence
  dimensions, thresholds and evaluation parameters;
- measures, expected outcomes, negative cases and stop conditions; and
- controlled changes and expected impact.

These records use their correct authority classes and namespaces. Scenario
meaning must not be promoted into the shared kernel because it occurs in the
first reference instance.

The View Definition, quality conclusion, confidence expression, mapping method
and profile concepts are shared model concepts. Each concrete definition,
dimension, method, threshold or profile is scenario-scoped by default.
Promotion into a reusable shared library is a kernel change governed by the
version and decision rule in section 3.1 and invariant 10. Reuse by two
scenarios does not create promotion by implication.

### 3.3 Projections and external systems

Reports, exports, engineering artefacts, catalogue records and evidence
packages are governed projections or exchanges from the connected records.
They do not become authoritative BIAN or customer assertions. A scenario
records which projections participate and why; it does not require every
platform pillar to produce an output.

## 4. Mandatory scenario contract

Each scenario instance shall record:

| Contract field | Required content |
|---|---|
| Identity | Stable scenario identifier, version, owner, status and change history |
| Kernel baseline | Exact adoption-kernel version, participating and non-participating stage IDs, and semantic diff outcome |
| Purpose | Primary user, trigger, decision, intended outcome and existing alternative |
| Decision subject | Scenario-specific subject shape around which the decision is organised, or an explicit no-subject state; a reference instance must not make its subject shape mandatory for another scenario |
| Scope | Included and excluded banking context, organisation, estate, source and time boundaries |
| BIAN context | Exact authorised source and release, or an explicit project placeholder and blocked BIAN attribution |
| Source shape | Participating BIAN artefact types and an explicit API-publication state rather than an assumption that an API specification exists |
| Customer context | Customer or HSB assertions, source systems, owners, quality, sensitivity and limitations |
| Decision rights | Proposer, source steward, reviewer, accountable decision authority, objector and escalation route |
| Maintained scope | Included records and relationships, exclusions, owner, effective period and change-review trigger |
| Options | Current state, at least two target or transition options where a selection is required, and a justified no-change option |
| Expected outcome | Decision, accepted and rejected alternatives, rationale, actions, owners, uncertainty and unresolved matters |
| Trust paths | Runtime, participant and lifecycle boundaries crossed, including expected non-success outcomes |
| Measures | Named decisions supported, method, baseline, limitations and stop or narrow conditions |
| Change | Controlled source, estate, policy or evidence change and the expected impact-review set |
| View provenance | View Definition, exact input records and versions, evaluation context, transformation version, result identity and limitations |
| Export boundary | Customer-owned decision package, simulated rights restrictions and excluded content |
| Claim boundary | What the scenario can establish and what remains unverified |

Missing information must use an explicit absence, unsupported or unresolved
state. It must not be omitted or replaced with invented BIAN meaning.

## 5. Domain-neutrality invariants

The following invariants apply to the shared architecture:

1. Shared subjects, assertions, relationships, provenance, review, evidence,
   view and impact concepts do not contain payment-specific semantics.
2. Logical responsibilities are derived only from `KB-01` through `KB-09` in
   the canonical kernel and are not named for a banking product or Service
   Domain.
3. A new scenario may add source-qualified BIAN or customer meaning through
   governed records without changing existing shared meaning.
4. A scenario-specific workflow variation is expressed through governed state,
   policy, configuration or extension rather than a new core truth class.
5. Mapping cardinality is not fixed. Unmapped, one-to-one, one-to-many,
   many-to-one, disputed, rejected and superseded outcomes remain representable.
6. The architecture does not assume that every Service Domain has published
   Service Operations or an API specification.
7. The absence of an API, event, control, projection or other stage is visible
   and does not cause the platform to invent one.
8. Source identity, authority, provenance, ownership, sensitivity, review and
   limitations survive every participating view and output.
9. Specific View Definitions, mapping methods, quality or confidence
   dimensions, thresholds and profiles remain scenario-scoped unless a
   recorded kernel change explicitly promotes them into a shared library.
10. A transferability probe may expose a missing shared concept, but a core
    change requires a recorded architecture decision, semantic diff, impact
    review and new kernel version rather than being disguised as scenario
    configuration.
11. Domain-specific controls or profiles attach without redefining BIAN content
    or contaminating the shared information model.

Canonical shared semantic and behaviour catalogues use the repository's
`domain-neutral` markers. The automated vocabulary check applies inside those
blocks. Scenario descriptions and explicit risk statements remain outside the
blocks so legitimate banking language does not weaken or disable the control.

## 6. First deep reference use case

| Field | HSB payments reference position |
|---|---|
| Use-case ID | `HSB-UC-001` |
| Working title | Modernise a fragmented payments estate using BIAN |
| Purpose | Test whether an enterprise or payments domain architect can reconstruct a credible legacy estate, use source-qualified BIAN context to identify gaps, duplication and boundary concerns, and make defensible target and transition decisions without a preselected outcome |
| Domain standing | HSB scenario data only; payments is not the platform domain model |
| BIAN standing | Exact R14 elements and relationships remain unresolved until authorised source qualification; project placeholders cannot be described as BIAN mappings |
| Depth | Multiple payment journeys, mixed-generation estate, conflicting sources, BIAN mapping, diagnosis, neutral options, target and transition decisions, participating downstream outcomes, controlled change, negative paths and export |
| Intended evidence | Internal architectural coherence, reproducibility, authority separation, transfer-ready responsibilities and explicit failure or stop signals |
| Prohibited inference | Universal BIAN support, customer demand, real-bank feasibility, regulatory acceptance, implementation security or production readiness |

The [bank-led payments-modernisation use case](HSB_USE_CASE_001_PAYMENTS_MODERNISATION.md)
defines the customer problem, estate and adoption assessment. The
[responsibility-allocation validation thread](HSB_SCENARIO_001_PAYMENTS_RESPONSIBILITY.md)
preserves `HSB-SCN-001/v0.2` as one unexecuted experiment within that use case
and records its subordinate disposition in `v0.3`. This contract constrains
both without duplicating their estate records, views or decision evidence.

## 7. Transferability probe

The transferability probe is a bounded architecture test, not a second complete
product proposition. Its exact BIAN scope shall be selected only after source
qualification or represented by clearly labelled project placeholders.

Under `DEC-035`,
[HSB-TP-001](HSB_TRANSFERABILITY_PROBE_001_CUSTOMER_ONBOARDING.md) uses customer
onboarding and periodic review as the first compact probe. Its estate-only paper
execution records an empty semantic diff against `ADOPTION-KERNEL/v1`. That is
information-semantics evidence only until `WRK-013` demonstrates that the same
logical application responsibilities support both the payments reference and
the probe.

The probe shall be:

- outside payments;
- not primarily driven by an API specification;
- based on a different primary adoption decision or trigger;
- free to declare its own organising decision-subject shape or an explicit
  no-subject state rather than inherit the payments responsibility subject;
- able to exercise a different combination of source types, participants,
  mapping shapes and outputs; and
- small enough to test architecture reuse without creating another full HSB
  estate.

The probe shall exercise at least nine of the eleven kernel stages. `AK-01`
through `AK-07`, `AK-09` and `AK-11` are mandatory. `AK-08` and `AK-10` may be
non-participating only when the scenario contract records why the decision does
not require options or a downstream outcome and which behaviour remains
unexercised.

The probe passes only when:

- it identifies `ADOPTION-KERNEL/v1` as its baseline and records an empty
  semantic diff for the canonical block in section 3.1;
- the same information semantics and truth classes remain sufficient;
- the same logical responsibilities can perform every behaviour required by
  its participating stage mappings;
- scenario variation is carried by governed records, policy, profiles or
  extensions;
- an absent API specification and every unsupported stage remain explicit;
- the probe produces a reconstructable decision view; and
- any unexercised structure remains a declared limitation.

A failure is valuable evidence. It must result in an architecture finding,
requirement impact and explicit decision to revise and re-version the shared
model, narrow the supported envelope or reject an unjustified scenario demand.
The work item may close after that outcome is dispositioned, but `GAT-003`
cannot rely on the failed kernel version as transferability evidence.

## 8. Structural variation matrix

The payments scenario and transferability probe together shall differ on at
least six of these eight dimensions. API dependence, primary decision, mapping
shape and source mix are mandatory differences.

| Dimension | Payments reference | Transferability expectation |
|---|---|---|
| Banking context | Fragmented domestic payments modernisation | Non-payment context |
| Primary decision | Current-state diagnosis, target choices and transition, including a subordinate responsibility-allocation decision | Different adoption decision or trigger |
| API dependence | APIs participate in the estate | API specification is absent or non-dominant |
| Mapping shape | Conflicting and mixed-responsibility mappings | A different cardinality or unmapped outcome |
| Source mix | Synthetic application, API, integration and governance sources | Different source combination |
| Participants | Enterprise or payments architect plus asset and control owners | Different primary or supporting roles |
| Downstream path | Selected engineering, assurance and governance consequences | Different participating projection or an explicit non-participating stage |
| Change | HSB estate or source-context change | Different change type, such as policy, evidence or source release |

The matrix is evidence planning, not permission to invent BIAN structures or
claim exhaustive combinatorial coverage.

`HSB-TP-001/v0.1` differs on all eight dimensions. Its exact comparison and
limitations are maintained in the probe rather than duplicated here.

## 9. `WRK-012` acceptance tests

`WRK-012` is complete only when:

1. `HSB-UC-001` supplies a coherent bank problem, estate, evidence boundary,
   neutral option space and expected adoption outcomes, while its executable
   validation threads satisfy every mandatory contract field.
2. The same governed records connect its business, information, trust, review,
   projection and impact views.
3. Its decision view is reconstructable from the exact View Definition, inputs,
   versions and evaluation context.
4. Its scenario-specific concepts remain outside shared platform semantics and
   logical responsibility names.
5. Every negative trust scenario has an expected non-success result and
   evidence record.
6. A controlled change identifies every maintained dependant and preserves the
   earlier decision view.
7. The HSB export package reconstructs the customer-owned decision and history
   without undocumented platform state or simulated rights leakage.
8. The transferability probe is executed against a named kernel version and
   either records an empty semantic diff or produces a recorded architecture
   finding, requirement impact and decision to re-version the kernel, narrow
   the supported envelope or reject an unjustified scenario demand.
9. Every participating and non-participating stage is explicit.
10. Measures and conclusions state their synthetic scope, method, limitations
    and stop or narrow result.
11. A source-blocked estate assessment is named and bounded separately from any
    BIAN-informed assessment, and no BIAN alignment or adoption conclusion is
    permitted until the exact source context passes `GAT-004`.

Passing these tests establishes conceptual evidence only. It does not satisfy
later implementation, security, operational, open-source publication or
production-supported release gates.

## 10. Application Architecture hand-off

The scenario and transferability probe shall map `KB-01` through `KB-09` from
the canonical kernel to logical application responsibilities. Each mapping
shall identify the participating stages, required interactions, governed
records and explicit non-participating behaviour. This section does not define
a second behaviour list.

`WRK-013` will allocate these behaviours to logical application
responsibilities. It must not name components from the HSB payments estate or
select deployable services, products, protocols or technologies.

## 11. Explicit non-decisions

This contract does not decide:

- which exact BIAN R14 artefacts form either scenario;
- how scenario contracts, configuration or View Definitions are serialised;
- which user experience implements the workflow;
- the number or deployment boundary of future applications or services;
- storage, query, integration or policy technology;
- the complete HSB estate or long-term scenario catalogue; or
- that the architecture supports every possible adopter or BIAN use without
  further evidence.

## References

- [Business Architecture](BUSINESS_ARCHITECTURE.md)
- [Information Systems Architecture](INFORMATION_SYSTEMS_ARCHITECTURE.md)
- [Conceptual Data Architecture](DATA_ARCHITECTURE.md)
- [Phase C model validation](PHASE_C_MODEL_VALIDATION.md)
- [Trust-boundary and security architecture](TRUST_BOUNDARY_AND_SECURITY_ARCHITECTURE.md)
- [Requirements and traceability](REQUIREMENTS_AND_TRACEABILITY.md)
- [Architecture Register](../governance/ARCHITECTURE_REGISTER.md)
- [Fictional bank and synthetic validation policy](../product/FICTIONAL_BANK_AND_SYNTHETIC_VALIDATION.md)
