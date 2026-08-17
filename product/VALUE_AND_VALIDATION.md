# Value proposition and validation strategy

## Document purpose

This document tests whether the BIAN Adoption & Engineering Platform is worth
building. It prevents architectural coherence, technical feasibility, or feature
breadth from being mistaken for customer value.

The product vision remains the north-star. It does not constitute build
authorisation.

## Current investment position

**Continue product discovery and conceptual architecture. Do not authorise a
full platform build yet.**

There is a credible value hypothesis, but insufficient evidence that banks or
practitioners will adopt, operate, or act on the complete platform. Horizon
Synthetic Bank can establish internal coherence, repeatability, safety, and
future technical behaviour. It cannot establish external desirability, buyer
commitment, real-bank data feasibility, regulatory acceptance, or realised
benefit.

This position must remain visible until evidence supports a different decision.

## Primary value hypothesis

The strongest potential value is a closed, traceable decision thread:

```text
Authoritative BIAN concept and release
        -> reviewed bank-estate mapping
        -> architecture finding or target decision
        -> model-derived engineering asset
        -> security requirement, control, test, and evidence
        -> ownership, lifecycle, and governance
        -> change and downstream impact
```

The platform should reduce translation loss between BIAN, enterprise
architecture, engineering delivery, assurance, and change governance. No single
feature in this chain is assumed to be differentiated by itself.

## Intended first users and decision

The accepted working architecture hypothesis under `DEC-018` uses an enterprise
or payments domain architect as the primary user. A Chief Architect or Head of
Enterprise Architecture sponsors the architecture outcome, while a payments
transformation sponsor represents funding and sequencing. Architecture
enablement or BIAN stewardship represents the operational owner. Real-world
buyer demand and operating fit remain unvalidated under `EVD-001`.

The first named decision is:

> Which HSB assets should own, support, or relinquish a bounded
> customer-payment initiation responsibility in the target state, and how should
> the transition be sequenced?

This is project and HSB scope until exact BIAN R14 relationships are qualified
from authorised sources. Other decisions in the fourteen-use-case vision remain
valid later propositions rather than part of the first user outcome.

CIO dashboards, developer self-service, and compliance reporting are downstream
benefits. They should not be treated as the first source of adoption.

## Value and challenge by platform area

| Area | Potential value | Challenge to prove | Current position |
|---|---|---|---|
| BIAN Sources and Model Registry | Preserve release-qualified meaning, provenance, relationships, mappings, and change impact | A searchable copy of BIAN or a database of API files is insufficient | Essential shared foundation, low standalone user value |
| Adoption & Architecture | Improve mapping, responsibility, duplication, target-state, vendor, and transition decisions | Generic enterprise architecture tools already cover inventories, capabilities, dependencies, and roadmaps; reliable bank inputs may be expensive to obtain and maintain | Strongest initial user-value candidate when bounded to a real decision |
| Service Generator | Carry approved model, profile, ownership, and provenance into disposable engineering assets | Generic client, server, documentation, and template generation is mature and readily available | Supporting capability, not a sufficient standalone proposition |
| Assurance & Compliance | Connect requirements, controls, implementations, tests, evidence, gaps, and scoped conclusions | High expertise, integration, legal, audit, and liability burden; established GRC and evidence standards already exist | Valuable narrow extension, not a general compliance product |
| Platform Control | Make ownership, lifecycle, workflow, documentation, templates, and findings discoverable | Established developer portals already provide catalogues, templates, documentation, and plugins | Experience and integration layer, not the core product |
| Runtime Targets | Demonstrate secure, supportable and portable operation in approved contexts | Deployment packaging does not prove product value or bank production readiness | Readiness requirement, not differentiation |

## Existing alternatives and market constraints

These sources are external assertions used to understand substitution and
overlap. They do not define this product's architecture and do not prove that an
alternative is better, widely adopted, or suitable for a specific bank.

| External evidence | Relevance to the value test |
|---|---|
| [BIAN Portal](https://bian.org/bian-portal/) | BIAN describes a Business Scenario Designer, API Align, and a forthcoming Application Landscape Mapper. BIAN exploration, scenario design, API alignment, and basic landscape mapping cannot be assumed to be unique. |
| [BIAN Agentic Banking Studio](https://bian.org/webinars/making-bian-real-live-demo-of-bians-agentic-banking-studio/) | BIAN is continuing to invest in applied adoption tooling, so differentiation cannot depend on static assumptions about BIAN's own capabilities. |
| [BIAN public repository](https://github.com/bian-official/public) | Public R14 Semantic API and AsyncAPI artefacts provide a feasible source for a bounded API-related use case, subject to exact licence and provenance review. |
| [BIAN membership FAQ](https://bian.org/about-bian/faqs/membership/) | BIAN states that non-members have read-only access to published materials while members receive additional formats and materials. Rights must be established artefact by artefact before open-source redistribution. |
| [SAP LeanIX application portfolio assessment](https://www.leanix.net/en/use-cases/application-portfolio-assessment) | Application inventory, business capability mapping, dependencies, redundancy analysis, and transformation views are established enterprise architecture capabilities. The platform should integrate rather than recreate a full EA repository. |
| [OpenAPI Generator](https://openapi-generator.tech/) | Generic client, server, schema, and documentation generation is established open-source capability. BIAN lineage and the connection to reviewed architecture decisions must create any additional value. |
| [Red Hat Developer Hub](https://access.redhat.com/products/red-hat-developer-hub/) | Software catalogue, templates, documentation, and extensibility are existing platform capabilities. Platform Control should use governed integration rather than duplicate a portal. |
| [NIST OSCAL](https://pages.nist.gov/OSCAL/) | Machine-readable controls, implementation and assessment information already have an open standard. Assurance should align or interoperate where appropriate rather than invent a competing general-purpose evidence model. |

Sources last reviewed on 17 August 2026. Capability statements and market
conditions require review before a material product or investment decision.

## Minimum consumable product hypothesis

A consumable release is not a shallow feature from every platform block. It is
one complete, usable journey in which a primary user can make a meaningful
decision without project-developer intervention.

The initial HSB hypothesis is that an architect can:

1. select an authorised BIAN release and inspect source provenance;
2. import a bounded application and API landscape;
3. propose, review, accept, reject, and explain mappings to BIAN;
4. identify responsibility, ownership, duplication, and boundary concerns;
5. record a current state, target option, and transition decision;
6. generate one traceable engineering package without overwriting owned logic;
7. apply one security profile and distinguish verified controls from gaps;
8. publish ownership, lifecycle, documentation, and findings through Platform
   Control; and
9. change a BIAN or HSB artefact and identify downstream impact.

The first user outcome is reached at step 5 through a reviewed target and
transition decision. Steps 6 through 9 test the connected value of that decision
across later platform concerns; they are not permission to implement every
capability at equal depth or make payments the product centre.

## Validation tests

Before a full build is authorised, evidence must address all of the following:

| Test | Question | Acceptable evidence at the current stage |
|---|---|---|
| Decision value | Which named user makes which materially better or faster decision? | Repeatable HSB scenario, explicit before and after decision process, and qualified independent critique |
| Connected differentiation | Does the shared model produce value that a collection of existing tools does not readily provide? | Alternatives analysis and a demonstrable cross-pillar traceability or change-impact outcome |
| Input feasibility | Can the required BIAN and bank information be obtained, understood, governed, and maintained? | Source-rights register, synthetic import exercise, ambiguity cases, ownership model, and maintenance estimate |
| Trust | Can users understand provenance, uncertainty, review state, and limitations well enough to act? | Explainable findings, review workflow, disputes, negative cases, and no hidden promotion of inference to fact |
| Adoption fit | Can the platform coexist with EA, API, GRC, source-control, delivery, and portal systems? | Clear system-of-record boundaries, portable exchange, and at least one credible integration path |
| Sustainable scope | Can an open-source maintainer group deliver and support the bounded proposition safely? | Narrow release scope, maintenance model, rights position, security process, and explicit support status |
| External desirability | Is there evidence that intended users recognise the problem and would invest time or sponsorship? | Qualified peer review, public evidence, independent usage, contributor interest, or later authorised stakeholder research |

HSB can contribute to the first six tests but cannot satisfy external
desirability by itself.

## Stop or narrow conditions

The project should stop, pause, or materially narrow the affected proposition if:

- source rights prevent a useful and lawful open-source distribution;
- the BIAN Model Registry offers no material value beyond authoritative BIAN
  source access;
- useful mappings require an unsustainable amount of manual reconciliation;
- intended users prefer to maintain the required BIAN relationships entirely in
  an existing system and gain no value from the shared model;
- generated assets provide no meaningful advantage over existing generators and
  organisational templates;
- Assurance & Compliance expands into an unsupported general-purpose GRC or
  regulatory interpretation product;
- adoption requires several organisational teams before any one user receives
  useful value;
- no output changes or materially supports an identifiable decision; or
- the scope cannot be maintained securely by the available open-source
  community.

Stopping or narrowing is a valid evidence-based outcome, not a project failure.

## Build-authorisation gate

Architecture work may continue while the hypotheses are tested. A full product
build should be authorised only when:

- a primary user, decision, trigger, and bounded outcome are explicit;
- the connected value is demonstrably more than feature aggregation;
- the minimum required sources and redistribution model are lawful;
- required input and review effort appear sustainable;
- the product boundary complements rather than casually replaces established
  systems;
- success measures and stop conditions are accepted; and
- remaining uncertainty is proportionate to a bounded implementation
  experiment.

Passing this gate authorises only the bounded proposition or experiment supported
by the evidence. It does not authorise the complete fourteen-use-case platform.

## Review discipline

Review this document when:

- a product proposition is selected or materially changed;
- authoritative BIAN tooling, sources, terms, or releases change;
- an external alternative changes the differentiation case;
- an HSB scenario produces material evidence;
- qualified peer or user evidence is received;
- solution architecture or implementation is proposed; or
- a stop condition is approached.

Record durable changes in the
[Architecture Register](../governance/ARCHITECTURE_REGISTER.md) and update the
project status. Do not remove a failed hypothesis merely because it is
inconvenient.
