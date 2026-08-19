# Project status

**Last updated:** 19 August 2026

**Lifecycle state:** Concept

**Current stage:** Information Systems Architecture

## Current focus

The Business Architecture and requirements normalisation is complete under
`DEC-030`. `GAT-001` has passed, `WRK-020` and `WRK-022` are complete, and the
active cross-cutting baseline is `REQ-001` through `REQ-025`. `BAR-002` and
`BAR-006` remain active Business Architecture refinements; the superseded
records retain their history and replacements. The conceptual Data Architecture
baseline has passed `GAT-002` under
`DEC-028`, with six Proposed requirements and source-qualified BIAN, export and
workload evidence retained as explicit limitations. The conceptual model has
been instantiated with one synthetic HSB record set, cross-domain gaps and
traceability are explicit, and the stage exit criteria are auditable tests. The
trust-boundary and security
baseline has been accepted under `DEC-026`, and `WRK-011` and `WRK-041` are
complete. It now constrains the connected HSB scenario and logical Application
Architecture while unresolved privacy, application-allocation and
implementation-evidence matters remain explicit. Build-authorisation
recalibration is complete under `DEC-027` and `WRK-042`: the existing gates
remain unchanged and no early experimental-build route has been created. The
immediate work item is the connected HSB scenario under `WRK-012`. `WRK-029`
continues the project-owner review of the wider lifecycle plan without blocking
this Phase C refinement.

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
  measures and a bounded HSB decision scenario. `DEC-030` retains `BAR-002` and
  `BAR-006`, promotes `BAR-010` into `REQ-021` and supersedes the remaining
  eleven `BAR` records with traceable parent requirements.
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
  `DEC-028` accepts nineteen, retains six as Proposed and confirms `DAR-021`,
  `DAR-022` and `DAR-025` as Deferred. `WRK-010` and `WRK-019` are complete,
  `DEP-003` is met and `GAT-002` has passed with explicit limitations.
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
- `DEC-022` reopened the accepted `REQ` and `BAR` baselines for controlled
  review. `DEC-030` records every disposition, accepts the normalised
  `REQ-001` through `REQ-025` baseline, closes `WRK-020` and `WRK-022` and
  returns `GAT-001` to Passed without erasing superseded history.
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
- Twenty-five accepted cross-cutting requirements provide the initial bridge from
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

`GAT-002` passed under `DEC-028`. Nineteen `DAR` records are Accepted, six remain
Proposed for later Application Architecture or scenario evidence and three
remain Deferred. `EVD-011` and `EVD-013` remain explicit limitations; the
synthetic worked example does not establish source-qualified BIAN fidelity or
prove the export obligation.

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

The trust baseline review is complete under `DEC-026` and `WRK-041`.
Build-authorisation recalibration is also complete under `DEC-027` and
`WRK-042`, with no separate early experimental-build route. The immediate work
sequence is to complete the connected HSB scenario and then develop the logical
Application Architecture.

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
