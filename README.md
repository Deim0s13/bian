# BIAN Adoption & Engineering Platform

This repository is currently a **product and conceptual-architecture
workspace**. The product baseline is established and will continue to evolve.
The current work defines the architecture vision and conceptual views before any
implementation or solution technology is selected.

No software is being built in this phase.

An earlier technical experiment is retained under
[`archive/initial-technical-spike/`](archive/initial-technical-spike/README.md).
It is historical reference only, does not represent approved architecture, and
should not constrain the product vision.

## Working foundations

- [Repository instructions](AGENTS.md) define the rules applied by Codex and
  contributors.
- [Project status](governance/PROJECT_STATUS.md) records the current stage and
  next gate.
- [Architecture Register](governance/ARCHITECTURE_REGISTER.md) is the canonical
  record of decisions, questions, risks, assumptions, dependencies, evidence
  gaps, requirements, work items, and issues.
- [Project principles](product/PROJECT_PRINCIPLES.md) is the authoritative
  numbered catalogue of overarching project principles.
- [Requirements and traceability](architecture/REQUIREMENTS_AND_TRACEABILITY.md)
  defines the requirements-management model while the Architecture Register
  retains authoritative requirement records and status.
- [Architecture repository](architecture/README.md) contains the active
  Architecture Vision, Business Architecture, Information Systems Architecture,
  and conceptual Data Architecture views.
- [Governance and working context](governance/README.md) holds shared audience,
  writing, architecture, quality, and governance context.
- [Contributing](CONTRIBUTING.md) defines the current contribution scope.
- [Security policy](SECURITY.md) states the present security and disclosure
  position.
- `python3 tools/check_project.py` runs the active documentation policy checks.

Repository context is the durable source of truth. Tool memory may assist a
session, but it does not replace checked-in decisions, rules, or status.

## Current objective

Develop and validate a coherent product centred on this question:

> How can a bank use BIAN as a practical, evidence-backed operating model for
> understanding its estate, improving architecture, engineering services,
> governing change, and planning transformation?

The product is a model-driven adoption and engineering platform. Its central
asset is a trusted BIAN Model Registry connecting authoritative BIAN knowledge
to a bank's applications, APIs, data, owners, controls, evidence, plans, and
generated engineering assets.

The registry drives three first-class product pillars:

- Service Generator;
- Adoption & Architecture;
- Assurance & Compliance.

Platform Control provides the governed experience, catalogue, templates,
ownership, lifecycle, scorecards, and documentation across those pillars.
Runtime Targets represent the environments into which platform and generated
capabilities may later be delivered.

The full vision is not yet authorised for implementation. The current
investment position is to continue discovery and conceptual architecture while
testing whether a bounded, connected journey offers decision value beyond a
collection of existing tools. See the
[value proposition and validation strategy](product/VALUE_AND_VALIDATION.md).

## Discovery pack

Read these in order:

1. [Product vision](product/PRODUCT_VISION.md)
2. [Value proposition and validation strategy](product/VALUE_AND_VALIDATION.md)
3. [Project principles](product/PROJECT_PRINCIPLES.md)
4. [Requirements and traceability](architecture/REQUIREMENTS_AND_TRACEABILITY.md)
5. [BIAN alignment policy](product/BIAN_ALIGNMENT_POLICY.md)
6. [Fictional bank and synthetic validation](product/FICTIONAL_BANK_AND_SYNTHETIC_VALIDATION.md)
7. [Open source and production readiness](product/OPEN_SOURCE_AND_PRODUCTION_READINESS.md)
8. [Personas and outcomes](product/PERSONAS_AND_OUTCOMES.md)
9. [Use-case catalogue](product/USE_CASE_CATALOGUE.md)
10. [End-to-end journeys](product/END_TO_END_JOURNEYS.md)
11. [Outline traceability](product/TRACEABILITY.md)
12. [Scope and prioritisation](product/SCOPE_AND_PRIORITISATION.md)
13. [Discovery questions](product/DISCOVERY_QUESTIONS.md)

## Stage gates

### Stage 1: Product definition (baseline established)

- identify users, buyers, problems, triggers, and desired decisions;
- define the complete use-case set and how the use cases reinforce each other;
- state evidence, confidence, provenance, and safety expectations;
- identify the smallest valuable customer proposition;
- evaluate assumptions through authoritative sources, public evidence, the
  fictional Horizon Synthetic Bank, and later qualified peer review.

### Stage 2: Conceptual architecture (current)

The [Architecture Vision](architecture/ARCHITECTURE_VISION.md) establishes the
direction. The initial
[Business Architecture](architecture/BUSINESS_ARCHITECTURE.md) defines the
value streams, platform capabilities, business services, roles, decision rights,
operating-model hypothesis, and HSB decision scenario. This stage will continue
through the
[Information Systems Architecture](architecture/INFORMATION_SYSTEMS_ARCHITECTURE.md),
beginning with the
[conceptual Data Architecture](architecture/DATA_ARCHITECTURE.md), then logical
Application Architecture, trust boundaries, scenario views, and capability
interactions without prematurely selecting detailed technology.

### Stage 3: Solution architecture and experiments

Begins only when the initial customer proposition and architecture questions
are sufficiently understood. Technology choices and prototypes belong here.

## Status language

All use cases in this repository are currently **product hypotheses**. They are
not implemented capabilities, validated customer demand, BIAN-provided
features, or compliance claims.

The project is intended to be independently open source, BIAN-native, secure by
design, and capable of meeting explicit bank-grade production-readiness gates.
It must not imply official BIAN or Red Hat affiliation, endorsement, or support.
