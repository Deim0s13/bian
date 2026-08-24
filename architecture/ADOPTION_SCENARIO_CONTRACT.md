# Adoption scenario contract

## Document status

**Status:** Initial conceptual contract under `DEC-031`

**Architecture stage:** Information Systems Architecture

**Scope:** Reusable structure and validation rules for bounded HSB adoption
scenarios

**First reference instance:** HSB customer-payment initiation responsibility
allocation

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

### 3.1 Shared adoption kernel

The adoption kernel consists of project-defined concepts that remain stable
when the banking domain or decision changes:

```text
Bounded adoption question
        -> source-qualified BIAN context or explicit unresolved scope
        -> customer or HSB estate assertions
        -> proposed relationships and mappings
        -> evidence, uncertainty and conflict
        -> accountable review and decision
        -> current-state finding
        -> target and transition options
        -> selected decision and owned actions
        -> participating projection, assurance or governance outcome
        -> source or estate change and downstream impact
```

The sequence describes a connected decision thread. A scenario may declare a
stage non-participating or unsupported when the decision does not require it.
The architecture must not manufacture records or semantics merely to make every
stage appear populated.

### 3.2 Scenario instance

A scenario instance supplies the bounded, versioned records that vary:

- banking question, trigger and intended decision;
- authorised BIAN release, artefacts and source-supported relationships;
- customer or HSB applications, APIs, events, integrations, data assets,
  products, vendors and other estate context;
- participants, ownership, delegated decision rights and escalation paths;
- candidate mappings, evidence, conflicts, uncertainty and review outcomes;
- current, target and transition options;
- security, assurance, policy and operating context;
- measures, expected outcomes, negative cases and stop conditions; and
- controlled changes and expected impact.

These records use their correct authority classes and namespaces. Scenario
meaning must not be promoted into the shared kernel because it occurs in the
first reference instance.

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
| Purpose | Primary user, trigger, decision, intended outcome and existing alternative |
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
2. Logical responsibilities are named for stable behaviour such as capture,
   validation, relationship proposal, review, projection, controlled exchange
   and impact analysis, not for a banking product or Service Domain.
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
9. Domain-specific controls or profiles attach without redefining BIAN content
   or contaminating the shared information model.
10. A transferability probe may expose a missing shared concept, but a core
    change requires a recorded architecture decision and impact review rather
    than being disguised as scenario configuration.

## 6. First deep reference instance

| Field | HSB payments reference position |
|---|---|
| Scenario ID | `HSB-SCN-001` |
| Working title | Allocate a bounded customer-payment initiation responsibility |
| Purpose | Test whether an enterprise or payments domain architect can make and defend a target allocation and transition decision across a fragmented synthetic estate |
| Domain standing | HSB scenario data only; payments is not the platform domain model |
| BIAN standing | Exact R14 elements and relationships remain unresolved until authorised source qualification; project placeholders cannot be described as BIAN mappings |
| Depth | Full connected path, including conflict, review, options, decision, participating downstream outcomes, controlled change, negative paths and export |
| Intended evidence | Internal architectural coherence, reproducibility, authority separation, transfer-ready responsibilities and explicit failure or stop signals |
| Prohibited inference | Universal BIAN support, customer demand, real-bank feasibility, regulatory acceptance, implementation security or production readiness |

The detailed payments scenario will be developed separately under `WRK-012`.
This contract constrains it but does not duplicate its estate records, views or
decision evidence.

## 7. Transferability probe

The transferability probe is a bounded architecture test, not a second complete
product proposition. Its exact BIAN scope shall be selected only after source
qualification or represented by clearly labelled project placeholders.

The probe shall be:

- outside payments;
- not primarily driven by an API specification;
- based on a different primary adoption decision or trigger;
- able to exercise a different combination of source types, participants,
  mapping shapes and outputs; and
- small enough to test architecture reuse without creating another full HSB
  estate.

The probe passes only when:

- the adoption kernel remains unchanged;
- the same information semantics and truth classes remain sufficient;
- the same logical responsibilities can perform the required behaviours;
- scenario variation is carried by governed records, policy, profiles or
  extensions;
- an absent API specification and every unsupported stage remain explicit;
- the probe produces a reconstructable decision view; and
- any unexercised structure remains a declared limitation.

A failure is valuable evidence. It must result in an architecture finding,
requirement impact and explicit decision to revise the shared model, narrow the
supported envelope or reject an unjustified scenario demand.

## 8. Structural variation matrix

The payments scenario and transferability probe together should vary these
dimensions:

| Dimension | Payments reference | Transferability expectation |
|---|---|---|
| Banking context | Payment-related responsibility allocation | Non-payment context |
| Primary decision | Target allocation and transition | Different adoption decision or trigger |
| API dependence | APIs participate in the estate | API specification is absent or non-dominant |
| Mapping shape | Conflicting and mixed-responsibility mappings | A different cardinality or unmapped outcome |
| Source mix | Synthetic application, API, integration and governance sources | Different source combination |
| Participants | Enterprise or payments architect plus asset and control owners | Different primary or supporting roles |
| Downstream path | Selected engineering, assurance and governance consequences | Different participating projection or an explicit non-participating stage |
| Change | HSB estate or source-context change | Different change type, such as policy, evidence or source release |

The matrix is evidence planning, not permission to invent BIAN structures or
claim exhaustive combinatorial coverage.

## 9. `WRK-012` acceptance tests

`WRK-012` is complete only when:

1. `HSB-SCN-001` satisfies every mandatory contract field.
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
8. The transferability probe passes the tests in section 7 without changing the
   shared adoption kernel.
9. Every participating and non-participating stage is explicit.
10. Measures and conclusions state their synthetic scope, method, limitations
    and stop or narrow result.

Passing these tests establishes conceptual evidence only. It does not satisfy
later implementation, security, operational, open-source publication or
production-supported release gates.

## 10. Application Architecture hand-off

The scenario and transferability probe shall identify the stable logical
behaviours needed for:

- source qualification, capture, quarantine and validation;
- identity registration and non-destructive reconciliation;
- assertion and relationship management;
- analysis and mapping proposals;
- purpose-bounded view evaluation;
- participant access, review and delegated decisions;
- projection, output verification, export and reconciliation;
- impact analysis and review routing; and
- audit, privileged change, failure and recovery evidence.

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
