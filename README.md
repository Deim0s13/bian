# BIAN Adoption & Transformation Platform

This repository is currently a **product-discovery workspace**. It defines the
full customer proposition before any implementation or technical architecture
is selected.

No software is being built in this phase.

An earlier technical experiment is retained under
[`archive/initial-technical-spike/`](archive/initial-technical-spike/README.md).
It is historical reference only, does not represent approved architecture, and
should not constrain the product vision.

## Current objective

Develop and validate a coherent product centred on this question:

> How can a bank use BIAN as a practical, evidence-backed operating model for
> understanding its estate, improving architecture, engineering services,
> governing change, and planning transformation?

The product is not simply a BIAN API generator. Its central asset is a trusted
model connecting BIAN knowledge to a bank's actual applications, APIs, data,
owners, controls, evidence, plans, and generated engineering assets.

## Discovery pack

Read these in order:

1. [Product vision](product/PRODUCT_VISION.md)
2. [Project principles](product/PROJECT_PRINCIPLES.md)
3. [BIAN alignment policy](product/BIAN_ALIGNMENT_POLICY.md)
4. [Fictional bank and synthetic validation](product/FICTIONAL_BANK_AND_SYNTHETIC_VALIDATION.md)
5. [Open source and production readiness](product/OPEN_SOURCE_AND_PRODUCTION_READINESS.md)
6. [Personas and outcomes](product/PERSONAS_AND_OUTCOMES.md)
7. [Use-case catalogue](product/USE_CASE_CATALOGUE.md)
8. [End-to-end journeys](product/END_TO_END_JOURNEYS.md)
9. [Outline traceability](product/TRACEABILITY.md)
10. [Scope and prioritisation](product/SCOPE_AND_PRIORITISATION.md)
11. [Discovery questions](product/DISCOVERY_QUESTIONS.md)

## Stage gates

### Stage 1 — Product definition (current)

- identify users, buyers, problems, triggers, and desired decisions;
- define the complete use-case set and how the use cases reinforce each other;
- state evidence, confidence, provenance, and safety expectations;
- identify the smallest valuable customer proposition;
- evaluate assumptions through authoritative sources, public evidence, the
  fictional Horizon Synthetic Bank, and later qualified peer review.

### Stage 2 — Conceptual architecture

Begins after the product definition is reviewed. It will define information
domains, system boundaries, conceptual components, external actors, trust
boundaries, and capability interactions—without prematurely selecting detailed
technology.

### Stage 3 — Solution architecture and experiments

Begins only when the initial customer proposition and architecture questions
are sufficiently understood. Technology choices and prototypes belong here.

## Status language

All use cases in this repository are currently **product hypotheses**. They are
not implemented capabilities, validated customer demand, BIAN-provided
features, or compliance claims.

The project is intended to be independently open source, BIAN-native, secure by
design, and capable of meeting explicit bank-grade production-readiness gates.
It must not imply official BIAN or Red Hat affiliation, endorsement, or support.
