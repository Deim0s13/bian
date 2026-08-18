# Phase C model validation

## Document status

**Status:** Initial synthetic record-level pressure test

**Scope:** One HSB application, one HSB API, one contested responsibility, one
candidate relationship to a project-labelled BIAN scope placeholder, one
contradiction and one change

**Governing decision:** `DEC-024`

**Evidence limitation:** This is project-authored synthetic architecture
evidence. It does not validate an exact BIAN R14 artefact, relationship or
identifier and does not establish real-bank feasibility.

## 1. Purpose

This exercise instantiates the conceptual Data Architecture at record level. It
is designed to make ambiguities fail visibly before logical Application
Architecture or implementation is built on top of them.

The example is intentionally small and contradictory. It tests identity,
assertions, binary relationship assertions, source capture, provenance, review,
evidence, derived projection and reproducible current views.

## 2. Scenario boundary

Horizon Synthetic Bank is considering which application should hold a bounded
customer-payment initiation responsibility. The example uses the fictional
Payment Initiation Gateway and its Payment Initiation API.

The exact BIAN R14 element is deliberately unresolved. The record
`SUBJ-PRJ-BIAN-SCOPE-001` is a Class C project placeholder named “BIAN scope for
customer-payment initiation, exact element unresolved”. It is not a BIAN
Service Domain, Business Capability, Business Scenario or other BIAN artefact.
No candidate relationship in this exercise may be described as a BIAN mapping.

## 3. Entity and record type catalogue exercised

| Record type | Minimum conceptual attributes exercised | Role in this example |
|---|---|---|
| Subject | identifier, namespace, kind, registration reason, created time, ownership scope | Stable identity anchor for each thing or project placeholder |
| Assertion | identifier, subject, predicate, value or absence state, operational class, source, effective time, recorded time, review state, owner, limitations | Source claim about an HSB subject |
| Relationship assertion | identifier, left subject, relationship type, right subject, class, source or method, time, review state, rationale, limitations | Binary source relationship or candidate mapping |
| Source capture | identifier, source system, source-native record, snapshot, capture method, captured time, integrity state, rights, sensitivity | Immutable record of what the fictional source supplied |
| Provenance event | identifier, event type, inputs, outputs, method and version, actor, recorded time, result | Reconstructs import, normalisation and view creation |
| Review and decision | identifier, reviewed records, actor, decision mandate, outcome, rationale, recorded time, affected records | Prevents an inference or conflict from silently becoming accepted truth |
| Evidence | identifier, supported or challenged record, source, method, scope, result, reviewer, validity, limitations | Shows why the candidate relationship remains unverified |
| View definition | identifier, version, selection rules, parameters, conflict behaviour, owner, effective state | Governs how a current view is selected |
| Derived projection | identifier, projection kind, definition version, inputs, evaluation times, method version, result digest or snapshot reference, content classes, limitations | Reconstructable materialisation of the selected view |

These are conceptual attributes, not a physical schema or API contract.

## 4. Subject records

| Field | Application | API | Responsibility | BIAN scope placeholder |
|---|---|---|---|---|
| `record_id` | `SUBJ-HSB-APP-042` | `SUBJ-HSB-API-017` | `SUBJ-HSB-RESP-001` | `SUBJ-PRJ-BIAN-SCOPE-001` |
| `namespace` | `hsb:estate` | `hsb:estate` | `hsb:architecture` | `project:bianaep:placeholder` |
| `subject_kind` | `application` | `api` | `responsibility` | `unresolved_bian_scope_placeholder` |
| `display_label` | Payment Initiation Gateway | Payment Initiation API | Initiate customer payment instruction | BIAN scope for customer-payment initiation, exact element unresolved |
| `registration_reason` | Source-native identity `app-042` observed in HSB CMDB capture | Source-native identity `api-017` observed in HSB API catalogue capture | HSB architecture scope created for the decision | Project placeholder required to prevent invented BIAN attribution |
| `created_at` | `2026-08-18T09:05:00Z` | `2026-08-18T09:07:00Z` | `2026-08-18T09:15:00Z` | `2026-08-18T09:20:00Z` |
| `ownership_scope` | `HSB` | `HSB` | `HSB` | `project` |
| `asserts_real_world_existence` | `false` | `false` | `false` | `false` |

A Subject is a platform-minted identity anchor. Creating it asserts only that
the platform needs a stable referent. Whether a source recognises the subject,
whether it existed at a particular time, and whether two sources refer to the
same thing are separate assertions. This prevents an infinite regress while
keeping existence claims attributable.

## 5. Source captures

| Field | HSB CMDB capture | HSB API catalogue capture |
|---|---|---|
| `record_id` | `SC-HSB-CMDB-20260818-001` | `SC-HSB-API-20260818-001` |
| `source_system` | Horizon CMDB | Horizon API Catalogue |
| `source_native_record_id` | `app-042` | `api-017` |
| `source_snapshot` | `hsb://cmdb/snapshot/2026-08-18/v1` | `hsb://api-catalogue/snapshot/2026-08-18/v1` |
| `capture_method` | Synthetic CSV snapshot import | Synthetic JSON snapshot import |
| `captured_at` | `2026-08-18T09:00:00Z` | `2026-08-18T09:02:00Z` |
| `integrity_state` | `not_computed` | `not_computed` |
| `rights_class` | `HSB synthetic project data` | `HSB synthetic project data` |
| `sensitivity` | `HSB-INTERNAL-SYNTHETIC` | `HSB-INTERNAL-SYNTHETIC` |
| `limitations` | Deliberately incomplete owner and dependency data | API ownership may describe the API team rather than application accountability |

`not_computed` is an explicit absence state. The example does not fabricate a
digest or claim that an illustrative payload was integrity-verified.

## 6. Assertion records

| ID | Subject | Predicate | Value | Class | Source | Effective time | Recorded time | Review state | Limitation |
|---|---|---|---|---|---|---|---|---|---|
| `AST-HSB-001` | `SUBJ-HSB-APP-042` | `source_recognises_subject` | `true` | D | `SC-HSB-CMDB-20260818-001` | `2026-08-18` | `2026-08-18T09:05:00Z` | Unreviewed | Recognition by one synthetic source is not universal existence proof |
| `AST-HSB-002` | `SUBJ-HSB-APP-042` | `display_name` | Payment Initiation Gateway | D | `SC-HSB-CMDB-20260818-001` | `2026-08-18` | `2026-08-18T09:05:00Z` | Unreviewed | Source label may change |
| `AST-HSB-003` | `SUBJ-HSB-APP-042` | `accountable_owner` | Payments Platform Team | D | `SC-HSB-CMDB-20260818-001` | `2026-08-18` | `2026-08-18T09:05:00Z` | Unreviewed | CMDB owner field has no recorded decision mandate |
| `AST-HSB-004` | `SUBJ-HSB-API-017` | `source_recognises_subject` | `true` | D | `SC-HSB-API-20260818-001` | `2026-08-18` | `2026-08-18T09:07:00Z` | Unreviewed | Recognition is scoped to the API catalogue |
| `AST-HSB-005` | `SUBJ-HSB-API-017` | `accountable_owner` | Digital Channels Team | D | `SC-HSB-API-20260818-001` | `2026-08-18` | `2026-08-18T09:07:00Z` | Unreviewed | May represent interface support rather than application accountability |
| `AST-HSB-006` | `REL-HSB-001` | `relationship_context` | Customer-payment initiation decision `HSB-DEC-SCOPE-001` | C | Project method | `2026-08-18` | `2026-08-18T09:22:00Z` | Draft | Context vocabulary is project-defined |

`AST-HSB-006` demonstrates reification: a Relationship Assertion has stable
identity and may itself be the target of an assertion. The relationship remains
binary; context does not become an unqualified third endpoint.

## 7. Relationship assertion records

| ID | Left subject | Relationship | Right subject | Class | Source or method | Review state | Rationale and limitation |
|---|---|---|---|---|---|---|---|
| `REL-HSB-001` | `SUBJ-HSB-APP-042` | `provides` | `SUBJ-HSB-API-017` | D | HSB architecture assertion derived from both synthetic captures | Proposed | Source identifiers are consistent, but no asset-owner review has occurred |
| `REL-HSB-002` | `SUBJ-HSB-APP-042` | `currently_holds` | `SUBJ-HSB-RESP-001` | D | HSB architecture working assertion | Disputed | Ownership sources disagree and the responsibility boundary is project-defined |
| `REL-HSB-003` | `SUBJ-HSB-APP-042` | `candidate_mapping_to` | `SUBJ-PRJ-BIAN-SCOPE-001` | E | Project rule `candidate-map/v0.1` | Blocked | This is an inference to a project placeholder, not a BIAN mapping; exact BIAN source context is absent |

Every relationship has exactly two endpoints. Additional context is expressed
through identified context subjects or assertions about the reified
Relationship Assertion. Source, method, time and evidence remain metadata and
do not become semantic endpoints.

## 8. Evidence, review and provenance

### Evidence

| Field | Value |
|---|---|
| `record_id` | `EVID-HSB-001` |
| `supported_or_challenged_record` | `REL-HSB-003` |
| `method` | Manual record-level comparison of HSB responsibility wording with unresolved project scope |
| `scope` | Candidate relationship only |
| `result` | `insufficient` |
| `reviewer` | Architecture owner acting in self-review capacity |
| `valid_from` | `2026-08-18T09:30:00Z` |
| `valid_until` | `until exact authorised BIAN source scope is qualified` |
| `limitations` | No Class A BIAN assertion exists in the example; cannot support BIAN attribution or conformance |

### Review

| Field | Value |
|---|---|
| `record_id` | `REV-HSB-001` |
| `reviewed_records` | `REL-HSB-002`, `REL-HSB-003`, `EVID-HSB-001` |
| `actor` | Architecture owner |
| `decision_mandate` | HSB conceptual model review only |
| `outcome` | Keep ownership contradiction unresolved; block BIAN mapping acceptance |
| `rationale` | No accountable asset-owner decision resolves ownership and no authorised BIAN assertion establishes the target concept |
| `recorded_at` | `2026-08-18T09:40:00Z` |
| `affected_records` | Current view must show both ownership assertions and label `REL-HSB-003` as an unverified platform inference |

### Provenance events

| ID | Event | Inputs | Outputs | Method and version | Result |
|---|---|---|---|---|---|
| `PRV-HSB-001` | Capture and register CMDB subject | `SC-HSB-CMDB-20260818-001` | `SUBJ-HSB-APP-042`, `AST-HSB-001` through `AST-HSB-003` | `synthetic-import/v0.1` | Completed with missing integrity digest |
| `PRV-HSB-002` | Capture and register API subject | `SC-HSB-API-20260818-001` | `SUBJ-HSB-API-017`, `AST-HSB-004`, `AST-HSB-005` | `synthetic-import/v0.1` | Completed with ownership ambiguity |
| `PRV-HSB-003` | Propose relationship | Subject and assertion records above | `REL-HSB-001` through `REL-HSB-003` | `candidate-map/v0.1` | Candidate only; BIAN relationship blocked |

## 9. View definition and reproducibility

### Governed view definition

| Field | Value |
|---|---|
| `record_id` | `VIEWDEF-HSB-001` |
| `version` | `1` |
| `operational_class` | C, project extension |
| `purpose` | Present the records applicable to the HSB responsibility-allocation review without hiding contradiction |
| `effective_at_parameter` | Required |
| `recorded_at_parameter` | Required |
| `selection_rule_1` | Include records effective at the requested effective time and recorded no later than the requested recorded time |
| `selection_rule_2` | Exclude withdrawn records but retain their identifiers in historical lineage |
| `selection_rule_3` | Do not select a winning assertion when applicable assertions contradict unless a linked authorised decision resolves the exact conflict |
| `selection_rule_4` | Display operational class, source, review state and limitations at the point of use |
| `policy_representation` | Human-readable conceptual rules; executable representation remains `OQ-048` |
| `owner` | Information model steward |

### View materialisation before review

| Field | Value |
|---|---|
| `record_id` | `PROJ-HSB-VIEW-001` |
| `projection_kind` | `current_view_materialisation` |
| `record_class` | C, project-derived projection |
| `view_definition` | `VIEWDEF-HSB-001@1` |
| `effective_at` | `2026-08-18T00:00:00Z` |
| `recorded_at` | `2026-08-18T09:35:00Z` |
| `input_records` | `AST-HSB-001` through `AST-HSB-006`, `REL-HSB-001` through `REL-HSB-003`, `EVID-HSB-001` |
| `method_version` | `manual-model-evaluation/v0.1` |
| `result` | Application and API recognised by separate HSB sources; two different ownership statements remain visible; candidate relationship is blocked and explicitly not BIAN-attributed |
| `result_digest` | `not_computed` |
| `content_truth_classes` | D and E, with C context |
| `limitations` | Manual materialisation; no executable selection language or independent review |

A decision using this view must reference the materialisation, definition
version, evaluation times and exact input set. Re-running a later “current” view
is not sufficient evidence of what the earlier decision saw.

## 10. Change and contradiction test

At `2026-08-18T10:00:00Z`, a second synthetic API catalogue capture states that
the Payment Initiation API is supported by the Payments Platform Team. It
supersedes the API catalogue's earlier owner assertion but does not overwrite
it.

| New record | Meaning |
|---|---|
| `SC-HSB-API-20260818-002` | Immutable second API catalogue capture |
| `AST-HSB-007` | Class D owner assertion: Payments Platform Team, recorded at `2026-08-18T10:02:00Z` |
| `PRV-HSB-004` | Supersession link from `AST-HSB-005` to `AST-HSB-007`, preserving both |
| `PROJ-HSB-VIEW-002` | Materialisation using `VIEWDEF-HSB-001@1`, recorded at `2026-08-18T10:05:00Z` |

`PROJ-HSB-VIEW-001` remains reproducible with the old conflict. The later view
shows the new source state but does not retrospectively change the earlier
review. This distinguishes effective time, recorded time, supersession and view
reconstruction.

## 11. Model findings and decisions

| Finding | Resolution | Remaining limitation |
|---|---|---|
| Subject creation appeared capable of asserting existence | A Subject is a platform-minted identity anchor; source recognition and existence are assertions | Identity registration and deduplication responsibilities require Application Architecture |
| Class B and Derived Projection overlapped | A Derived Projection is a projection record. Class B applies only to a deterministic BIAN-derived projection. A claim made from a projection is a separate assertion linked by provenance. | Physical representation and interface shape remain open |
| Current-view selection had no governed home | Add View Definition and reproducible view materialisation concepts plus `DAR-026` | Executable policy representation remains `OQ-048` |
| Class C could display as inference or context | Class C always presents as Project context; Class E always presents as Platform inference | Product wording and all point-of-use views must use the corrected mapping |
| Relationship arity was open | A Relationship Assertion is binary. N-ary meaning uses identified context subjects or assertions about the reified relationship record | Query and indexing consequences remain for later design |

## 12. Validation outcome

The example supports the conceptual separation of Subject, Assertion, Source
Capture, Relationship Assertion, Review, Evidence and Provenance, but it does
not justify accepting the complete Data Architecture.

It found four required model clarifications and one new governed concept. It
also confirms that `DAR-010`, `DAR-011`, `DAR-014`, `DAR-019`, `DAR-020` and
`DAR-026` require logical Application Architecture responsibilities before
their acceptance evidence can be completed. Those requirements remain
Proposed.

The next validation should replace the BIAN placeholder with exact authorised,
release-qualified Class A content after `GAT-004`, then repeat the mapping and
view tests. Until then, `EVD-011` remains open.
