# Architecture lifecycle and ADM tailoring

## Document status

**Status:** Proposed lifecycle baseline for project-owner review

**Scope:** Tailored progression from the current Information Systems
Architecture through Technology Architecture, Opportunities and Solutions,
Migration Planning, Implementation Governance, Architecture Change Management,
and later architecture iterations

**Governing decision:** `DEC-023`

**Excluded:** Completion of any future ADM phase, build authorisation, solution
technology selection, implementation planning at false precision, and any claim
of TOGAF conformance or endorsement

## 1. Purpose

This document makes the complete architecture lifecycle visible before the
project advances beyond Information Systems Architecture. It prevents later
TOGAF phases from becoming an improvised hand-off after the architecture has
already been designed.

The project uses the TOGAF Standard as a method and viewpoint discipline. It
does not reproduce a protected TOGAF template. The phase outcomes below are
original project tailoring for the BIAN Adoption & Engineering Platform.

## 2. Method position

The project will use the full ADM lifecycle as a connected and iterative method:

```text
Architecture Vision
        -> Business Architecture
        -> Information Systems Architecture
             -> Data Architecture
             -> Application Architecture
        -> Technology Architecture
        -> Opportunities and Solutions
        -> Migration Planning
        -> Implementation Governance
        -> Architecture Change Management
        -> targeted revision or a further ADM cycle

Architecture Requirements Management and GAT-011 operate throughout.
```

Iteration is expected within a phase, between adjacent phases, and across later
cycles. Iteration does not permit an unresolved gate to disappear or an earlier
decision to be overwritten without history.

## 3. Tailored lifecycle map

| ADM position | Project outcome | Canonical control | Current position |
|---|---|---|---|
| Preliminary and method preparation | Repository instructions, principles, role model, governance, register, tailoring and evidence boundaries | `GAT-011` | Established and continuously governed |
| Phase A: Architecture Vision | Product direction, stakeholders, concerns, scope, value hypothesis and investment boundary | Accepted working Architecture Vision; `DEC-011` through `DEC-013` | Working baseline |
| Phase B: Business Architecture | Value streams, capabilities, business services, roles, information needs, decision rights and bounded proposition | `GAT-001` | Passed after requirement normalisation under `DEC-030` |
| Phase C: Data Architecture | Identity, assertions, relationships, provenance, authority, time, quality, lifecycle and exchange | `GAT-002` | Passed with explicit limitations under `DEC-028` |
| Phase C: Application Architecture | Logical application responsibilities, interactions, ownership and integration seams | Contributes to `GAT-003` | Not started; `WRK-013` planned |
| Phase D: Technology Architecture | Baseline and target technology capabilities, logical technology building blocks, standards constraints, quality attributes, trust and operational boundaries, and gaps | `GAT-012` | Not started |
| Phase E: Opportunities and Solutions | Candidate transition architectures, delivery approaches and work packages that address architecture gaps | `GAT-013` | Not started |
| Phase F: Migration Planning | Prioritised roadmap, transition states, dependencies, resources, value, risk, readiness and governance sequence | `GAT-014` | Not started |
| Phase G: Implementation Governance | Conformance, evidence, exception, risk, decision and release-governance model for authorised implementation | `GAT-015`, then continuous governance | Not started |
| Phase H: Architecture Change Management | Change monitoring, impact classification, architecture maintenance and initiation of further ADM work | `GAT-016`, then continuous operation | Not started |
| Requirements Management | Requirement capture, ownership, status, traceability, change impact and evidence across every phase | Architecture Register and `GAT-011` | Continuous |

Solution Architecture is a project delivery activity rather than a separate ADM
phase. It applies the approved enterprise and platform architecture to one
bounded, authorised solution scope under `GAT-007`. It must not replace Phase D
or be used to select technology before the target Technology Architecture and
delivery direction are coherent.

## 4. Current completion plan

The project remains in Information Systems Architecture. The following work is
required before Phase D begins:

The record-level model pressure test and initial Phase C gap and cross-domain
traceability analysis are complete under `WRK-035` and `WRK-036`. `GAT-002` has
passed under `DEC-028` with its validation limits explicit; this is not evidence
that `GAT-003` has passed. The trust-boundary and security baseline has also
been accepted under `DEC-026`; `WRK-011` and `WRK-041` are complete.
Build-authorisation review is complete under `DEC-027` and `WRK-042`, with no
separate early experimental-build route.

1. Exercise the information and trust boundaries through the connected HSB
   scenario under `WRK-012`.
2. Develop the logical Application Architecture under `WRK-013`.
3. Review the complete Information Systems Architecture against every auditable
   `GAT-003` stage test, including explicit non-decisions.

Work may iterate across these activities. Phase D starts only after `GAT-003`
and the bounded capability proposition gate `GAT-005` pass, and any carried
uncertainty has an owner, later gate and bounded consequence.

## 5. Phase D: Technology Architecture plan

### Intended decision

Determine which technology capabilities, logical building blocks, standards
constraints and operational qualities are needed to realise the target Business
and Information Systems Architectures without prematurely selecting a deployable
solution.

### Minimum concerns

- baseline technology assumptions and external platform dependencies;
- target technology capabilities and logical technology services;
- identity, trust, isolation, data protection and policy-enforcement boundaries;
- interoperability, portability, integration and restricted-network needs;
- availability, resilience, recovery, observability, performance, capacity and
  sustainability quality attributes;
- software supply-chain, delivery, configuration and operational-control needs;
- cloud-neutral core boundaries and evidence for any platform-specific
  capability;
- technology standards, lifecycle, compatibility and obsolescence constraints;
- baseline-to-target gaps, risks, dependencies and unresolved options; and
- implications for open-source maintainability and bank-supported operation.

### Expected project artefacts

- Technology Architecture scope and stakeholder concerns;
- baseline and target technology capability views;
- logical technology building-block and interaction views;
- technology principles, standards criteria and quality-attribute scenarios;
- trust, deployment-context and operational-responsibility views;
- gap, option, risk and dependency analysis; and
- proposed Technology Architecture requirements with acceptance evidence.

Phase D will not assume microservices, Kubernetes, OpenShift, a cloud provider,
a database, a language or a deployment topology. Each becomes an option only
when a named requirement and evidence justify it.

## 6. Phase E: Opportunities and Solutions plan

### Intended decision

Determine which combinations of reuse, integration, acquisition, contribution,
bounded experimentation and later implementation can address the approved
architecture gaps with acceptable value and risk.

### Minimum concerns

- consolidated gaps from Business, Data, Application and Technology
  Architecture;
- candidate transition architectures and useful intermediate states;
- work packages that produce independently valuable outcomes;
- build, integrate, reuse, contribute, acquire and stop options;
- dependencies on BIAN sources, rights, external systems, reviewers and adopter
  participation;
- capability and organisational readiness;
- evidence-generating experiments for unresolved uncertainty;
- expected value, cost range, risk, reversibility and stop conditions; and
- effects on the open-source product and an adopting bank's local extensions.

The output is a set of candidate delivery paths and an outline implementation
and migration strategy. It is not build authorisation and must include a
credible no-build or narrower-scope option.

## 7. Phase F: Migration Planning plan

### Intended decision

Determine the justified sequence of transition states and work packages, and
whether the evidence supports investment in the first bounded delivery scope.

### Minimum concerns

- prioritisation by decision value, dependency, risk reduction and learning;
- transition-state coherence and temporary architecture debt;
- resource, competency, funding and maintainer-capacity ranges;
- source-rights, security, operational and independent-review prerequisites;
- benefits, costs, risks and evidence expressed without false precision;
- architecture, product, delivery and adopter ownership;
- release, rollback, support and decommissioning implications;
- implementation-governance readiness; and
- explicit stop, defer, resequence and revisit conditions.

The Phase F outcome supports `GAT-006` build authorisation. Detailed delivery
commitments are created only after the project owner accepts a bounded scope.

## 8. Phase G: Implementation Governance plan

### Intended decision

Determine whether an authorised implementation remains aligned with its
approved architecture, requirements and risk position, and whether deviations
are accepted, corrected, deferred or escalated.

### Minimum controls

- traceability from requirement and decision to implementation and evidence;
- architecture review points proportional to risk and reversibility;
- automated and human verification responsibilities;
- deviation, exception, waiver, expiry and remediation records;
- generated-versus-owned asset boundaries;
- security, privacy, supply-chain, resilience and operability evidence;
- release-scope and support-state decisions;
- risk acceptance by the correct accountable role; and
- feedback from implementation into requirements and architecture.

Implementation Governance must enable delivery rather than become an approval
bottleneck. Routine decisions stay with delegated engineering roles when they
remain within approved boundaries. Material deviations return to the affected
architecture gate.

## 9. Phase H: Architecture Change Management plan

### Intended decision

Determine whether observed change can be handled within the current architecture
baseline, requires targeted architecture revision, or justifies a further ADM
cycle.

### Change signals

- a new or changed BIAN release, artefact, relationship or source-rights term;
- new product evidence, user behaviour, adoption friction or failed value
  hypothesis;
- security vulnerability, incident, threat or control failure;
- regulatory, legal, privacy or information-governance change;
- technology lifecycle, compatibility, cost, sustainability or support change;
- operational performance, capacity, resilience or recovery evidence;
- architectural exception accumulation or repeated implementation deviation;
- open-source maintainer, contributor or dependency change; and
- a new adopter scope or materially different stakeholder concern.

### Change classification

| Classification | Response |
|---|---|
| Correction | Amend an error without changing approved meaning; retain provenance and review affected records under `GAT-011`. |
| Bounded evolution | Revisit the affected requirement, decision and architecture gate while retaining the wider baseline. |
| New architecture increment | Initiate the required ADM phases for a new capability, adopter context or material target-state change. |
| New full cycle | Return to Architecture Vision when product purpose, stakeholder outcomes, scope or investment basis has materially changed. |
| Urgent protective change | Apply an authorised time-bounded control for immediate harm, then complete retrospective architecture and risk review. |

The Architecture Register remains the control plane for triggers, decisions,
requirements, risks, evidence, work and impact. Phase H does not create a second
change register.

## 10. Iteration and improvement model

Each completed cycle must leave the architecture easier to evaluate and change.
At minimum it records:

```text
observed signal or evidence
        -> affected concern and requirement
        -> impact on architecture and decisions
        -> chosen change classification
        -> work, exception or new ADM scope
        -> verification and outcome evidence
        -> updated baseline and remaining uncertainty
```

The project will not repeat every phase mechanically. The affected scope,
stakeholders, risks and evidence determine which phases are revisited. A new
BIAN release may principally revisit Data, Application, Technology, transition
and change views; a failed value hypothesis may require a return to Architecture
Vision and Business Architecture.

## 11. Tailoring guardrails

- Produce an artefact only when it supports a named decision, gate or evidence
  need.
- Do not mistake document completion for architecture acceptance or product
  value.
- Do not create detailed cost, schedule or resource estimates before their
  inputs are credible.
- Do not imply independent governance when the project owner performs several
  roles.
- Do not copy TOGAF templates or protected text into the open-source project.
- Do not treat HSB evidence as adopter, market, regulatory or production
  evidence.
- Do not allow a later phase to weaken BIAN integrity, source provenance,
  security, customer ownership or evidence requirements established earlier.
- Preserve declined, rejected and superseded options so later iterations can
  explain why the architecture changed.

## 12. Authoritative method references

The project's produced, consolidated, deferred and omitted work products are
recorded in the [ADM tailoring statement](ADM_TAILORING.md).

- [The TOGAF Standard, 10th Edition](https://www.opengroup.org/togaf), The Open
  Group, accessed 18 August 2026.
- [TOGAF Enterprise Architecture Practitioner competency-to-role mapping](https://help.opengroup.org/hc/en-us/articles/32127544219026-Competency-to-Role-Mapping-TOGAF-Enterprise-Architecture-Practitioner),
  The Open Group, updated 27 December 2025 and accessed 18 August 2026.

These references support the method and phase distinction. The project-specific
outcomes, gates and artefacts in this document remain project-authored
tailoring.
