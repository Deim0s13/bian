# Product vision

## Working proposition

The BIAN Adoption & Transformation Platform helps banks turn BIAN from a
reference framework into a practical way to understand, design, govern, and
change their technology estate.

It connects three things that are normally separate:

1. **BIAN's model of banking** — Service Domains, APIs, events, Business
   Objects, Business Scenarios, capabilities, and relationships.
2. **The bank as it exists** — applications, APIs, integrations, data,
   technology, owners, controls, vendors, and lifecycle state.
3. **The bank as it wants to become** — target architecture, engineering
   standards, migration plans, governance decisions, and assurance evidence.

The result should allow a bank to ask meaningful questions and receive answers
grounded in traceable information rather than generic advice.

## The problem

Banks do not generally start with a clean collection of BIAN-aligned services.
They have large application portfolios, overlapping APIs, accumulated legacy
technology, inconsistent ownership, duplicated capabilities, and incomplete
architecture records.

BIAN can provide a useful common functional language, but adoption remains hard:

- teams struggle to relate BIAN concepts to their actual estate;
- generating an API does not establish who should own or implement it;
- architects cannot easily measure current alignment or model target states;
- BIAN release changes are difficult to connect to bank-specific impact;
- security and regulatory requirements sit outside most generation workflows;
- executives cannot see whether adoption is producing measurable improvement;
- architecture guidance often remains detached from engineering delivery.

## Product promise

The platform should help a bank move through a continuous adoption cycle:

```text
Understand the BIAN model
          ↓
Map the current bank estate
          ↓
Assess alignment, duplication, ownership, and risk
          ↓
Design scenarios and target states
          ↓
Plan transformation
          ↓
Create governed engineering paths
          ↓
Verify controls and retain evidence
          ↓
Measure adoption and respond to BIAN releases
```

Each stage enriches the same body of knowledge rather than creating another
isolated assessment or diagram.

## Foundational capability: trusted model registry

The foundational capability is a **versioned knowledge model**, referred to for
now as the BIAN Model Registry. It is not itself the entire product and should
not be confused with a database implementation.

Conceptually, it holds and relates:

- authorised BIAN artefacts and their release versions;
- relationships between BIAN concepts;
- customer applications, APIs, data assets, integrations, owners, and vendors;
- customer-to-BIAN mappings;
- current-state and target-state assertions;
- security profiles and control mappings;
- regulatory requirements, tests, evidence, and scoped attestations;
- transformation decisions and roadmap dependencies;
- generated assets and the model elements from which they were produced.

Its defining quality is not storage. It is the ability to say **what is known,
where it came from, how confident the platform is, and who has reviewed it**.

## Four classes of truth

The platform must never blend different claims together without explanation.
It should distinguish at least:

### 1. External framework assertions

Content imported from an authorised BIAN release or another recognised source.
The original source, release, licence context, and import status must be known.

### 2. Customer assertions

Information supplied by the bank, such as application ownership, lifecycle,
technology, API purpose, or an architect-approved mapping.

### 3. Platform inferences

Mappings, duplication warnings, proposed target states, or recommendations
produced through rules, analysis, or AI. These require confidence, supporting
evidence, and a review state. They are not facts merely because a model produced
them.

### 4. Verified evidence

Results tied to an explicit test, scope, time, version, and control. Evidence can
support a narrow conclusion; it must not be inflated into a broad compliance
claim.

## Fourteen product use cases

The original concept is preserved as fourteen distinct customer-facing use
cases. They share the model foundation but solve different problems.

### Engineering and delivery

1. Model-driven engineering artefact generation
2. Safe regeneration with owned banking logic preserved
3. BIAN release impact and upgrade management
4. Consistent security profiles
5. Evidence-based control assurance
6. Developer self-service through a platform front door

### Architecture and transformation

7. Customer landscape mapping
8. Existing API alignment analysis
9. Current-state to target-state design and transition planning
10. Business Scenario Studio with customer implementation overlays
11. Evidence-backed modernisation advice
12. Vendor and product capability mapping

### Governance and adoption

13. Architecture governance and duplication detection
14. BIAN adoption scorecards and executive reporting

The detailed definitions are in [USE_CASE_CATALOGUE.md](USE_CASE_CATALOGUE.md).

## Strategic differentiation

The strongest proposition is not “generate BIAN APIs.” It is the combination of:

- BIAN knowledge;
- the customer's real estate;
- model-derived engineering outputs;
- architecture and transformation decisions;
- evidence and confidence;
- continuous release and adoption management.

A standalone generator can be copied. A trusted, evolving model of how a bank's
estate relates to BIAN—and how that relationship affects change—is considerably
more valuable and defensible.

## Product guardrails

- Never invent BIAN semantics and present them as authoritative.
- Never equate API conformance with architectural alignment.
- Never equate automated tests with broad regulatory compliance.
- Never hide uncertainty behind a single alignment percentage.
- Never overwrite customer-owned implementation through regeneration.
- Never treat AI inference as reviewed architecture truth.
- Never assume that publicly accessible material is commercially reusable.
- Always show source, release, scope, confidence, review state, and limitations
  where they materially affect a conclusion.

## What must be learned before architecture

The full vision is intentionally broad. Product discovery must establish:

- which customer problem is painful enough to fund first;
- who buys, champions, operates, and trusts the product;
- which customer data is realistically available and sufficiently reliable;
- which decisions users expect the platform to improve;
- what evidence users need before accepting a mapping or recommendation;
- which BIAN materials may legally and operationally be used;
- how much human review is acceptable or desirable; and
- which narrow proposition can demonstrate value without pretending to deliver
  the entire vision.

