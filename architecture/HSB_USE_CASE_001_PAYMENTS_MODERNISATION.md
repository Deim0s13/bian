# HSB-UC-001: modernise a fragmented payments estate using BIAN

## Document status

**Status:** Initial bank-led use case under `WRK-012`

**Use-case version:** `HSB-UC-001/v0.2`

**Governing decision:** `DEC-034`

**Evidence standing:** Project-authored synthetic banking context. It is not
evidence of a real bank, customer demand, BIAN alignment, regulatory compliance
or a preferred target architecture.

### Change history

| Version | Standing | Change |
|---|---|---|
| `v0.1` | Initial bank-led use case | Established the bank problem, five journeys, mixed-generation estate, evidence boundary, BIAN adoption questions and neutral option space |
| `v0.2` | Banking-realism refinement | Adds the clearing and settlement boundary, returns and recalls, party, account and payee information, AML monitoring, dated forcing functions, out-of-scope cross-border constraints, limits the platform cannot remove, an explicit realism disclaimer and separately named BIAN-blocked and BIAN-informed assessment outputs |

## 1. Purpose

This use case describes a credible problem that an established bank could bring
to the BIAN Adoption & Engineering Platform. It begins with the bank's
fragmented payments estate and its need to understand, rationalise and
modernise that estate. It does not begin with a platform feature or a
preselected architecture outcome.

The use case asks whether source-qualified BIAN context and reviewed bank-estate
evidence can help Horizon Synthetic Bank (HSB) establish a common architectural
language, expose gaps and duplication, evaluate target choices and plan a safe
transition.

The existing
[customer-payment initiation responsibility scenario](HSB_SCENARIO_001_PAYMENTS_RESPONSIBILITY.md)
is a subordinate validation thread. It tests one contested decision within this
broader adoption assessment and is not the customer use case by itself.

## 2. Claim and source boundary

HSB, its history, participants, systems, interfaces, incidents, pressures and
outcomes are fictional. The scenario deliberately resembles the conditions of
an established bank without claiming that a particular bank has this estate or
would make the same decisions.

### Realism disclaimer

This use case is the project's best current attempt to create a credible
incumbent-bank payments scenario from architecture experience, research and
review. It is not an empirical reconstruction of a named bank and should not be
treated as complete or representative of every institution. Real banks differ
by market, scheme participation, products, history, operating model,
regulation, technology, controls and organisational constraints. Missing or
simplified concerns are therefore expected.

An omission does not mean that a concern is unimportant, that BIAN does not
address it or that the future platform supports it. HSB tests the internal
coherence, boundaries and behaviour of the proposed architecture. Any adopting
bank would need to establish fitness against its actual estate, authoritative
BIAN sources, jurisdiction, obligations and decision context.

No name in this document is a BIAN term unless an authorised, release-qualified
BIAN source later establishes that attribution. Exact BIAN Service Domains,
Business Capabilities, Business Scenarios, Business Objects, Service Operations
and relationships remain unresolved until source qualification and rights
review pass their governing gates.

BIAN is used as a banking reference framework. This use case does not assume:

- that one application should correspond to one BIAN Service Domain;
- that every Service Domain has a published BIAN API specification;
- that alignment requires identical implementation across banks;
- that a modern API proves sound responsibility boundaries; or
- that BIAN alone determines the bank's target architecture.

## 3. Horizon Synthetic Bank context

HSB is a medium-sized retail and business bank. Its payments estate has evolved
through product growth, acquisition and successive integration programmes.
The bank serves personal customers, small and medium businesses and a smaller
corporate segment through digital and assisted channels.

The current estate reflects several generations of change:

- the primary retail core remains central to account state and posting;
- an acquired business bank retains a separate core and payment engine;
- mobile and online channels use newer APIs for selected journeys;
- business customers use file, portal and API initiation routes;
- branch and contact-centre users retain assisted payment paths;
- a payment orchestration hub supports only part of the estate;
- adapters, integration middleware and batch exchanges bridge newer and older
  platforms;
- domestic clearing connectivity, settlement positions, returns and scheme
  reconciliation have evolved separately from customer-facing payment change;
  and
- payment operations rely on repair, reconciliation and manual intervention
  outside the main digital path.

This is not intended to model every bank or every payment type. It provides a
bounded but recognisable incumbent-bank context in which responsibility,
information and modernisation decisions are genuinely difficult.

## 4. Transformation trigger

HSB has commissioned a payments architecture assessment after several
synthetic pressures converged:

1. vendor support for the acquired payment engine's current release and its
   proprietary domestic scheme connector ends on 30 September 2027;
2. payment scheme and message changes must be implemented repeatedly across
   different processing paths;
3. business and digital product teams want faster, consistent payment change;
4. recent incidents exposed incomplete end-to-end ownership and difficult
   operational diagnosis;
5. operations teams report avoidable repair and reconciliation work; and
6. earlier programmes introduced a payment hub without establishing whether it
   should become the strategic responsibility holder for every journey.

HSB needs an accepted target direction and first transition scope by 31 March
2027 to enter its next funding cycle. Deferral beyond that date requires an
explicit support exception, contract extension and scheme-change contingency.
No-change remains a valid option, but it is not cost-free.

The HSB transformation sponsor has not approved a replacement programme,
vendor, deployment model or preferred hub strategy. The assessment must first
establish what the estate does, how it relates to source-qualified BIAN context,
where the structural problems lie and which choices are defensible.

The initiating question is:

> How should HSB rationalise and progressively modernise its domestic
> account-to-account payments estate using source-qualified BIAN context,
> reviewed estate evidence and explicit operational constraints?

## 5. Scope and boundaries

### In scope

- personal and business domestic account-to-account payments;
- immediate, future-dated, scheduled and business bulk initiation;
- mobile, online, business API or file, branch and contact-centre channels;
- initiation, validation, fraud and sanctions dependencies, orchestration,
  routing, account posting, status, exception handling and reconciliation;
- applications, APIs, messages, files, integrations, information concepts,
  owners, lifecycle and operational dependencies that affect those journeys;
- current-state understanding, BIAN mapping, gap and duplication analysis,
  target options and transition sequencing; and
- change impact against the accepted HSB and BIAN context.

### Outside the first assessment

- card acquiring and issuing;
- cash, ATM, securities and lending transactions;
- detailed cross-border, foreign-exchange and correspondent-banking design;
- redesign of clearing or settlement schemes outside HSB;
- production transaction or personal data;
- solution products, deployment topology and implementation technology; and
- a claim that the assessment covers the complete bank.

An out-of-scope element remains visible when it creates an in-scope dependency.
It is not silently removed from the architecture view.

The subjects and journeys in sections 6 and 7 are the scope ceiling for the
first assessment. A newly noticed concern is recorded as an exclusion,
dependency or evidence gap rather than causing another estate subject to be
added, unless it is required to decide an existing in-scope question and the
scope change is explicitly accepted.

The Acquired Corporate Payments Engine also supports cross-border and
correspondent functions outside this assessment. HSB cannot retire the engine
as one undifferentiated unit unless a later scope supplies a replacement for
those functions. This retained dependency constrains domestic target choices
without bringing detailed cross-border design into scope.

## 6. Current payment journeys

| Journey | Current path | Known concern |
|---|---|---|
| `HSB-PJ-001` Personal digital payment | Mobile or online channel to Payment Initiation Gateway, partial orchestration through the Payment Orchestration Hub, legacy translation, primary core posting and Domestic Clearing Gateway | Validation and fraud sequencing differ between records; the Hub covers only selected payment routes; scheme status is translated more than once |
| `HSB-PJ-002` Business single or bulk payment | Business portal, file or API route to the Acquired Corporate Payments Engine, acquired business core and its scheme-facing path | Separate instruction, status, validation and scheme-message models duplicate parts of the retail path |
| `HSB-PJ-003` Assisted payment | Branch or contact-centre platform to core-facing services and legacy integration | The path bypasses parts of the newer payment layer and ownership is split across channel, core and operations teams |
| `HSB-PJ-004` Scheduled payment | Stored instruction and scheduled execution within a core-led path | Schedule ownership and execution status are poorly connected to the newer orchestration view |
| `HSB-PJ-005` Exception and repair | Failed or unmatched instructions pass to operations and reconciliation tools through messages, files and manual work queues | The initiating journey, repair action and final outcome cannot always be reconstructed from one source |
| `HSB-PJ-006` Return, recall or reversal | A customer, operations user or domestic scheme initiates a post-submission change that crosses the scheme gateway, payment engine or Hub, core, operations and channel paths | Ownership, permissible state change, customer status, settlement consequence and cut-off handling differ by route |

The journeys are HSB assertions. They are not represented as BIAN Business
Scenarios until exact authorised sources support that classification and
meaning.

## 7. Synthetic estate baseline

The estate deliberately combines modern and legacy elements. Lifecycle labels
are HSB portfolio assertions, not product recommendations.

| Subject ID | Synthetic asset | Current role | Accountable HSB area | Lifecycle at baseline |
|---|---|---|---|---|
| `SUBJ-HSB-APP-040` | Mobile and Online Banking | Personal customer initiation and payment status | Digital Channels | Strategic |
| `SUBJ-HSB-APP-041` | Business Banking and File Gateway | Business portal, API and bulk-file initiation | Business Banking | Maintain |
| `SUBJ-HSB-APP-042` | Payment Initiation Gateway | Channel validation and request translation for selected digital journeys | Payments Platform, disputed by Digital Channels | Maintain |
| `SUBJ-HSB-APP-043` | Payment Orchestration Hub | Instruction state, idempotency and routing for part of the retail estate | Payments Platform | Strategic, later challenged |
| `SUBJ-HSB-APP-044` | Legacy Payment Adapter | Translation and core submission with retained duplicate validation | Core Banking Integration | Contain |
| `SUBJ-HSB-APP-045` | Core Account Processing | Primary account state, scheduled instructions and posting | Core Banking | Maintain |
| `SUBJ-HSB-APP-046` | Fraud Decision Service | Fraud assessment used at different points across payment paths | Financial Crime | Strategic |
| `SUBJ-HSB-APP-047` | Customer Identity and Access Service | Customer authentication and digital identity context | Digital Identity | Strategic |
| `SUBJ-HSB-APP-048` | Acquired Corporate Payments Engine | Business payment validation, batching, routing and status, plus retained cross-border and correspondent processing outside the first assessment | Business Payments | Replace under review |
| `SUBJ-HSB-APP-049` | Acquired Business Core | Business account state and posting | Business Core Banking | Contain |
| `SUBJ-HSB-APP-050` | Sanctions Screening Service | Sanctions assessment invoked differently by payment route | Financial Crime | Maintain |
| `SUBJ-HSB-APP-051` | Payment Operations Workbench | Repair, release, investigation and manual intervention | Payment Operations | Maintain |
| `SUBJ-HSB-APP-052` | Reconciliation and Repair Service | End-of-cycle reconciliation, unmatched-item management and outcome reporting | Finance Operations | Maintain |
| `SUBJ-HSB-APP-053` | Branch and Contact Centre Platform | Assisted payment capture and servicing | Customer Operations | Maintain |
| `SUBJ-HSB-APP-054` | Enterprise Integration Platform | Message, file, routing and transformation services across several paths | Integration Platform | Contain |
| `SUBJ-HSB-APP-055` | Domestic Clearing Gateway | Scheme connectivity, message translation, acknowledgements, cut-offs, returns and recalls for the primary estate | Payment Infrastructure | Maintain |
| `SUBJ-HSB-APP-056` | Settlement Position and Scheme Reconciliation | Scheme settlement positions, settlement reporting and scheme-to-bank reconciliation | Treasury Operations | Maintain |
| `SUBJ-HSB-APP-057` | Customer and Party Information Platform | Shared customer and party identity and relationship reference for selected channels | Customer Information | Strategic |
| `SUBJ-HSB-APP-058` | Payee and Beneficiary Management | Payee registration, verification state and customer-maintained beneficiary information for selected channels | Digital Banking | Maintain |
| `SUBJ-HSB-APP-059` | AML Transaction Monitoring | Post-event transaction monitoring, investigation referral and case correlation | Financial Crime | Strategic |

The six subjects used by `HSB-SCN-001/v0.2` remain a subset of this estate.
Their existing pre-registration records are not rewritten by this broader
context.

### Information and reference dependencies

| Subject ID | Information dependency | Current custody and concern |
|---|---|---|
| `SUBJ-HSB-DATA-001` | Customer and party reference | The Customer and Party Information Platform supplies selected channels, while the acquired estate retains local party identifiers and relationship records |
| `SUBJ-HSB-DATA-002` | Account and product reference | The two cores remain authoritative for different account populations; downstream systems cache different subsets and use different identifiers |
| `SUBJ-HSB-DATA-003` | Payee and beneficiary reference | Payee and Beneficiary Management covers newer digital paths, while business and acquired channels maintain separate beneficiary records |
| `SUBJ-HSB-DATA-004` | Payment instruction and status | Gateway, Hub, acquired engine, cores and operations tools retain different instruction and state representations |
| `SUBJ-HSB-DATA-005` | Scheme message and settlement position | The Domestic Clearing Gateway and Settlement Position and Scheme Reconciliation component use scheme-facing formats that are not the same as channel or core representations |

These are HSB information subjects and custody assertions. They are not BIAN
Business Objects or semantic definitions unless later source qualification
establishes an exact relationship.

## 8. Evidence available to the assessment

HSB does not begin with one reliable architecture repository. The assessment
must reconcile information from sources with different purposes and authority:

| Synthetic source | Useful content | Known limitation |
|---|---|---|
| Application portfolio and CMDB | Application identity, support group, lifecycle and environment | Ownership fields mix technical support, business ownership and accountability |
| API catalogue | Newer interfaces, owners and selected consumers | Legacy messages, files and direct core interactions are incomplete |
| Integration catalogue | Message, file and platform connections | Batch schedules, manual hand-offs and invocation order are inconsistent |
| Architecture repository | Current and target diagrams, principles and earlier decisions | Some diagrams describe intended rather than implemented behaviour |
| Source repositories and interface documents | Contracts, schemas and selected implementation evidence | Coverage and documentation quality vary by system generation |
| Ownership register | Named owners and governance assignments | Several entries conflict with operational support records |
| Incident and problem records | Failure paths, recovery actions and recurring operational concerns | Records describe symptoms and may not establish structural cause |
| Operations procedures | Repair, reconciliation, release and escalation activity | Manual steps and local knowledge are not consistently versioned |
| Scheme specifications and certification records | Message, cut-off, acknowledgement, return and certification expectations | Scheme material has separate rights and version context; successful certification does not prove the complete HSB architecture |
| Vendor contracts and support notices | Support dates, exit conditions, licensed components and extension choices | Commercial interpretation requires authorised procurement and legal review |
| Workforce and delivery plans | Specialist availability, change capacity and programme dependencies | Plans are time-bound management assertions, not architecture facts |
| Control catalogue | Project-defined HSB control expectations and owners | It is not regulation, external assurance or evidence that controls operate |
| Authorised BIAN sources | Release-qualified reference content after source and rights approval | Exact first-scope content remains unavailable until `GAT-004` |

Source conflict and absence are assessment inputs. The platform must not resolve
them silently or turn an architecture opinion into an HSB fact.

## 9. Known symptoms and validation conditions

The synthetic estate contains conditions that a useful adoption assessment
should expose without being told the desired target answer:

| Condition ID | Planted condition |
|---|---|
| `HSB-COND-001` | Payment validation is repeated across channel, gateway, engine, adapter and core paths, with incomplete evidence about which repetition is required |
| `HSB-COND-002` | Payment initiation, orchestration, posting, status and repair responsibilities are divided differently across personal, business and assisted journeys |
| `HSB-COND-003` | Fraud and sanctions controls are invoked at inconsistent points |
| `HSB-COND-004` | AML Transaction Monitoring receives different event detail and timing from the personal and acquired-business paths |
| `HSB-COND-005` | Personal and business paths use different instruction, party, account, payee and status representations |
| `HSB-COND-006` | Payee and beneficiary management is duplicated across newer digital, business and acquired-channel paths |
| `HSB-COND-007` | Payment limits and funds checks are divided among gateways, engines and cores, and the evidence does not yet establish which allocations are deliberate |
| `HSB-COND-008` | Modern APIs coexist with messages, batch files, direct integration and manual hand-offs |
| `HSB-COND-009` | Application, API, operational and architecture ownership sources disagree |
| `HSB-COND-010` | The Payment Orchestration Hub appears strategic but does not support the complete in-scope estate and later receives an adverse lifecycle change |
| `HSB-COND-011` | The APP-048 application-level portfolio record says Replace under review, while its embedded domestic connector loses support and its retained cross-border functions have a different transition horizon; component-level lifecycle cannot be inferred from the application label |
| `HSB-COND-012` | Scheme formatting, cut-off, acknowledgement, return, recall, settlement position and scheme-reconciliation responsibilities are not expressed in the current digital architecture view |
| `HSB-COND-013` | Exception, repair and reconciliation responsibilities are weakly connected to the initiating payment journey |
| `HSB-COND-014` | Workload, resilience, failure-rate and transition-cost evidence is incomplete |

These conditions create testable ground truth for finding coverage. They do not
preselect which component survives, which responsibility moves or whether HSB
should centralise, federate, replace or retain a path.

### Constraints the platform cannot remove

The assessment must also carry constraints that architecture analysis can make
visible but cannot solve:

| Constraint | Synthetic HSB position | Consequence for the assessment |
|---|---|---|
| Vendor and commercial | The acquired engine has an exit charge before its contract breakpoint, while support for its current release and domestic connector ends on 30 September 2027 | Options must distinguish technical preference from the authorised commercial decision and cost evidence |
| Workforce | Three specialists hold most acquired-engine and scheme-connector knowledge, and the recruitment plan is not approved | A transition cannot assume skills or parallel delivery capacity that HSB does not have |
| Funding | The next transformation funding decision closes on 31 March 2027 | Deferral can miss the funding cycle and must carry that consequence rather than appear neutral |
| Operational calendar | Payment Operations prohibits high-risk migration during the synthetic year-end and peak-business windows | Sequencing must show the restricted period, coexistence and recovery implications |

The platform may connect these constraints to options, evidence, owners and
decisions. It cannot renegotiate a contract, create specialists, approve
funding or accept operational risk on HSB's behalf.

## 10. BIAN adoption assessment

The HSB architecture team needs the assessment to answer:

1. Which exact, authorised BIAN R14 artefacts provide the relevant reference
   context, and what does their publication state permit the platform to claim?
2. Which banking responsibilities are performed across the six payment
   journeys, and where are they currently implemented?
3. Which reviewed HSB assertions can be mapped to source-qualified BIAN
   concepts, with what evidence, uncertainty and review state?
4. Where does one application combine several banking responsibilities, and
   where do several applications implement overlapping responsibility?
5. Which responsibilities, interactions, owners or information concepts are
   missing, disputed or unsupported, including scheme, settlement, party,
   account, payee, limits, monitoring and post-submission change?
6. Where do APIs, messages and information structures align or diverge from the
   qualified BIAN context, without treating interface similarity as functional
   equivalence?
7. Which differences are justified HSB choices and which indicate accidental
   complexity, duplication, technical debt or unclear accountability?
8. Which target-state options are viable under operational, lifecycle,
   security, organisational, commercial, workforce, funding and evidence
   constraints?
9. What transition states allow HSB to change safely without hiding temporary
   duplication, coexistence, rollback or retained legacy responsibility?
10. Which mappings, decisions, assets, owners, controls and plans are affected
    when HSB evidence or the selected BIAN release changes?

An unanswered question remains an explicit gap. The assessment does not create
a BIAN mapping or bank fact merely to complete a view.

## 11. Assessment path and outcomes

The use case has two separately named execution outputs:

- `HSB-ASSESS-ESTATE-001` is the BIAN-blocked estate assessment. It may
  reconstruct current payment journeys, reconcile HSB sources, expose conflicts,
  gaps, duplication and ownership, and prepare candidate questions. It must not
  claim BIAN alignment, BIAN-derived gaps or a BIAN-informed target decision.
- `HSB-ASSESS-BIAN-001` is the BIAN-informed adoption assessment. It begins only
  after the exact source, release, intended use and rights position pass
  `GAT-004`. It may extend the accepted estate baseline with reviewed HSB-to-BIAN
  mappings, BIAN-informed findings, target choices and release-aware impact.

An estate-only run is a valid limited result, not a failed BIAN assessment. Its
output name, claim boundary and unresolved source dependency must remain visible
at every point of use.

| Stage | Bank activity | Required outcome |
|---|---|---|
| Establish scope | Confirm journeys, products, entities, decision authority, exclusions and evidence limits | A bounded assessment mandate |
| Qualify reference context | Select exact BIAN source and release content and decide permitted use | Source-qualified context or an explicit block |
| Reconstruct current state | Reconcile estate, interfaces, information, ownership, lifecycle, controls and operations | A reviewable current-state model with conflict and absence visible |
| Review mappings | Propose, contest, accept, reject or supersede HSB-to-BIAN mappings | Reviewed mapping set that remains an HSB assertion |
| Diagnose the estate | Identify fragmentation, duplication, gaps, mixed responsibility, control discontinuity and dependency | Evidence-backed findings with limitations and owners |
| Develop options | Compare retention, simplification, consolidation, federation, progressive replacement and no-change choices | At least two viable choices, including justified no change where relevant |
| Decide target and transition | Allocate target responsibilities and sequence intermediate states | Governed target and transition decisions, actions and unresolved matters |
| Connect delivery and assurance | Hand off approved context without implying implementation approval | Traceable specification, control and governance consequences |
| Maintain the decision | Reassess accepted records when HSB or BIAN context changes | Reconstructable history and owned impact review |

The customer outcome is not a generic BIAN alignment score. It is a defensible
and maintainable understanding of the estate, together with target and
transition decisions that show how BIAN informed them and where it did not.

The path above is intentionally compatible with `ADOPTION-KERNEL/v1` so the
use case can test whether the kernel is sufficient for this payments problem.
A pass cannot establish that every stage is necessary or that the kernel
generalises. The non-payment transferability probe can challenge generality and
expose missing or redundant structure, but one additional probe still cannot
prove necessity or universal support.

## 12. Neutral option space

The use case must allow combinations of these outcomes:

- retain a path and clarify its responsibility and interface contract;
- remove unjustified duplication while preserving required controls;
- federate common responsibility while allowing channel-specific behaviour;
- decouple the acquired engine's proprietary domestic scheme connectivity and
  consolidate it into the Domestic Clearing Gateway before deciding the wider
  engine future, while retaining its out-of-scope cross-border and
  correspondent functions;
- extend an existing asset only when evidence supports its target fitness;
- progressively replace an acquired or ageing component;
- introduce a new responsibility holder when existing assets are unsuitable;
- defer a change because evidence, operational risk or dependency is unresolved;
  or
- make no structural change and improve ownership, observability or governance.

The Payment Orchestration Hub is a candidate, not the presumed centre of the
target estate. Its later adverse lifecycle assertion must be capable of changing
an earlier decision without forcing a predetermined replacement answer.
Deferral and no change must state their support, contract, scheme, funding and
operational-calendar consequences rather than being treated as cost-free.

## 13. Participants and decision rights

| Participant | Contribution | Decision limit |
|---|---|---|
| Enterprise or payments domain architect | Leads the assessment, proposes mappings, findings and target choices | Cannot create BIAN truth or approve evidence outside delegated scope |
| Transformation sponsor | Sets business outcomes and funds accepted transition work | Funding preference does not determine semantic or architecture correctness |
| Payments Product owner | Owns customer and product outcomes affected by payment behaviour, service levels and migration | Cannot approve source meaning or override operational, control or architecture evidence |
| Application, API and service owners | Review estate assertions and own resulting actions | Ownership of one asset does not decide the end-to-end target |
| Payment Operations owner | Reviews exception, repair, reconciliation and recoverability consequences | Operational preference does not silently override architecture authority |
| Security and Assurance owners | Decide their scoped requirements, evidence and conclusions | Cannot claim general compliance or approve the target architecture |
| Bank information steward | Governs HSB source identity, quality, sensitivity, correction and conflict | Source precedence does not determine target design by itself |
| BIAN source steward and Source-rights reviewer | Qualify exact source meaning and permitted use | Cannot infer missing BIAN content or decide HSB architecture |
| Architecture decision authority | Accepts, rejects or reopens target and transition decisions within its mandate | Must retain contrary evidence, limitations and rejected options |
| Engineering owner | Accepts or returns a specification-level hand-off | Acceptance does not authorise implementation or close evidence gaps |

## 14. Measures and failure conditions

The first internal run should measure structure rather than claim realised bank
benefit:

- planted conflicts and gaps surfaced versus those present by construction;
- in-scope journeys and assets included, explicitly excluded or unresolved;
- proposed, contested, rejected, superseded and accepted mappings retained;
- duplicate and mixed-responsibility findings supported by reviewable evidence;
- records traversed to reconstruct a finding or decision;
- accountable ownership of decisions, actions and unresolved matters;
- completeness of downstream impact after a controlled change; and
- ability to export and reconstruct the bank-owned assessment without hidden
  platform state or restricted source content;
- correct separation of `HSB-ASSESS-ESTATE-001` from
  `HSB-ASSESS-BIAN-001`, including every prohibited claim and unresolved source
  dependency.

Time saved, commercial value, organisational adoption and decision quality
compared with current bank practice remain unverified until people who did not
design the scenario can exercise the frozen paths.

The use case must be narrowed, stopped or redesigned when:

- it requires invented or unauthorised BIAN meaning;
- the evidence cannot distinguish genuine overlap from justified variation;
- the platform merely recreates an enterprise architecture repository;
- maintaining the connected model costs more than the decision value it adds;
- the analysis assumes the preferred target rather than comparing viable
  alternatives;
- a BIAN-blocked estate result is presented as BIAN alignment or adoption
  evidence;
- the bank needs broad organisational participation before the primary user
  receives a useful outcome; or
- payments-specific concepts leak into the shared adoption kernel or logical
  platform responsibilities.

## 15. Relationship to the validation protocol

`HSB-SCN-001/v0.2` remains a mechanically protected, unexecuted design for one
customer-payment initiation responsibility decision. `DEC-033` still governs
its scenario-specific subject and protected blocks.

Under `DEC-034`:

- this use case is the primary bank narrative;
- the narrow responsibility-allocation decision becomes one possible finding
  and decision thread within the wider assessment;
- the pre-registered Hub hypothesis is not the expected outcome of this use
  case;
- the validation thread must inherit the estate and evidence boundaries defined
  here before execution; and
- any changed hypothesis or impact set requires a new recorded scenario version
  and must preserve the earlier pre-registration as history.

This separation prevents the bank problem from being shaped to make a platform
test pass while retaining the valuable deterministic, negative-path, change,
export and reconstruction mechanics already designed.

## 16. Completion state

`HSB-UC-001/v0.2` defines the bank-led use case and synthetic estate baseline.
It does not complete `WRK-012` and has not produced scenario evidence.

Before this use case can support `GAT-003`, the project must:

1. review the realism and internal consistency of the synthetic estate;
2. align a new version of the subordinate validation thread to this use case
   without rewriting its historical pre-registration;
3. qualify or explicitly block the exact BIAN source context;
4. instantiate and exercise the governed records, findings, options, negative
   paths, change and export;
5. record the result against the measures and stop conditions above; and
6. use the completed `HSB-TP-001/v0.1` information-level result to test reuse of
   the logical application responsibilities developed under `WRK-013`.

## References

- [Adoption scenario contract](ADOPTION_SCENARIO_CONTRACT.md)
- [HSB responsibility-allocation validation thread](HSB_SCENARIO_001_PAYMENTS_RESPONSIBILITY.md)
- [HSB customer-onboarding transferability probe](HSB_TRANSFERABILITY_PROBE_001_CUSTOMER_ONBOARDING.md)
- [Business Architecture](BUSINESS_ARCHITECTURE.md)
- [Information Systems Architecture](INFORMATION_SYSTEMS_ARCHITECTURE.md)
- [Fictional bank and synthetic validation policy](../product/FICTIONAL_BANK_AND_SYNTHETIC_VALIDATION.md)
- [Value proposition and validation strategy](../product/VALUE_AND_VALIDATION.md)
- [Architecture Register](../governance/ARCHITECTURE_REGISTER.md)
