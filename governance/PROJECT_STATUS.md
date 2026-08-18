# Project status

**Last updated:** 17 August 2026

**Lifecycle state:** Concept

**Current stage:** Information Systems Architecture

## Current focus

The required Business Architecture baseline is accepted as sufficient to begin
Information Systems Architecture under `DEC-019`. The current focus is review
of the initial Information Systems Architecture scope and conceptual Data
Architecture, including identity, assertions, relationships, provenance, time,
authority, quality, systems of record, reconciliation, information lifecycle,
and exchange. Logical Application Architecture follows this information
baseline. Remaining Business Architecture refinements and open evidence
questions continue through the Architecture Register rather than blocking all
progress.

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
  protection, and portability explicit. Its `DAR-001` through `DAR-017`
  requirements remain proposed pending review.
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

## Evidence position

The current use cases are product hypotheses. Synthetic scenarios can establish
internal coherence and future technical behaviour, but cannot validate customer
demand, bank adoption, regulatory acceptance, or realised benefits.

The strongest current value hypothesis is the traceable connection from an
authoritative BIAN concept through bank-estate mapping, architecture decision,
engineering asset, assurance evidence, ownership, and change impact. The
individual platform capabilities are not assumed to be differentiated.

## Next gate

Stage 2 is ready to close only when:

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
- the first HSB scenario has defined inputs, expected decisions, and evidence;
- the first proposition has passed the applicable decision-value,
  connected-differentiation, input-feasibility, trust, adoption-fit, and
  sustainable-scope tests;
- external desirability remains explicitly unvalidated or has credible evidence;
- applicable stop and narrow conditions have been reviewed;
- material source-rights, security, privacy, tenancy, and governance questions
  affecting solution architecture are understood;
- the architecture identifies which uncertainties require bounded experiments;
- the owner explicitly authorises solution architecture to begin.

## How to update this check-in

Update this file when the stage, current focus, evidence position, or next gate
changes. Put decisions, questions, risks, assumptions, dependencies, evidence
gaps, architecture requirements, work items, and issues in
`ARCHITECTURE_REGISTER.md` rather than turning this into a historical diary.
