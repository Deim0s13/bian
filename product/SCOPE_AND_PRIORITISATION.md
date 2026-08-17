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

Architecture components and technologies must contribute to a customer outcome.
Their selection and packaging should follow the product capability and evidence
needed, rather than becoming the definition of the platform.

## Candidate first propositions

### A. BIAN adoption baseline for a bounded domain

**Promise:** “We will show where the responsibilities in one important banking
domain are implemented today, how reliable those mappings are, and where the
most material duplication, ownership, and target-state questions lie.”

**Uses:** UC-07 Landscape Mapping, a focused part of UC-08 API Alignment, and a
carefully defined subset of UC-14 Adoption Scorecard. It can then lead into
UC-09 target-state planning.

**Why it is promising:**

- creates bank-estate knowledge that service generation and later use cases can
  reuse;
- creates customer-specific knowledge reused by most later use cases;
- produces findings an architecture or transformation sponsor can act on;
- can begin within a bounded area such as payments;
- tests the hardest trust question: will architects accept and maintain mappings?

**Primary tracked risk:** `RSK-013` in the
[Architecture Register](../governance/ARCHITECTURE_REGISTER.md#risks).

### B. API alignment and governance assessment

**Promise:** “We will analyse a selected API estate against BIAN, explain mixed
responsibilities and possible duplication, and help owners decide what to do.”

**Uses:** UC-08 API Alignment and UC-13 Architecture Governance, later UC-14.

**Why it is promising:** OpenAPI and gateway catalogues may be more accessible
than complete enterprise architecture data, and outputs can be concrete.

**Primary tracked risk:** `RSK-014` in the
[Architecture Register](../governance/ARCHITECTURE_REGISTER.md#risks).

### C. BIAN release impact service

**Promise:** “We will explain what changed between BIAN releases and which of
your reviewed mappings or engineering assets may be affected.”

**Uses:** UC-03 Release Impact, then UC-02 Safe Regeneration.

**Why it is promising:** it is repeatable, model-centric, and potentially highly
differentiated once a bank has established mappings.

**Primary tracked risk:** `RSK-015` in the
[Architecture Register](../governance/ARCHITECTURE_REGISTER.md#risks).

### D. Service Generator and engineering golden path

**Promise:** “Select a BIAN domain and organisational profile and receive a
governed, traceable engineering starting point.”

**Uses:** UC-01, UC-02, UC-04, and UC-06.

**Why it is promising:** visible demonstrations, tangible artefacts, and clear
platform-engineering users.

**Primary tracked risk:** `RSK-016` in the
[Architecture Register](../governance/ARCHITECTURE_REGISTER.md#risks).

### E. Evidence-based security and control assurance

**Promise:** “For a defined service and profile, show exactly which technical
controls are verified, with evidence and explicit gaps.”

**Uses:** UC-04 and UC-05.

**Why it is promising:** high-value governance problem and strong trust-based
differentiation.

**Primary tracked risk:** `RSK-017` in the
[Architecture Register](../governance/ARCHITECTURE_REGISTER.md#risks).

## Current architecture validation recommendation

Use a **connected, model-driven HSB journey** across the north-star structure,
initially within a bounded payments scope. Payments is a practical synthetic
scenario, not an assumed market choice or the definition of the platform.

The journey should progressively demonstrate that one governed model thread can:

1. ingest and version selected authorised BIAN Sources;
2. represent their semantics and relationships in the BIAN Model Registry;
3. connect HSB applications, APIs, integrations, data, owners, lifecycle, and
   reviewed mappings through Adoption & Architecture;
4. describe a current state, target option, and transition question;
5. drive traceable contracts, models, tests, and scaffolds through the Service
   Generator while preserving owned implementation boundaries;
6. apply a security profile and connect requirements, controls, tests, evidence,
   gaps, and scoped conclusions through Assurance & Compliance;
7. expose catalogue, templates, ownership, lifecycle, architecture governance,
   documentation, and scorecards through Platform Control;
8. describe and later validate delivery into selected Runtime Targets; and
9. assess how a BIAN or HSB change affects mappings, generated artefacts,
   controls, evidence, owners, and runtime consumers.

This does not require every capability to be implemented at once. It gives each
architecture increment a shared end-to-end thread and prevents any one pillar
from defining the product. HSB can validate internal coherence and technical
behaviour while market demand and real-bank operating fit remain unvalidated.

The complete vision must not be implemented as a shallow feature checklist. A
consumable release must support one meaningful decision through a complete
model thread. The applicable value tests and stop conditions are maintained in
[VALUE_AND_VALIDATION.md](VALUE_AND_VALIDATION.md).

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

Passing product definition does not authorise a full platform build. Any later
implementation approval is limited to the proposition supported by the
build-authorisation gate in
[VALUE_AND_VALIDATION.md](VALUE_AND_VALIDATION.md).
