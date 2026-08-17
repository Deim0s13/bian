# End-to-end customer journeys

The platform becomes valuable when use cases reinforce one another. These
journeys test whether the catalogue describes a coherent product rather than a
collection of unrelated tools.

## Journey 1: Modernise payments

### Situation

A bank knows its payments estate is fragmented across channels, a payment hub,
core banking, messaging, fraud systems, and manual controls. It wants a target
architecture and transition plan, not a generic BIAN diagram.

### Participants

Transformation director, enterprise architect, payments architect, application
owners, API owners, security architect, and programme teams.

### Journey

1. **Scope the assessment.** The team defines the payment products, legal
   entities, channels, and systems in scope.
2. **Map the landscape (UC-07).** Applications, APIs, integrations, data, owners,
   and lifecycle are reconciled and mapped to candidate BIAN responsibilities.
3. **Analyse critical APIs (UC-08).** Existing payment APIs are assessed for
   mixed responsibilities, duplication, and data concerns.
4. **Model important scenarios (UC-10).** Scenarios such as domestic or
   international payment initiation are overlaid with actual systems and controls.
5. **Ask focused questions (UC-11).** Architects explore why responsibilities are
   fragmented and what would be required to isolate Payment Initiation.
6. **Design target and transition states (UC-09).** The team models retained,
   wrapped, introduced, migrated, and retired elements and sequences changes.
7. **Govern delivery (UC-13).** Programme designs are checked against the agreed
   target, existing services, ownership, and exceptions.
8. **Measure progress (UC-14).** Executives see mapped coverage, fragmentation,
   ownership, remediation, and target-state progress with drill-down evidence.

### Customer outcome

A shared, evidence-backed payments transformation model connects the strategic
target to real applications, APIs, owners, dependencies, and programme actions.

### Value hypothesis

The bank should make better sequencing and boundary decisions, identify
duplication earlier, and spend less time reconstructing context for each project.

## Journey 2: Respond to a new BIAN release

### Situation

A new BIAN release becomes available. The bank needs to know what changed, what
matters to it, and whether generated or mapped assets require action.

### Participants

Chief Architect, BIAN/platform owner, enterprise architects, API owners, service
owners, and engineering teams.

### Journey

1. **Compare releases (UC-03).** The platform identifies semantic changes and
   source uncertainties.
2. **Resolve bank impact (UC-03 + UC-07).** Accepted mappings connect changed
   concepts to applications, APIs, consumers, owners, plans, and controls.
3. **Review alignment (UC-08).** Material APIs are reassessed where relevant.
4. **Regenerate safely (UC-02).** Affected generated contracts are updated while
   owned implementation remains separate.
5. **Regenerate other assets (UC-01).** Tests, SDKs, catalogue metadata, and
   documentation are refreshed where appropriate.
6. **Reverify controls (UC-04 + UC-05).** Changed security expectations or
   contracts trigger scoped verification and evidence renewal.
7. **Govern and report (UC-13 + UC-14).** Actions, deferrals, exceptions, owners,
   and adoption status remain visible.

### Customer outcome

The bank receives a manageable, bank-specific change programme instead of a
generic release comparison or wholesale regeneration exercise.

### Value hypothesis

Assessment time and missed impacts should fall, while adoption decisions become
traceable and owned.

## Journey 3: Introduce a new BIAN-informed service

### Situation

A product team proposes a new customer payment service. The bank wants to reuse
existing capability where sensible and use approved engineering/security paths.

### Participants

Product owner, solution architect, developer, platform engineer, API architect,
security architect, and architecture review board.

### Journey

1. **Discover context (UC-06).** The team searches for relevant BIAN domains,
   existing implementations, APIs, owners, and target-state guidance.
2. **Model the scenario (UC-10).** Responsibilities and interactions are made
   explicit, including customer-specific behaviour.
3. **Check the proposal (UC-13).** Potential duplication, ownership conflicts,
   mixed responsibilities, and policy concerns are raised early.
4. **Select an engineering path (UC-01 + UC-06).** The team chooses approved
   contract, event, test, catalogue, and deployment projections.
5. **Apply security context (UC-04).** The appropriate audience/risk profile is
   selected and unresolved controls are shown.
6. **Implement behind an owned boundary (UC-02).** Business logic and bank
   adapters remain separate from disposable generated assets.
7. **Verify scoped controls (UC-05).** Tests produce evidence tied to the exact
   service/version and list what they do not verify.
8. **Register and govern (UC-06 + UC-13).** Ownership, lifecycle, documentation,
   decisions, and exceptions become discoverable.

### Customer outcome

The team receives context and a governed delivery path rather than an empty
microservice or an architecture document disconnected from delivery.

### Value hypothesis

Teams should spend less time interpreting standards, create fewer duplicates,
and reach review with better evidence and clearer ownership.

## Journey 4: Evaluate a core-banking product

### Situation

A bank is considering a new core platform and wants to understand functional
coverage, overlap with its estate, and transition implications.

### Participants

Transformation director, enterprise architects, procurement, product/domain
owners, commercial teams, security/risk representatives, and vendor specialists.

### Journey

1. **Define required scope.** The bank selects BIAN responsibilities, scenarios,
   business constraints, and target outcomes, not merely a feature checklist.
2. **Map current estate (UC-07).** Current implementations, ownership, lifecycle,
   dependencies, and pain points are established.
3. **Map vendor claims (UC-12).** Claims are connected to BIAN concepts with
   evidence source and review status.
4. **Compare overlap and gaps (UC-12).** The platform highlights likely coverage,
   coexistence, residual capability, integration, and exit concerns.
5. **Test scenarios (UC-10).** Critical customer scenarios reveal which systems
   and vendor capabilities would participate.
6. **Explore options (UC-11).** Architects ask evidence-backed questions about
   replacement boundaries and dependency consequences.
7. **Design transitions (UC-09).** Alternative migration sequences and retained
   elements are modelled.
8. **Record the decision (UC-13).** Assumptions, evidence, risks, exceptions, and
   accountable approvals remain connected to the selected direction.

### Customer outcome

A product decision is connected to banking responsibilities and actual portfolio
impact, while vendor assertions remain distinguishable from bank-verified facts.

### Value hypothesis

The bank should ask better due-diligence questions, identify residual scope and
integration earlier, and retain a reusable decision model beyond the RFP.

## Journey 5: Establish evidence-backed API governance

### Situation

A bank has thousands of APIs, inconsistent ownership, and repeated concern that
teams are building overlapping services.

### Participants

API platform owner, API architects, enterprise architects, service owners,
solution architects, and architecture governance.

### Journey

1. **Inventory and reconcile (UC-07).** Gateway, specification, catalogue, and
   implementation records are linked.
2. **Prioritise analysis.** Scope is selected by domain, criticality, lifecycle,
   change volume, or suspected overlap.
3. **Assess alignment (UC-08).** Operations and data are mapped with confidence,
   mixed responsibilities, and candidate duplicates.
4. **Review with owners.** Findings are accepted, corrected, rejected, or turned
   into remediation work.
5. **Prevent recurrence (UC-13).** New proposals are checked against reviewed
   existing assets and target-state boundaries.
6. **Provide an approved path (UC-01 + UC-06).** Teams can discover existing
   APIs or create new ones through governed templates and ownership metadata.
7. **Track outcomes (UC-14).** Leaders see reviewed coverage, duplication actions,
   ownership gaps, and lifecycle progress rather than an opaque alignment score.

### Customer outcome

API governance shifts from periodic inventory exercises to a maintained model
that connects analysis, owners, remediation, new designs, and delivery paths.

### Value hypothesis

The bank should reduce duplicate creation, accelerate review, improve ownership,
and focus remediation on evidence-backed concerns.

## Journey-level questions for discovery

- Which journey begins with a funded event that customers already recognise?
- Who owns the outcome and budget for that event?
- Which inputs are available without a multi-year data-cleaning programme?
- What is the smallest scope that can produce a meaningful decision?
- Where is human review essential, and who will perform it?
- Which output would a customer act on within the first engagement?
- What existing tools must receive or provide information?
- What would make the customer distrust or abandon the result?
