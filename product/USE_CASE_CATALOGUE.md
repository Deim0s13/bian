# Use-case catalogue

## How to read this catalogue

These fourteen use cases preserve the complete original product outline. They
are customer-problem definitions, not promises of implemented functionality and
not predetermined technical components.

Every use case is currently at **Concept** status and requires customer
validation. “Platform” below refers to the proposed product, not existing code.

## Shared foundation: FDN-01 — Trusted BIAN and bank knowledge model

This is a prerequisite shared across the use cases rather than a standalone
customer outcome.

### Purpose

Maintain a versioned and explainable body of knowledge connecting BIAN concepts
to the customer's actual estate, decisions, controls, evidence, and generated
assets.

### Information it may eventually connect

- BIAN releases, Service Domains, Business Objects, APIs, events, Business
  Scenarios, capabilities, landscape groupings, and explicit relationships;
- customer applications, services, APIs, integrations, data assets, platforms,
  vendors, technologies, owners, consumers, and lifecycle states;
- candidate, reviewed, accepted, rejected, and superseded mappings;
- current-state, transition-state, and target-state architecture;
- security profiles, requirements, controls, implementations, tests, evidence,
  exceptions, and attestations;
- generated artefacts, versions, source model elements, and consuming systems.

### Trust expectations

Every material assertion should expose its source, version, scope, author or
producer, confidence where relevant, review state, and change history. The model
must distinguish BIAN content, customer-supplied facts, platform inferences,
third-party claims, and verified evidence.

---

## UC-01 — Generate engineering artefacts from the BIAN-informed model

**Original idea:** treat BIAN as compiler input, producing many artefacts rather
than merely converting OpenAPI into a service.

**Primary actors:** platform engineer, developer, API architect, domain architect.

**Desired outcome:** create a consistent engineering starting point linked to an
approved BIAN domain, bank context, and model version.

**Initiating event:** a team needs to create or standardise a service, API, event,
SDK, test harness, mock, catalogue entry, deployment definition, or related asset.

**Required inputs:**

- selected BIAN concept and release;
- approved customer extension or mapping, if applicable;
- desired projection types;
- organisation standards and target runtime context;
- ownership, lifecycle, and version information.

**Conceptual flow:**

1. The user selects the relevant model element and confirms its source/release.
2. The platform displays available projections and any unsupported or absent
   source semantics.
3. The user selects desired outputs and organisation-specific profiles.
4. The platform generates traceable artefacts and a generation manifest.
5. Validation reports what was derived, extended, defaulted, or left unresolved.
6. Generated outputs enter the customer's normal review and delivery process.

**Outputs:** potentially OpenAPI, AsyncAPI, domain/data models, service contracts,
SDKs, test harnesses, mocks, documentation, catalogue metadata, IaC templates,
security-policy hooks, and observability defaults.

**Decisions enabled:** whether a generated starting point is suitable, what must
be supplied by the implementation team, and which outputs are affected by later
model changes.

**Trust and safety rules:** absence of a BIAN operation is not permission to
invent one. Generated content must identify derived versus customer-authored
semantics. Generation does not make an artefact production-ready.

**Success signals:** reduced setup effort; fewer inconsistent contracts and
templates; traceable generated assets; teams regenerate rather than hand-forking.

**Outside this use case:** implementing business logic, selecting a bank's
runtime architecture, or certifying a service as BIAN-compliant.

---

## UC-02 — Regenerate safely while preserving bank-owned implementation

**Original idea:** keep generated content completely separate from business
logic, adapters, and configuration.

**Primary actors:** developer, platform engineer, service owner, release manager.

**Desired outcome:** adopt updated source models or generator improvements
without overwriting or obscuring owned banking behaviour.

**Initiating event:** a BIAN release, customer mapping, profile, template, or
generator changes.

**Required inputs:** prior generation manifest, new model/profile versions,
generated contract, owned implementation interfaces, compatibility policy.

**Conceptual flow:**

1. The platform identifies the previous source and generator versions.
2. It calculates changes relevant to the generated projection.
3. It classifies compatibility and shows the affected generated interfaces.
4. The user reviews impact on owned implementations and adapters.
5. The generated layer is replaced without editing the owned layer.
6. Contract and integration tests verify the retained implementation boundary.

**Outputs:** regenerated artefacts, compatibility report, implementation-impact
list, migration actions, and retained traceability.

**Decisions enabled:** whether regeneration is safe, which owned components need
attention, and whether to adopt, defer, or partially apply the change.

**Trust and safety rules:** generated and owned files must have an unambiguous
boundary. The platform must not claim that successful regeneration proves the
business implementation is correct.

**Success signals:** owned logic survives regeneration; changes are predictable;
manual merging declines; teams can explain exactly why code changed.

---

## UC-03 — Assess and manage BIAN release impact

**Original idea:** make BIAN release management a first-class enterprise feature.

**Primary actors:** enterprise architect, API architect, service owner,
transformation lead, platform owner.

**Desired outcome:** understand which changes between BIAN releases matter to
the bank and what action they require.

**Initiating event:** a new BIAN release or corrected source package becomes
available, or a bank considers changing its adopted version.

**Required inputs:** authorised source releases, stable identity/reconciliation
rules, bank mappings, generated-asset lineage, consumers, owners, and lifecycle.

**Conceptual flow:**

1. The platform compares BIAN concepts and relationships, not just file text.
2. Changes are classified—for example addition, removal, rename, schema change,
   behavioural change, or relationship change.
3. Bank mappings reveal which applications, APIs, data, plans, and controls are
   potentially affected.
4. Owners review false positives, materiality, and compatibility.
5. The platform records required action, responsible owner, decision, and status.
6. Relevant engineering assets may proceed to UC-02 for safe regeneration.

**Outputs:** release summary, bank-specific impact report, affected assets and
consumers, change classification, migration proposals, and action register.

**Decisions enabled:** whether and when to adopt a release; which teams must act;
which changes are irrelevant, breaking, or beneficial for this bank.

**Trust and safety rules:** source identity uncertainty must be explicit. A
structural diff is not automatically a business-impact conclusion. Owners must
be able to review mappings and materiality.

**Success signals:** shorter release assessment; fewer missed impacts; a smaller,
bank-specific action set; visible ownership of upgrade decisions.

---

## UC-04 — Apply consistent, context-specific security profiles

**Original idea:** security is a platform layer expressed through reusable
profiles, not hard-coded independently into every service.

**Primary actors:** security architect, platform engineer, API owner, developer.

**Desired outcome:** consistently apply the right security expectations for an
internal, partner, public, payment, or other service context.

**Initiating event:** a service is created, exposed to a new audience, migrated,
or reviewed against a changed security standard.

**Required inputs:** service exposure and risk context, approved security
profiles, identity/gateway/platform capabilities, exceptions, and control links.

**Conceptual flow:**

1. The service context determines applicable candidate profiles.
2. The user selects or confirms a profile such as internal-bank, partner-api,
   public-api, or an applicable financial API profile.
3. The platform resolves requirements across gateway, identity provider, policy
   engine, middleware, secrets, audit, and service-to-service identity.
4. Unsupported controls and exceptions are identified.
5. Engineering hooks and verification expectations are attached to the service.
6. Evidence may flow into UC-05; coverage appears in governance views.

**Outputs:** applicable security requirements, configuration/policy projections,
test expectations, exceptions, ownership, and coverage status.

**Decisions enabled:** which profile applies, whether the target platform can
enforce it, and which gaps need remediation or accepted exception.

**Trust and safety rules:** a profile describes expected controls; it does not
prove correct implementation. Regulatory or scheme names require controlled,
versioned mappings and appropriate expert review.

**Success signals:** fewer one-off interpretations; consistent enforcement;
explicit exceptions; quicker review; reusable evidence.

---

## UC-05 — Produce evidence-based, scoped control assurance

**Original idea:** compliance is an evidence chain, not a checkbox.

**Primary actors:** control owner, security architect, risk/compliance analyst,
service owner, auditor or assurance reviewer.

**Desired outcome:** understand what technical controls have actually been
verified for a precise system/version/scope and what remains unverified.

**Initiating event:** release assessment, control testing, audit preparation,
service approval, evidence expiry, or control/profile change.

**Required inputs:** regulation or policy interpretation, requirements, controls,
implementations, test definitions, execution results, scope, versions, exceptions,
and accountable reviewers.

**Conceptual flow:**

1. Applicable requirements are mapped to defined controls.
2. Controls are linked to expected implementations and verification methods.
3. Tests execute in the customer's approved environment or evidence is imported.
4. Evidence records source, result, time, scope, version, and integrity metadata.
5. Gaps, failures, expired evidence, and untested requirements remain explicit.
6. A reviewer issues a narrowly worded, scoped status or attestation if permitted.

**Outputs:** control coverage, evidence bundle, failures and exceptions, freshness
status, unverified areas, and scoped attestation language.

**Decisions enabled:** whether a technical control is sufficiently evidenced,
what must be remediated, and what can legitimately be asserted.

**Trust and safety rules:** preserve the chain `regulation → requirement → control
→ implementation → test → evidence → scoped attestation`. Never claim broad
regulatory compliance from code or conformance tests alone.

**Success signals:** reduced evidence collection effort; fewer ambiguous claims;
clear gaps; repeatable assurance; reviewers can reproduce conclusions.

---

## UC-06 — Provide a developer and architect self-service front door

**Original idea:** use Red Hat Developer Hub/Backstage as a future front door for
catalogue, templates, ownership, lifecycle, scorecards, and documentation.

**Primary actors:** developer, platform engineer, solution architect, service
owner, platform product owner.

**Desired outcome:** access approved BIAN-informed workflows and trustworthy
context in the place teams already use to create and manage software.

**Initiating event:** a user wants to discover an existing capability, create a
service, review ownership, understand standards, or inspect scorecards.

**Required inputs:** approved workflows, model/catalogue information, identity
and access, ownership, lifecycle, profiles, templates, and target platform data.

**Conceptual flow:**

1. The user searches or selects a BIAN domain, customer capability, or asset.
2. The portal shows relevant owners, implementations, APIs, standards, and
   lifecycle information.
3. The user starts an approved workflow such as create, align, review, or assess.
4. Required context is captured through a guided form.
5. The platform invokes the appropriate underlying capability.
6. Outputs are published to the relevant repositories, catalogues, or reviews.

**Outputs:** discoverable catalogue entries, golden-path workflows, linked
documentation, ownership/lifecycle views, and task/result status.

**Decisions enabled:** whether to reuse or create; which standard path applies;
who owns the result; where to find supporting evidence.

**Trust and safety rules:** the portal is an interaction surface, not the source
of truth. The core proposition must not depend on one portal product.

**Success signals:** higher discovery and reuse; fewer support hand-offs; greater
golden-path adoption; current ownership and documentation.

---

## UC-07 — Map a customer's application, API, integration, and data landscape

**Original idea:** BIAN Landscape Mapper.

**Primary actors:** enterprise architect, application owner, portfolio manager,
API architect, transformation analyst.

**Desired outcome:** understand where BIAN responsibilities are implemented in
the actual bank estate and identify fragmentation, duplication, and gaps.

**Initiating event:** adoption assessment, transformation programme, portfolio
review, acquisition/integration, or architecture baseline exercise.

**Required inputs:** CMDB, application catalogue, API specifications/gateway
catalogue, integrations, data catalogue, architecture repository, source
metadata, descriptions, owners, lifecycle, and known domain mappings.

**Conceptual flow:**

1. The bank defines scope—for example payments, customer servicing, or a legal
   entity—and identifies source systems.
2. The platform inventories and reconciles customer assets and identifiers.
3. Candidate BIAN mappings are proposed with rationale, evidence, and confidence.
4. Architects and asset owners review, correct, accept, reject, or defer mappings.
5. The platform analyses responsibility distribution, overlap, unmapped assets,
   ownership conflicts, lifecycle risks, and dependency concentrations.
6. The accepted baseline is versioned and maintained as inputs change.

**Outputs:** BIAN-to-customer landscape map, mapping register, confidence/review
status, duplication and gap findings, ownership conflicts, and coverage baseline.

**Decisions enabled:** where to simplify, what needs ownership clarification,
which areas warrant deeper analysis, and where BIAN adoption can add value.

**Trust and safety rules:** do not force every asset into BIAN. Candidate mappings
must show evidence and uncertainty. Customer-approved corrections take precedence
over unreviewed inference but retain history.

**Success signals:** useful coverage for the chosen scope; high review acceptance;
material findings; less manual reconciliation; baseline remains maintainable.

---

## UC-08 — Analyse an existing API's alignment with BIAN

**Original idea:** BIAN API Alignment connected to the customer's wider estate,
ownership, controls, and remediation workflow.

**Primary actors:** API architect, API product owner, enterprise architect,
developer, architecture reviewer.

**Desired outcome:** understand which BIAN responsibilities an API appears to
serve, where it combines concerns, and how it relates to existing implementations.

**Initiating event:** API design/review, portfolio rationalisation, modernisation,
gateway migration, duplication concern, or standards assessment.

**Required inputs:** API contract and documentation, operation descriptions,
schemas, consumers, implementation, owner, telemetry where permitted, and the
relevant BIAN model/release.

**Conceptual flow:**

1. The user supplies or selects an API and analysis scope.
2. Operations and information concepts are compared with candidate BIAN domains.
3. The platform explains suggested mappings and highlights weak or conflicting
   evidence.
4. Behaviours that may belong to other domains are identified.
5. Existing APIs and implementations are checked for possible duplication.
6. The user reviews findings and records accepted mapping or remediation actions.

**Outputs:** domain/operation/data mapping, confidence and evidence, mixed-
responsibility findings, potential duplicates, gaps, and remediation options.

**Decisions enabled:** retain, relabel, decompose, wrap, redesign, retire, or
accept the API with documented rationale.

**Trust and safety rules:** alignment is not binary compliance. Similar names do
not prove semantic equivalence. Scores must decompose into explainable findings
and never obscure uncertainty.

**Success signals:** reviewers find the analysis accurate and useful; duplicate
or misplaced behaviour is discovered; remediation decisions are recorded.

---

## UC-09 — Design current, transition, and target states

**Original idea:** current-state to target-state BIAN architecture and roadmap.

**Primary actors:** enterprise architect, domain architect, transformation lead,
programme architect, application owners.

**Desired outcome:** turn an agreed transformation objective into a coherent,
sequenced BIAN-informed target design grounded in current reality.

**Initiating event:** a bank decides to modernise a domain, simplify a portfolio,
adopt a platform, replace a core, or remediate an architecture concern.

**Required inputs:** reviewed current landscape, business scenarios, target
principles, constraints, dependencies, lifecycle, change initiatives, budgets or
time horizons where appropriate, and architecture decisions.

**Conceptual flow:**

1. The user selects business scope and desired outcomes.
2. The platform presents the relevant current-state responsibilities and assets.
3. Architects allocate responsibilities to candidate target capabilities and
   define retained, wrapped, migrated, introduced, and retired elements.
4. Dependencies and transition states are modelled explicitly.
5. The platform proposes sequencing and highlights risk, prerequisite, and
   ownership conflicts.
6. Architects review alternatives and publish a governed target and roadmap.

**Outputs:** current/target views, transition architectures, gap analysis,
dependency graph, sequenced roadmap, decisions, assumptions, and affected owners.

**Decisions enabled:** what to change, in what order, what to retain, where to
introduce boundaries, and which dependencies must be resolved first.

**Trust and safety rules:** recommendations are alternatives, not automatic
architecture decisions. Costs, organisational constraints, and operational risk
must not be inferred without sufficient evidence.

**Success signals:** roadmap is accepted by accountable owners; dependencies are
identified earlier; target-state decisions link to programme work and outcomes.

---

## UC-10 — Model business scenarios and overlay the customer's implementation

**Original idea:** Business Scenario Studio that builds on, rather than merely
copies, BIAN scenario concepts.

**Primary actors:** business architect, domain architect, solution architect,
product owner, application owner.

**Desired outcome:** describe a banking outcome as interactions between
responsibilities, then show how the bank currently or potentially implements it.

**Initiating event:** design workshop, operating-model review, incident analysis,
new product/change, customer-journey analysis, or target-state design.

**Required inputs:** scenario goal, participants, relevant BIAN concepts and
interactions, customer channels/applications/integrations, ownership, controls,
and current/target context.

**Conceptual flow:**

1. The user describes or selects a business scenario.
2. Relevant BIAN interactions are imported or proposed with source status shown.
3. The user adds bank-specific steps and exceptions without relabelling them as
   BIAN-defined content.
4. Customer systems, APIs, integrations, teams, and controls are overlaid.
5. The platform highlights missing ownership, duplicated hand-offs, control
   points, and current-versus-target differences.
6. The scenario is reviewed and linked to architecture or transformation work.

**Outputs:** interaction model, customer implementation overlay, responsibility
and control points, gap/duplication findings, and current/target comparisons.

**Decisions enabled:** where responsibilities should sit, which hand-offs need
design, what systems participate, and where change delivers scenario outcomes.

**Trust and safety rules:** imported BIAN scenarios, customer additions, and
platform proposals must remain distinguishable. A plausible generated scenario
is not automatically an authoritative business process.

**Success signals:** stakeholders share one understandable scenario; system and
responsibility gaps become visible; scenarios are reused across design work.

---

## UC-11 — Provide evidence-backed modernisation advice

**Original idea:** BIAN Modernisation Advisor using AI to reason over the model,
not merely “chat with BIAN.”

**Primary actors:** enterprise architect, transformation lead, domain architect,
application owner, programme analyst.

**Desired outcome:** answer consequential architecture questions using the
bank's reviewed model and show the evidence and assumptions behind the answer.

**Initiating event:** a user asks why an area is poorly aligned, what would be
required to isolate a capability, or how a change affects the estate.

**Required inputs:** reviewed landscape mappings, APIs, dependencies, ownership,
scenarios, current/target states, lifecycle, decisions, and relevant BIAN model.

**Conceptual flow:**

1. The user asks a scoped architecture or transformation question.
2. The platform identifies the model elements and evidence relevant to the query.
3. It presents findings, uncertainty, assumptions, and missing information.
4. It proposes options with consequences and dependencies rather than a single
   unexplained answer.
5. The user challenges, refines, or asks for supporting views.
6. Any accepted decision is recorded through the appropriate governance process.

**Outputs:** explained analysis, evidence links, options, dependency/impact views,
assumptions, confidence, missing data, and suggested next investigations.

**Decisions enabled:** which modernisation options deserve analysis, what prevents
a target boundary, and what data or stakeholder review is still needed.

**Trust and safety rules:** AI is an analytical assistant, not a design authority.
Every material claim needs traceable support. Unsupported certainty and invented
estate facts are unacceptable.

**Success signals:** answers withstand architect review; evidence is accessible;
analysis time falls; users discover dependencies or options they had missed.

---

## UC-12 — Map vendor and product capabilities to BIAN and the bank estate

**Original idea:** vendor/product mapping for core replacement, RFPs, overlap,
and exit strategy.

**Primary actors:** sourcing lead, enterprise architect, transformation director,
product owner, commercial analyst, vendor representative as a contributor.

**Desired outcome:** compare products against required banking responsibilities
and understand their overlap with the bank's current and target estate.

**Initiating event:** RFP, vendor due diligence, core replacement, platform
selection, contract renewal, consolidation, or exit planning.

**Required inputs:** required BIAN scope, vendor capability claims, product
documentation/evidence, bank mappings, non-functional constraints, target state,
and decision criteria.

**Conceptual flow:**

1. The bank defines the capability scope and decision being made.
2. Vendor/product claims are mapped to BIAN concepts with source and claim owner.
3. Evidence quality and granularity are assessed.
4. The proposed coverage is compared with the bank's current implementations and
   target responsibilities.
5. Gaps, overlap, dependencies, integration needs, and exit implications are
   highlighted.
6. Bank reviewers approve, challenge, or qualify mappings for the decision.

**Outputs:** coverage and gap map, overlap analysis, evidence quality, integration
and dependency considerations, assumptions, and decision comparison views.

**Decisions enabled:** shortlist, fit-gap focus, replacement scope, negotiation
questions, coexistence strategy, and exit planning.

**Trust and safety rules:** vendor claims are not independently verified facts.
Coverage does not prove product quality, implementation readiness, or contractual
commitment. Commercially sensitive data requires appropriate controls.

**Success signals:** more precise RFP/due-diligence questions; identified gaps and
overlap; less subjective comparison; traceable sourcing decisions.

---

## UC-13 — Embed BIAN-informed architecture governance into change delivery

**Original idea:** automatically assess new project/service proposals for likely
domain, duplication, ownership, and data concerns.

**Primary actors:** solution architect, architecture review board, enterprise
architect, project team, API owner, data owner.

**Desired outcome:** identify material architecture concerns early and give
reviewers relevant estate context without automating away human accountability.

**Initiating event:** new initiative, design submission, API proposal, service
registration, major change, or architecture exception request.

**Required inputs:** proposal scope and design, candidate responsibilities/data,
existing landscape, target-state rules, ownership, existing services/APIs,
accepted mappings, policies, and exceptions.

**Conceptual flow:**

1. A project submits structured design information or links existing artefacts.
2. The platform suggests likely BIAN responsibilities and relevant existing assets.
3. It checks for potential duplication, misplaced data ownership, target-state
   conflicts, missing owners, and policy concerns.
4. Findings show evidence, severity rationale, and uncertainty.
5. The project responds; accountable reviewers accept, reject, request change, or
   grant a time-bound exception.
6. The decision updates the model and future governance context.

**Outputs:** review pack, relevant existing capabilities/assets, explainable
findings, decisions, remediation actions, exceptions, and audit trail.

**Decisions enabled:** approve, modify, reuse, consolidate, escalate, or grant an
exception with explicit rationale.

**Trust and safety rules:** a similarity flag is not proof of duplication. Policy
checks must show the rule and evidence. Final authority remains with designated
reviewers.

**Success signals:** issues found earlier; fewer duplicate services; faster review
for well-aligned proposals; decisions and exceptions remain visible.

---

## UC-14 — Measure and communicate BIAN adoption

**Original idea:** BIAN adoption scorecard for executives and architects.

**Primary actors:** Chief Architect, CIO/CTO, transformation director, enterprise
architect, portfolio owner, architecture governance lead.

**Desired outcome:** understand adoption progress, quality, risk, and realised
change without relying on a misleading headline percentage.

**Initiating event:** executive review, quarterly planning, transformation
governance, architecture health review, or adoption programme checkpoint.

**Required inputs:** scope definition, mapping coverage and review state,
ownership, alignment findings, duplicates, lifecycle, target states, governance
decisions, remediation, control evidence, and historical baselines.

**Conceptual flow:**

1. The viewer selects organisational, functional, or programme scope.
2. The platform presents multiple adoption dimensions and their definitions.
3. Metrics distinguish inventory coverage, mapping confidence, reviewed
   alignment, ownership, duplication, target-state definition, remediation, and
   evidence—not one opaque score.
4. Trends and material hotspots are highlighted.
5. Users drill into the underlying assets, findings, owners, and data-quality gaps.
6. Decisions and actions are recorded through governance or transformation work.

**Outputs:** dimensional scorecard, trends, hotspots, data-quality indicators,
targets, ownership, and drill-down evidence.

**Decisions enabled:** where to invest, which areas need review, whether adoption
is changing architecture outcomes, and what should be escalated.

**Trust and safety rules:** every metric needs a definition, scope, denominator,
date, and data-quality indicator. “Unmapped” must not automatically mean “bad,”
and higher alignment must not automatically mean greater business value.

**Success signals:** leaders use the scorecard to make specific decisions; metrics
are stable and explainable; teams improve underlying quality rather than gaming a
single score.

---

## Cross-use-case requirements

The following are product requirements even before they become architecture:

- version and provenance for all consequential information;
- explainable inference with evidence and confidence;
- human review, correction, rejection, and exception workflows;
- explicit scope and limitations for scores and assurance;
- separation between external framework, customer truth, inference, and evidence;
- support for current, target, and historical states;
- change/decision history and accountable ownership;
- open import/export boundaries so the product does not become another isolated
  architecture repository;
- protection of sensitive topology, security, commercial, and ownership data;
- graceful handling of incomplete and contradictory customer information.

