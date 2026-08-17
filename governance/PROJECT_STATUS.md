# Project status

**Last updated:** 17 August 2026

**Lifecycle state:** Concept

**Current stage:** Conceptual architecture

## Current focus

Review the initial Business Architecture and use it to refine the primary user,
decision, value streams, platform capabilities, business services, roles,
decision rights, operating model, measures, and bounded HSB scenario. Continue
testing alternatives, value hypotheses, and stop conditions before any build is
authorised.

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
- The initial Business Architecture defines six connected value streams, seven
  project-defined platform capabilities, business services, decision rights,
  candidate requirements, measures, and a bounded HSB decision scenario.
- The Architecture Register is the single canonical record for decisions,
  active questions, risks, assumptions, dependencies, evidence gaps,
  architecture requirements, work items, and issues. Context documents use its
  stable identifiers rather than maintaining parallel registers.
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

- the Architecture Vision is reviewed and accepted;
- the Business Architecture is reviewed and its leading user, decision, value
  stream, capability, operating-model, and measure hypotheses are accepted or
  explicitly carried as open questions;
- architecture requirements and stakeholder concerns are traceable;
- conceptual capability, information, context, trust, scenario, and operating
  model views are coherent;
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
