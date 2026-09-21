# HSB-TP-001: customer onboarding and periodic-review transferability probe

## Document status

**Status:** Conceptually exercised transferability probe

**Probe version:** `HSB-TP-001/v0.1`

**Kernel baseline:** `ADOPTION-KERNEL/v1`

**Governing decisions:** `DEC-031`, `DEC-032`, `DEC-033`, `DEC-035`

**Evidence standing:** Project-authored synthetic architecture evidence. This
probe is not evidence of a real bank, customer demand, BIAN alignment,
regulatory compliance, implementation behaviour or production readiness.

## 1. Purpose

This probe tests whether the shared architecture developed for the BIAN
Adoption & Engineering Platform can support a structurally different adoption
problem without acquiring payment-specific semantics or responsibilities.

It is deliberately smaller than
[HSB-UC-001](HSB_USE_CASE_001_PAYMENTS_MODERNISATION.md). It is not a second
product proposition or an attempt to model an entire customer-lifecycle or
financial-crime function. Its only purpose is to challenge the reuse claim in
`REQ-026` and provide the transferability evidence required by `WRK-012` and
`GAT-003`.

## 2. Claim and source boundary

The probe concerns fictional customer onboarding and periodic review at Horizon
Synthetic Bank (HSB). All people, policies, records, applications, providers,
conflicts and decisions are synthetic.

The probe uses no production customer or personal data. Synthetic case IDs and
invented attributes are sufficient to exercise ownership, sensitivity,
provenance, review and change behaviour.

No exact BIAN concept, relationship or release assertion participates. The BIAN
scope is an explicit unresolved project placeholder until the exact authorised
source and intended use pass `GAT-004`. Therefore:

- no probe record is Class A or Class B;
- no current result is a BIAN mapping, alignment finding or adoption
  recommendation;
- absence of an API specification is explicit and does not block the estate-only
  architecture test; and
- `HSB-TP-ASSESS-BIAN-001` remains blocked.

Terms in this document describe the fictional bank unless a future
source-qualified revision attributes an exact term to BIAN.

## 3. Bounded bank problem

HSB operates separate onboarding paths for personal and business customers.
Successive programmes added channel automation, a customer master, screening
case management and local operational controls without establishing one
reviewed responsibility and evidence model.

An internal synthetic control review found that teams could not consistently
answer:

- which system and owner hold the current onboarding or periodic-review state;
- which evidence supported an identity, screening or approval decision;
- why two records showed different review dates or outcomes;
- which responsibilities were duplicated or absent; and
- which records and decisions would be affected by a policy change.

The accountable HSB architecture authority asks:

> How should HSB clarify and progressively improve the responsibility,
> information and evidence model for customer onboarding and periodic review,
> while retaining explicit uncertainty and preparing for later
> source-qualified BIAN assessment?

The decision is not to select an implementation product. It is to determine a
defensible target direction and first transition actions.

## 4. Probe contract

| Contract field | Probe position |
|---|---|
| Identity | `HSB-TP-001/v0.1`; owned by the Architecture owner; conceptually exercised on 21 September 2026 |
| Kernel baseline | `ADOPTION-KERNEL/v1`; all eleven stages participate |
| Purpose | Challenge domain transferability through a non-payment, non-API-dominant bank problem |
| Decision subject | `SUBJ-HSB-ONB-MODEL-001`, the scenario-specific onboarding and periodic-review responsibility and evidence model |
| Scope | Personal and business onboarding, identity and screening evidence, approval state, customer-master hand-off and periodic-review scheduling |
| BIAN context | `SUBJ-PRJ-BIAN-SCOPE-ONB-001`, an unresolved Class C placeholder; no Class A or Class B content |
| Source shape | HSB process, policy, portfolio, case, questionnaire and review records plus one third-party provider statement; no API specification participates |
| Customer context | Five synthetic HSB applications, one external provider and four planted contradictions or gaps |
| Decision rights | HSB enterprise architect proposes; source owners attest their records; Customer operations owner reviews operating impact; Financial crime control owner reviews the fictional control position; HSB architecture authority decides |
| Maintained scope | Named records in sections 5 and 6, their relationships, the decision view, selected option, actions and controlled change |
| Options | Retain and strengthen local controls; establish a federated responsibility and evidence model; or consolidate case management later after evidence justifies it |
| Expected outcome | Select the federated model as the synthetic first transition, retain consolidation as a later option and reject any claim of BIAN alignment |
| Trust paths | `TB-01` through `TB-07` and `TB-11`; no plugin, build, release or operator path participates |
| Measures | Sources reconciled, planted conflicts surfaced, records traversed for reconstruction, stages exercised and semantic diff result |
| Change | `HSB-TP-CHG-001`, a fictional periodic-review policy change with an explicit impact set |
| View provenance | `VIEWDEF-HSB-TP-001@1`, exact input versions, evaluation date, method version and limitations |
| Export boundary | `HSB-TP-OUT-001`, a customer-owned decision package excluding personal data and rights-restricted source content |
| Claim boundary | Internal evidence of conceptual reuse only; no universal-domain, BIAN-fidelity, real-bank or implementation claim |

## 5. Synthetic estate and source records

### 5.1 Applications and external participant

| ID | Synthetic estate subject | Current role asserted by HSB | Known limitation |
|---|---|---|---|
| `APP-060` | Retail Onboarding Portal | Captures personal-customer applications and supporting evidence references | Channel status is treated as onboarding status even when downstream review is incomplete |
| `APP-061` | Business Onboarding Workbench | Coordinates business-customer cases and manual approvals | Locally maintained states do not align with the customer master or screening case manager |
| `APP-062` | Customer Master and Relationship Platform | Holds customer identity and relationship records after approved creation | Portfolio records overstate its ownership of onboarding and periodic-review decisions |
| `APP-063` | Identity and Screening Case Manager | Records synthetic identity checks, screening cases and analyst outcomes | Provider result, analyst decision and retained evidence are not consistently distinguished |
| `APP-064` | Periodic Review Register | Schedules periodic reviews and tracks local completion | Spreadsheet-derived dates conflict with application and policy records |
| `EXT-020` | External Identity and Screening Provider | Supplies synthetic identity and screening result assertions | Provider statement does not establish HSB approval or retained decision evidence |

These are Class D HSB subjects and assertions except for `EXT-020` statements,
which are Class F. Registration of a subject does not prove the asserted role.

### 5.2 Source set

| ID | Source | Truth class | Limitation |
|---|---|---|---|
| `HSB-ONB-SRC-001` | Synthetic application-portfolio extract | Class D | Owner and lifecycle fields are six months old |
| `HSB-ONB-SRC-002` | Retail and business onboarding process pack | Class D | Approved diagrams omit local operational work queues |
| `HSB-ONB-SRC-003` | Fictional customer due-diligence and review policy | Class D | Project-authored HSB policy, not law, regulation or external guidance |
| `HSB-ONB-SRC-004` | Application-owner questionnaires | Class D | Owners disagree about responsibility boundaries |
| `HSB-ONB-SRC-005` | Synthetic case and periodic-review samples | Class D and evidence records | Contains invented case IDs only; sample cannot establish real frequency or harm |
| `HSB-ONB-SRC-006` | Provider capability and result-retention statement | Class F | Supplier assertion has not been independently verified |

### 5.3 Planted conditions

| ID | Condition present by construction | Required architecture response |
|---|---|---|
| `HSB-TP-COND-001` | `APP-060` is described as owning retail identity verification while `APP-063` and its owner assert that the screening case manager owns the review decision | Preserve both assertions and require an accountable decision; do not select a silent winner |
| `HSB-TP-COND-002` | `APP-062` is recorded as owning periodic-review outcomes, but its owner states that it receives only a completion status | Reject or narrow the portfolio relationship without changing either source record |
| `HSB-TP-COND-003` | `APP-063` and `APP-064` show different next-review dates for synthetic case `HSB-CUST-1042` | Surface the conflict, provenance and policy basis at the point of review |
| `HSB-TP-COND-004` | `EXT-020` reports a successful screening result but the retained HSB record lacks the provider configuration and analyst rationale needed to reproduce the approval | Keep the provider claim, evidence gap and HSB decision separate; do not convert success into verified approval evidence |

The planted-condition ground truth is known because the project authored the
contradictions. That supports structural counts, not claims about prevalence in
a real bank.

## 6. Estate-only paper execution

`HSB-TP-ASSESS-ESTATE-001` is a paper execution of the conceptual architecture.
It demonstrates record and decision behaviour without implying that software
exists.

### 6.1 Relationship lifecycle

The probe creates proposals at `AK-04`, contests them at `AK-05` and records an
accountable outcome at `AK-06`.

| Relationship record | Proposal | Conflict or evidence | `AK-06` outcome |
|---|---|---|---|
| `HSB-TP-REL-001` | `APP-060` currently owns retail identity verification | Contradicted by `APP-063` owner statement and case evidence | Rejected; portal captures input but does not own the review decision |
| `HSB-TP-REL-002` | `APP-063` currently records identity and screening review decisions | Provider results and analyst decisions are not consistently separated | Accepted with limitation and remediation action |
| `HSB-TP-REL-003` | `APP-062` owns periodic-review outcomes | Customer-master owner states it receives only status | Rejected; source records retained unchanged |
| `HSB-TP-REL-004` | `APP-064` is the authoritative source of next-review dates | Conflicts with `APP-063` for `HSB-CUST-1042` | Disputed pending policy-based correction; no winner selected |
| `HSB-TP-REL-005` | The HSB responsibility set maps to the unresolved BIAN scope placeholder | Exact BIAN source and relationship are absent | Blocked and explicitly not a BIAN mapping |

### 6.2 Current-state finding

The Class E finding is:

> HSB has no consistently evidenced responsibility and lifecycle model spanning
> onboarding capture, identity and screening review, customer-record creation
> and periodic review. Existing records support narrower local responsibilities,
> but ownership labels, state meanings, review dates and evidence claims conflict.

The finding is supported by all four planted conditions and retains the
limitation that no source-qualified BIAN comparison has occurred.

### 6.3 Neutral options and synthetic decision

| Option | Description | Principal benefit | Principal limitation |
|---|---|---|---|
| `HSB-TP-OPT-000` | Retain current applications and strengthen local reconciliation and control instructions | Lowest immediate change | Preserves duplicated states, manual reconstruction and unclear end-to-end ownership |
| `HSB-TP-OPT-001` | Establish a federated responsibility, state and evidence model across retained applications, with named owners and controlled hand-offs | Addresses the observed decision and evidence gaps without preselecting a replacement platform | Requires stewardship and integration work whose real effort is unvalidated |
| `HSB-TP-OPT-002` | Consolidate onboarding and periodic-review case management into a future common capability | May reduce duplicated workflow and state | Product, migration, operating-model and replacement evidence is insufficient |

`HSB-TP-DECISION-001` selects `HSB-TP-OPT-001` as the synthetic first
transition. It retains `HSB-TP-OPT-002` for later assessment and rejects neither
existing application nor provider by implication. The decision creates actions
to clarify responsibility, define shared state meaning, repair evidence lineage
and reconcile the disputed review date. It does not select technology or claim
BIAN alignment.

### 6.4 Kernel-stage outcome

| Stage | Probe execution | Outcome |
|---|---|---|
| `AK-01` | Record the bounded question, accountable authority, trigger, options and intended decision | Pass |
| `AK-02` | Record `SUBJ-PRJ-BIAN-SCOPE-ONB-001` as unresolved and prohibit BIAN attribution | Pass through explicit unresolved state |
| `AK-03` | Register the estate and six source records with authority, ownership, provenance and limitations | Pass |
| `AK-04` | Create five attributable relationship proposals without merging source assertions | Pass |
| `AK-05` | Surface four planted conditions, contrary evidence and unresolved uncertainty | Pass: four of four planted conditions surfaced |
| `AK-06` | Record accepted, rejected, disputed and blocked outcomes under the named decision authority | Pass |
| `AK-07` | Produce the estate-only finding through `VIEWDEF-HSB-TP-001@1` | Pass with BIAN limitation |
| `AK-08` | Compare no-change, federated and later consolidation options | Pass |
| `AK-09` | Select a synthetic first transition with rationale, owners and actions | Pass |
| `AK-10` | Produce `HSB-TP-OUT-001`, a governance and architecture decision package; no engineering artefact participates | Pass |
| `AK-11` | Apply `HSB-TP-CHG-001` and route every maintained dependant to impact review | Pass at paper-execution level |

All eleven stages participate. This exceeds the nine-stage floor without making
every future scenario exercise every stage.

## 7. View and reconstruction

`VIEWDEF-HSB-TP-001@1` is a Class C, scenario-specific View Definition. At the
evaluation date it includes:

- the six source records and their recorded versions;
- the estate subjects and source-native identifiers;
- all five relationship proposals and their lifecycle states;
- all supporting and contrary evidence for the four planted conditions;
- explicit unresolved BIAN scope;
- accepted, rejected, disputed and blocked outcomes; and
- the exact option and decision records.

It excludes personal data, unstated legal interpretation and any inferred BIAN
relationship. A reconstruction manifest lists the exact input versions,
evaluation date, method version, transformation result and limitations.

The structural measures are:

| Measure | Result | Limitation |
|---|---|---|
| Source records requiring reconciliation | Six | Project-authored scope, not a real-bank effort estimate |
| Planted conflicts or gaps surfaced | Four of four | Ground truth is synthetic |
| Relationship lifecycle states exercised | Proposed, accepted, rejected, disputed and blocked | Does not prove all future mapping shapes |
| Kernel stages exercised | Eleven of eleven | Conceptual paper execution only |
| Time-based effort | Deferred | The same author designed the probe and comparator, so a time comparison would not be credible |

## 8. Controlled change and impact

`HSB-TP-CHG-001` changes the fictional HSB policy on 1 April 2027 so that the
next review for the synthetic business-customer category containing
`HSB-CUST-1042` is calculated from a different interval. This is an HSB policy
change, not a regulatory claim.

The expected maintained impact set is:

- the superseded and replacement policy assertions from `HSB-ONB-SRC-003`;
- the conflicting next-review-date assertions for `HSB-CUST-1042`;
- `HSB-TP-REL-004` and its unresolved decision state;
- the current materialisation of `VIEWDEF-HSB-TP-001@1`;
- the related remediation action in `HSB-TP-DECISION-001`; and
- the current `HSB-TP-OUT-001` decision package.

Paper execution preserves the earlier decision view, marks the current
materialisation and dependant records for impact review, and produces no silent
date correction or retrospective change to the original evidence.

## 9. Trust and negative outcomes

| Test | Boundary | Expected non-success outcome |
|---|---|---|
| A case sample arrives without sensitivity classification | `TB-01`, `TB-02` | Retain an explicit Unclassified state, handle as restricted and block analysis or egress until reviewed |
| A portfolio owner attempts to approve the Financial crime control owner's decision | `TB-11`, `TB-05` | Deny the action without changing governed state; record the attempted scope |
| The provider statement is presented as verified HSB approval evidence | `TB-03`, `TB-04` | Fail point-of-use classification; retain it as Class F with the evidence gap visible |
| A file labelled as a BIAN onboarding model lacks qualified source context | `TB-01`, `TB-02` | Quarantine it and prohibit Class A or Class B creation |
| The decision package attempts to include synthetic case attributes that are unnecessary for reconstruction | `TB-06`, `TB-07` | Exclude the attributes and record the output-policy result |

These paths test different protected information and participants from the
payments scenario. They do not establish implemented security.

## 10. Structural variation result

The probe differs from the payments reference on all eight dimensions in the
contract, exceeding the required six. The four mandatory differences are
explicit.

| Dimension | Payments reference | Onboarding probe | Result |
|---|---|---|---|
| Banking context | Fragmented domestic payments modernisation | Customer onboarding and periodic review | Different |
| Primary decision | Estate diagnosis, target choices and payment transition | Responsibility and evidence model plus first operating transition | Different, mandatory |
| API dependence | APIs and integrations participate materially | No API specification participates | Different, mandatory |
| Mapping shape | Mixed-responsibility application and journey mappings | Accepted, rejected, disputed and blocked responsibility and evidence relationships | Different, mandatory |
| Source mix | Application, API, integration and operational payment records | Policy, process, portfolio, questionnaire, case, evidence and provider records | Different, mandatory |
| Participants | Payments architect, product, scheme, operations and application owners | Enterprise architect, Customer operations, Financial crime control, customer-data and application owners | Different |
| Downstream path | Payment target and transition consequences with later engineering potential | Governance and architecture decision package; no engineering projection | Different |
| Change | Estate or payment-source change | Fictional policy and evidence-validity change | Different |

## 11. Kernel semantic diff

The mechanical comparison covers the exact UTF-8 text inside and including the
named `adoption-kernel` domain-neutral boundary markers in the
[Adoption scenario contract](ADOPTION_SCENARIO_CONTRACT.md).

**Kernel block SHA-256:**
`998057efe99c8fabaadfdcaba6cdb7d00f41ed3d8c82c4f17e5a0e86da5f24dc`

**Semantic diff outcome:** Empty. The probe requires no new kernel stage,
behaviour, truth class, shared subject shape or payment-specific logical
responsibility. Its decision subject, View Definition, sources, conditions,
relationships, options, measures and policy change remain scenario-owned.

The repository check recomputes the canonical block digest and fails if this
record is no longer an exact comparison with the named kernel baseline.

## 12. Result and remaining work

At the scenario-contract and information-semantics level, the probe passes. It
provides evidence that `ADOPTION-KERNEL/v1` can represent one structurally
different, non-payment and non-API-dominant problem without semantic change.

It does not yet complete `WRK-012` or pass `GAT-003` because:

- the connected payments validation thread remains unexecuted;
- logical Application Architecture has not allocated `KB-01` through `KB-09`;
- reuse of those logical responsibilities by both scenarios therefore remains
  untested; and
- source-qualified BIAN fidelity remains blocked by `GAT-004`.

The probe now becomes a mandatory test input to `WRK-013`. A logical
responsibility that works only for payments, assumes an API input, or cannot
support this probe fails the Application Architecture review.

## References

- [Adoption scenario contract](ADOPTION_SCENARIO_CONTRACT.md)
- [Information Systems Architecture](INFORMATION_SYSTEMS_ARCHITECTURE.md)
- [Conceptual Data Architecture](DATA_ARCHITECTURE.md)
- [Trust-boundary and security architecture](TRUST_BOUNDARY_AND_SECURITY_ARCHITECTURE.md)
- [HSB payments-modernisation use case](HSB_USE_CASE_001_PAYMENTS_MODERNISATION.md)
- [Architecture Register](../governance/ARCHITECTURE_REGISTER.md)
