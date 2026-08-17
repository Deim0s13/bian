# Personas and desired outcomes

These personas are design hypotheses. A person may occupy more than one role,
particularly in a smaller bank. They will initially be exercised through Horizon
Synthetic Bank scenarios, public evidence, and qualified peer review rather than
customer trials. Their real-world priorities and operating fit therefore remain
unvalidated.

## Economic buyers and sponsors

### Chief Architect / Head of Enterprise Architecture

**Responsible for:** architecture direction, standards, target states, portfolio
simplification, and design governance.

**Needs to know:**

- where business responsibilities are implemented today;
- how consistently the bank uses BIAN as a common language;
- which projects duplicate or misplace capabilities;
- which target-state decisions have evidence behind them; and
- whether architecture governance is changing delivery outcomes.

**Desired outcome:** an actionable, maintained view of the bank's functional
architecture rather than another static assessment.

### Transformation Director / Programme Executive

**Responsible for:** major modernisation programmes, sequencing, dependencies,
benefits, and delivery risk.

**Needs to know:**

- which applications, APIs, integrations, and owners are affected;
- how a target design can be reached incrementally;
- what can be retired, retained, wrapped, or replaced;
- where dependencies threaten sequencing; and
- whether transformation is reducing fragmentation and risk.

**Desired outcome:** a defensible transition roadmap connected to the actual
estate and architecture decisions.

### CIO / CTO

**Responsible for:** technology investment, operating risk, simplification, and
enterprise delivery performance.

**Needs to know:**

- whether BIAN adoption is producing measurable benefit;
- where duplication, concentration, obsolescence, and ownership gaps exist;
- how vendor and modernisation choices affect the portfolio; and
- which decisions require investment or executive intervention.

**Desired outcome:** decision-quality scorecards with drill-down evidence, not a
single unqualified maturity number.

## Core practitioners

### Enterprise Architect

**Job to be done:** map the estate to a common banking capability language,
identify structural concerns, and guide cross-domain target states.

**Pain today:** information is fragmented across CMDBs, catalogues, diagrams,
repositories, and individual knowledge. Mappings are difficult to review and
quickly become stale.

**Desired outcome:** create, review, explain, and maintain mappings with visible
source, confidence, ownership, and impact.

### Domain / Solution Architect

**Job to be done:** design a change in context, allocate responsibilities,
identify affected systems, and pass architecture review.

**Pain today:** BIAN guidance is detached from the bank's design standards and
current implementations.

**Desired outcome:** start from a business scenario or change objective and
produce a bank-specific, BIAN-informed design and transition proposal.

### API Architect / API Product Owner

**Job to be done:** understand existing API responsibilities, improve contract
alignment, avoid duplication, and manage consumers and lifecycle.

**Pain today:** an API may combine multiple business responsibilities, duplicate
another interface, or use labels that obscure its purpose.

**Desired outcome:** receive an explainable mapping between API operations/data
and BIAN concepts, then manage remediation without blindly rewriting contracts.

### Platform Engineer / Developer

**Job to be done:** create and evolve services through approved engineering
paths while preserving business logic and operational ownership.

**Pain today:** reference standards, security requirements, templates, and
deployment controls are inconsistent or require manual interpretation.

**Desired outcome:** request an approved starting point that already reflects
the selected domain, version, security profile, ownership, and deployment
context and can be regenerated safely later.

### Application / Service Owner

**Job to be done:** keep authoritative information about an asset, understand
its responsibilities and dependencies, and evaluate proposed changes.

**Pain today:** centrally produced mappings can be inaccurate and ownership
records may not reflect operational reality.

**Desired outcome:** review and correct assertions about owned assets, see why a
change affects them, and approve or challenge mappings.

## Assurance and governance practitioners

### Security Architect

**Job to be done:** define reusable security expectations and ensure they are
applied consistently across relevant services and platforms.

**Desired outcome:** manage versioned security profiles and see their coverage,
exceptions, implementations, and verification evidence.

### Risk / Compliance / Control Owner

**Job to be done:** connect obligations to controls and determine what available
evidence actually verifies.

**Desired outcome:** see scoped control coverage, evidence freshness, exceptions,
and unverified areas without misleading compliance claims.

### Architecture Review Board / Design Authority

**Job to be done:** assess whether a proposal duplicates existing capability,
misplaces data ownership, or conflicts with target architecture.

**Desired outcome:** receive explainable checks and relevant existing context
before deciding, while retaining human authority for the final decision.

## Commercial and sourcing practitioners

### Vendor / Procurement / Core-Replacement Lead

**Job to be done:** compare products against required banking capabilities and
the bank's existing footprint.

**Desired outcome:** understand potential coverage, gaps, overlap, dependencies,
and evidence quality without treating vendor claims as independently verified
facts.

## Critical distinction: user, champion, buyer, and data owner

These roles may not be the same:

- the Chief Architect may sponsor the initiative;
- Enterprise Architects may operate the mapping process;
- application owners may supply and approve the data;
- a transformation programme may fund the first engagement;
- developers may consume generated outputs later; and
- risk teams may determine whether assurance language is acceptable.

Discovery must identify this operating model. A product that delights an
architect but creates unmanageable work for application owners will not remain
trusted or current.

## Outcome hierarchy

### Enterprise outcomes

- less functional duplication and architectural fragmentation;
- clearer ownership and accountability;
- safer, better-sequenced transformation;
- improved reuse of approved engineering and security patterns;
- quicker understanding of BIAN release changes;
- decision-quality evidence for architecture and control governance.

### User outcomes

- less manual discovery and reconciliation;
- faster, explainable analysis;
- reusable models instead of one-off diagrams;
- clear review and correction workflows;
- traceable outputs suitable for governance conversations.

### Product-quality outcomes

- users can distinguish fact, customer assertion, inference, and verification;
- every material conclusion can be traced to supporting information;
- confidence and limitations are visible;
- changes can be reviewed over time;
- automation accelerates judgment without impersonating it.
