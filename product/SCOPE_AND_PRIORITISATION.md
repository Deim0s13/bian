# Scope and prioritisation hypotheses

## Why prioritisation is necessary

The fourteen use cases form a coherent long-term proposition, but they do not
form a credible first product if attempted simultaneously. The immediate task is
not to choose what the platform will never do. It is to identify the first
valuable customer outcome that can establish trust and create reusable knowledge
for later use cases.

## Separate foundations from customer outcomes

The trusted model registry, provenance, versioning, inference status, review,
and change history are foundational qualities. Customers may value them, but
they are unlikely to buy “a canonical model” in isolation.

Likewise, a portal, database, AI model, graph technology, or API generator is not
a customer outcome. Technology selection should follow the chosen proposition.

## Candidate first propositions

### A. BIAN adoption baseline for a bounded domain: recommended for discovery

**Promise:** “We will show where the responsibilities in one important banking
domain are implemented today, how reliable those mappings are, and where the
most material duplication, ownership, and target-state questions lie.”

**Uses:** UC-07 Landscape Mapping, a focused part of UC-08 API Alignment, and a
carefully defined subset of UC-14 Adoption Scorecard. It can then lead into
UC-09 target-state planning.

**Why it is promising:**

- addresses the adoption problem that exists before service generation;
- creates customer-specific knowledge reused by most later use cases;
- produces findings an architecture or transformation sponsor can act on;
- can begin within a bounded area such as payments;
- tests the hardest trust question: will architects accept and maintain mappings?

**Primary risk:** customer source data may be incomplete, inconsistent, hard to
access, or politically sensitive. Review effort may dominate any automation.

### B. API alignment and governance assessment

**Promise:** “We will analyse a selected API estate against BIAN, explain mixed
responsibilities and possible duplication, and help owners decide what to do.”

**Uses:** UC-08 API Alignment and UC-13 Architecture Governance, later UC-14.

**Why it is promising:** OpenAPI and gateway catalogues may be more accessible
than complete enterprise architecture data, and outputs can be concrete.

**Primary risk:** contracts and names alone may be semantically insufficient.
Poor explanations or overconfident scores will quickly undermine trust.

### C. BIAN release impact service

**Promise:** “We will explain what changed between BIAN releases and which of
your reviewed mappings or engineering assets may be affected.”

**Uses:** UC-03 Release Impact, then UC-02 Safe Regeneration.

**Why it is promising:** it is repeatable, model-centric, and potentially highly
differentiated once a bank has established mappings.

**Primary risk:** its bank-specific value is limited before the customer model
exists. Release frequency and urgency may not support it as the first wedge.

### D. BIAN engineering golden path

**Promise:** “Select a BIAN domain and organisational profile and receive a
governed, traceable engineering starting point.”

**Uses:** UC-01, UC-02, UC-04, and UC-06.

**Why it is promising:** visible demonstrations, tangible artefacts, and clear
platform-engineering users.

**Primary risk:** it can collapse into commodity code generation and create many
technically valid but organisationally unowned services. It does not by itself
solve BIAN adoption.

### E. Evidence-based security and control assurance

**Promise:** “For a defined service and profile, show exactly which technical
controls are verified, with evidence and explicit gaps.”

**Uses:** UC-04 and UC-05.

**Why it is promising:** high-value governance problem and strong trust-based
differentiation.

**Primary risk:** high domain, legal, audit, integration, and liability burden.
It should not be the first proposition without expert control ownership.

## Current recommendation

Run product discovery around **a bounded BIAN adoption and modernisation
assessment**, initially using payments as the working example but not assuming
payments is the final market choice.

The first assessment will be performed against Horizon Synthetic Bank. It will
validate the internal product logic and required evidence while leaving market
demand and real-bank operating fit explicitly unvalidated.

The assessment would aim to answer:

1. Where are the selected BIAN responsibilities implemented today?
2. Which mappings are known, inferred, disputed, or missing?
3. Where are responsibilities fragmented or duplicated?
4. Which APIs combine responsibilities that deserve architectural review?
5. Which ownership and lifecycle concerns matter to the target objective?
6. What target-state options and transition questions follow from the evidence?
7. How should progress be measured without a misleading adoption score?

This proposition leads with customer understanding and transformation value. It
also establishes the information needed for later governance, release impact,
engineering, vendor mapping, and assurance use cases.

## What the first proposition should not promise

- automatic mapping of an entire bank;
- an authoritative answer without architect and owner review;
- a universal BIAN alignment score;
- a complete target architecture generated by AI;
- service generation as evidence of adoption;
- compliance or certification;
- immediate replacement of enterprise architecture, CMDB, or API-management
  systems.

## Prioritisation criteria

Each proposition should first be assessed through official sources, public case
studies, HSB scenario exercises, and qualified peer review. This can establish
coherence and technical feasibility, but buyer demand remains unvalidated.

| Criterion | Question |
|---|---|
| Pain and urgency | Is this a recognised problem tied to a funded event? |
| Buyer clarity | Who owns the outcome and can fund it? |
| Actionability | Will the customer make a decision from the output? |
| Data feasibility | Can required inputs be accessed and interpreted? |
| Trust feasibility | Can conclusions be explained and reviewed? |
| Time to value | Can a bounded engagement show value quickly? |
| Reusability | Does the resulting knowledge support later use cases? |
| Differentiation | Is the value more than generic mapping or generation? |
| Operating burden | Can the customer keep the result current? |
| Legal/commercial risk | Are source rights and claims manageable? |

## Product-definition exit criteria

Move into conceptual architecture when the product definition is internally
coherent and there is adequate documented evidence or an explicit unvalidated
hypothesis for:

- the first target adopter and likely trigger;
- the primary user and accountable decision-maker;
- the decision or workflow the first proposition improves;
- the required inputs and likely data quality;
- the review and operating model;
- the output the customer will act upon;
- clear success measures and unacceptable failure modes;
- how the first proposition contributes to the larger fourteen-use-case vision.

Architecture must also have approved inputs from the BIAN alignment policy,
fictional-bank validation plan, open-source governance requirements, and
production-readiness policy.
