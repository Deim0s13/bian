# Project status

**Last updated:** 19 August 2026

**Lifecycle state:** Concept

**Current stage:** Information Systems Architecture

## Current focus

The required Business Architecture baseline was accepted as sufficient to begin
Information Systems Architecture under `DEC-019`. Whole-register review has
since placed `GAT-001` in `Revisit required` while the Business Architecture
requirements receive a controlled disposition review. This does not reverse the
stage decision, but it prevents the earlier baseline from being treated as
settled. The immediate architecture focus remains `GAT-002`, the conceptual Data
Architecture baseline. The Phase C pressure test now precedes logical
Application Architecture: the conceptual model has been instantiated with one
synthetic HSB record set, cross-domain gaps and traceability are explicit, and
the stage exit criteria are auditable tests. The initial trust-boundary and
security baseline is now drafted under `WRK-011`; `WRK-041` must review its
boundaries, threats, negative paths, failure behaviour and Application
Architecture hand-off. The first review has added an explicit participant
access boundary, separated runtime from extension and release lifecycle
boundaries, made Unclassified information visible, added participant privacy,
and prioritised workstation, source-control, dependency and intake-exhaustion
threats. Build-authorisation recalibration then follows under
`WRK-042`, before it becomes an implementation constraint. `WRK-029` continues the
project-owner review of the wider lifecycle plan without blocking this Phase C
refinement.

No software implementation or solution architecture is approved. The archived
technical spike is inactive and does not constrain current work.

## Established foundations

- The product is the BIAN Adoption & Engineering Platform. Its north-star
  structure is BIAN Sources to BIAN Model Registry to Service Generator,
  Adoption & Architecture, and Assurance & Compliance, supported by Platform
  Control and Runtime Targets.
- Fourteen customer-facing use cases and a shared trusted model foundation are
  preserved in the product definition.
- The product definition is accepted as an evolving baseline. Unresolved buyer,
  demand, source-rights, and operating-model assumptions remain visible.
- The current investment position is to continue discovery and conceptual
  architecture, not to authorise a full platform build. Connected decision value
  must be demonstrated before implementation scope is approved.
- The Architecture Vision covers the full platform. A bounded HSB payments
  assessment is an initial validation scenario rather than the product centre.
- The accepted Business Architecture defines six connected value streams, seven
  project-defined platform capabilities, business services, decision rights,
  measures, accepted `BAR-001` through `BAR-014`, and a bounded HSB decision
  scenario.
- `DEC-019` establishes Information Systems Architecture as the current stage
  and sequences conceptual Data Architecture before logical Application
  Architecture without selecting physical storage, products, protocols,
  deployment topology, or implementation frameworks.
- The initial conceptual Data Architecture separates subjects from assertions,
  treats relationships as attributable and versioned assertions, and makes
  authority, provenance, temporal context, quality, conflict, review, evidence,
  protection, portability and downstream impact explicit. Following the first
  pressure test under `DEC-020`, its `DAR-001` through `DAR-028` requirements
  have single accountable owners, canonical gates and related blocker records.
  `DAR-021`, `DAR-022` and `DAR-025` are deferred; the remainder await explicit
  review outcomes under `WRK-019`.
- `DEC-024` resolves five conceptual-model ambiguities through a record-level
  HSB example: subjects are identity anchors, relationship assertions are binary
  and reified, projections remain separate from assertions, Class C is project
  context, and current views use governed View Definitions. `EVD-011` keeps the
  source-qualified BIAN, real-bank and workload evidence gaps explicit.
- The Phase C gap and traceability analysis connects twelve baseline-to-target
  gaps to platform capabilities, value streams, role authority and later Phase
  E work. It moves `EVD-007` to `Partial`, not `Closed`, because comparison with
  an actual combination of existing tools remains absent.
- `DEC-021` establishes one canonical gate vocabulary and one canonical role
  vocabulary. It reserves authority language for information semantics and
  recorded adopting-organisation decision rights. The register now records
  origin, risk likelihood and impact, event-based review triggers, and the
  limitations of the current single-person role holders.
- `DEC-022` reopens the accepted `REQ` and `BAR` baselines for controlled review.
  Every requirement is now assigned to a canonical gate and linked to related
  register records. `WRK-020` and `WRK-022` will determine whether individual
  requirements are retained, revised, rejected or superseded without erasing
  their accepted history.
- `DEC-023` plans the complete tailored architecture lifecycle before the
  project advances beyond Information Systems Architecture. Phase D has its own
  Technology Architecture baseline under `GAT-012`; Phases E through H use
  `GAT-013` through `GAT-016`. Requirements Management and `GAT-011` remain
  continuous, and Architecture Change Management can trigger targeted revision
  or a further ADM cycle without silently replacing earlier baselines.
- `DEC-025` answers `OQ-022` with an explicit ADM tailoring statement covering
  produced, consolidated, deferred and omitted project work products. The
  project does not claim TOGAF conformance or invent an Architecture Board.
- The initial trust-boundary and security architecture separates semantic
  authority from operational trust, identifies protected information and the
  runtime, participant and lifecycle trust boundaries, and defines threats,
  failure behaviour, control outcomes and synthetic negative scenarios without
  selecting security products or a deployment topology. `EVD-012` keeps the
  absence of implementation and operational security evidence explicit.
- Solution Architecture remains a bounded project delivery activity under
  `GAT-007`. It does not replace Technology Architecture or authorise
  implementation, which remains behind `GAT-008` and the Implementation
  Governance readiness controls in `GAT-015`.
- The first working proposition helps an enterprise or payments domain architect
  decide the target allocation and transition of one contested banking
  responsibility. HSB customer-payment initiation is the initial synthetic
  scope, subject to exact BIAN R14 source qualification.
- Existing enterprise systems remain authoritative for their source records.
  The platform is authoritative only for its governed mappings, review,
  traceability, connected decisions, workflow, and audit records.
- The Architecture Register is the single canonical record for decisions,
  active questions, risks, assumptions, dependencies, evidence gaps,
  architecture requirements, work items, and issues. Context documents use its
  stable identifiers rather than maintaining parallel registers.
- Seventeen accepted overarching project principles provide one numbered
  catalogue for value, BIAN integrity, authority, evidence, security, synthetic
  validation, open source, bank adoption, interoperability, portability,
  generation, change, simplicity, and architecture governance.
- Twenty accepted cross-cutting requirements provide the initial bridge from
  product outcomes and principles to Business, Data, Application, Technology,
  security, operational, and future solution requirements.
- Horizon Synthetic Bank will provide repeatable fictional scenarios and
  synthetic information.
- The project is intended to be independently open source.
- BIAN-attributed content must be authoritative, release-qualified, and fully
  traceable. Project and inferred content must remain separate.
- Production readiness will be demonstrated through scoped evidence gates.
- TOGAF guides the current and future architecture method and viewpoints,
  subject to appropriate tailoring and rights review.
- The current CNCF definition and relevant authoritative CNCF guidance will
  guide future engineering through traceable requirements and evidence.
  Microservices and Kubernetes are not assumed solutions.
- Active documentation follows repository-wide writing and quality checks.
- No independent proposition, BIAN, architecture, security or assurance review
  has yet occurred. `RSK-025`, `DEP-008`, `EVD-008` and `WRK-024` make this a
  declared limitation rather than an implied confidence claim.

## Evidence position

The current use cases are product hypotheses. Synthetic scenarios can establish
internal coherence and future technical behaviour, but cannot validate customer
demand, bank adoption, regulatory acceptance, or realised benefits.

The strongest current value hypothesis is the traceable connection from an
authoritative BIAN concept through bank-estate mapping, architecture decision,
engineering asset, assurance evidence, ownership, and change impact. The
individual platform capabilities are not assumed to be differentiated.

## Next gates

`GAT-002` is the immediate gate. It requires explicit outcomes for all proposed
`DAR` records, resolution or deliberate carry-forward of their blocker records,
and a conceptual model whose BIAN validation limits remain explicit. The worked
example is internal evidence of coherence only; it does not close `EVD-011`.

`GAT-003` is the Information Systems Architecture baseline gate. It is ready to
pass only when every test in the Information Systems Architecture has its named
evidence and a recorded pass from the accountable judge. In practical terms:

- the overarching project principles have been reviewed and accepted or revised;
- the cross-cutting requirements baseline has been reviewed, its records have
  explicit outcomes, and its traceability model is accepted;
- the Architecture Vision is reviewed and accepted;
- the Business Architecture is reviewed and its leading user, decision, value
  stream, capability, operating-model, and measure hypotheses are accepted or
  explicitly carried as open questions;
- architecture requirements and stakeholder concerns are traceable;
- conceptual capability, Data Architecture, Application Architecture, context,
  trust, scenario, and operating-model views are coherent;
- the trust and sensitive-information view is completed before the connected
  HSB scenario is used as stage evidence;
- Application Architecture resolves or deliberately carries forward the
  responsibilities listed in `DEP-013`, `DEP-014` and `WRK-040`;
- the first HSB scenario has defined inputs, expected decisions, and evidence;
- the first proposition has passed the applicable decision-value,
  connected-differentiation, input-feasibility, trust, adoption-fit, and
  sustainable-scope tests;
- external desirability remains explicitly unvalidated or has credible evidence;
- applicable stop and narrow conditions have been reviewed;
- material source-rights, security, privacy, tenancy, and governance questions
  affecting solution architecture are understood;
- the architecture identifies which uncertainties require bounded experiments;
- the owner explicitly authorises Technology Architecture to begin.

The immediate work sequence is to review the trust baseline under `WRK-041`,
recalibrate bounded build authorisation under `WRK-042`, then continue with the
connected HSB scenario and logical Application Architecture. Recalibration does
not authorise implementation during the current stage.

After `GAT-003`, the planned architecture sequence is:

1. `GAT-005`: bounded capability proposition approval;
2. `GAT-012`: Technology Architecture baseline;
3. `GAT-013`: Opportunities and Solutions baseline;
4. `GAT-014`: Migration Planning approval;
5. `GAT-006`: bounded build authorisation;
6. `GAT-007`: bounded Solution Architecture approval;
7. `GAT-015` and `GAT-008`: Implementation Governance and implementation
   readiness;
8. `GAT-016`: Architecture Change Management readiness, then continuous
   operation and later ADM re-entry; and
9. `GAT-009` or `GAT-010`: the applicable release-readiness gate.

This sequence is iterative. Gate identifiers are stable record identifiers, not
ordinal phase numbers.

## How to update this check-in

Update this file when the stage, current focus, evidence position, or next gate
changes. Put decisions, questions, risks, assumptions, dependencies, evidence
gaps, architecture requirements, work items, and issues in
`ARCHITECTURE_REGISTER.md` rather than turning this into a historical diary.
