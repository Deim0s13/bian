# Phase C gap and traceability analysis

## Document status

**Status:** Initial Phase C cross-domain baseline for review

**Scope:** Baseline-to-target gaps, Business-to-Information Systems traceability,
information-domain accountability and first-proposition depth

**Governing decision:** `DEC-024`

## 1. Purpose

This analysis makes the transition from Business Architecture to Information
Systems Architecture visible. It identifies the gaps that later feed Phase E,
shows which platform capabilities and value streams depend on each information
domain, and distinguishes first-proposition obligations from north-star scope.

The gap analysis also tests the value hypothesis. The proposed advantage is not
that the platform stores more architecture metadata. It is that an architect can
reconstruct a decision and its changing foundations without repeatedly joining
uncontrolled documents and systems by hand.

## 2. Phase C baseline-to-target gap analysis

| ID | Baseline condition | Target condition | Decision and value consequence | Related controls | Phase E consumption |
|---|---|---|---|---|---|
| `GAP-C-001` | BIAN context is obtained from separate sources with unresolved rights, release and integrity boundaries | Exact authorised BIAN assertions and deterministic projections retain release, rights, integrity and provenance | A reviewer can determine what BIAN actually supplied and which gaps remain unsupported | `REQ-002`; `DAR-002`, `DAR-005`, `DAR-023`; `GAT-004` | Source qualification and ingestion options, including user-supplied-source and no-ingestion paths |
| `GAP-C-002` | Applications, APIs and architecture records use unrelated identifiers and labels | Stable platform identity anchors retain every source-native identity and attributable identity relationship | The decision can relate records without merging or overwriting source truth | `REQ-005`; `DAR-001`, `DAR-002`, `DAR-011`, `DAR-028` | Identity-registration and later reconciliation work packages |
| `GAP-C-003` | Latest values are copied into diagrams or catalogues without preserving who asserted them | Source-qualified assertions retain authority, time, review, limitations and supersession | The architect can distinguish source statements, project context, customer decisions and inferences | `REQ-003`; `DAR-003`, `DAR-006`, `DAR-018`, `DAR-019` | Assertion capture, classification and review capabilities |
| `GAP-C-004` | Customer-to-BIAN interpretations are implicit or embedded in diagrams | Candidate, disputed, accepted, rejected and superseded relationship assertions retain rationale, evidence and decision history | Mapping disagreement becomes reviewable rather than hidden in notation | `BAR-003`, `BAR-004`; `DAR-007`, `DAR-008`, `DAR-012` | Mapping proposal and accountable review work packages |
| `GAP-C-005` | A decision's “current state” is reconstructed from whatever records are current when someone asks | Governed View Definitions and immutable materialisations retain policy, time, inputs, result and limitations | A decision can be defended against the exact view used at the time | `REQ-006`, `REQ-007`; `DAR-004`, `DAR-026` | View-selection, materialisation and decision-package options |
| `GAP-C-006` | Conflicting sources are resolved through undocumented precedence or manual judgement | Contradictions stay visible until an authorised decision records the selected assertion, alternatives and rationale | No silent winner is presented as bank or BIAN truth | `DAR-009`, `DAR-010`, `DAR-018` | Conflict routing and decision-right work packages |
| `GAP-C-007` | Lineage and change impact are manually reconstructed across separate repositories | Provenance links connect sources, mappings, decisions, projections, controls, evidence, owners and review actions within maintained scope | A changed foundation produces accountable review work instead of an unqualified impact claim | `REQ-006`, `REQ-018`; `DAR-004`, `DAR-020`, `DAR-024` | Connected impact analysis and ownership-notification options |
| `GAP-C-008` | Ownership fields, architecture approval and operational custody overlap or remain absent | Each governed record has one accountable owner and a distinct source, reviewer, decision right and custodian where needed | The user can route correction and impact without assuming that data ownership equals decision authority | `REQ-007`; `DAR-010`, `DAR-012`; domain-role matrix below | Stewardship, review and integration responsibility packages |
| `GAP-C-009` | Sensitive architecture metadata is exchanged without a consistent ownership, sensitivity or access reference | Governed records carry customer scope, sensitivity and access-policy references across trust boundaries | The HSB slice and later adopter integration can be minimised and protected deliberately | `REQ-009`; `DAR-014`; `OQ-034` | Trust-boundary and policy-enforcement options |
| `GAP-C-010` | Logical responsibilities for capture, validation, view selection, review, projection and impact are not defined | Application Architecture allocates each responsibility without changing information semantics | Data requirements can be validated against an operable responsibility model | `GAT-003`; `WRK-013`; `DEP-013` | Logical Application Architecture input before Phase E |
| `GAP-C-011` | Export and exit depend on undocumented platform state or inaccessible external content | A bounded portable set reconstructs customer-owned decisions and references rights-restricted dependencies | The customer can review, migrate and exit without the platform becoming the only interpreter | `REQ-014`; `DAR-016`; `OQ-035` | Export, integration and exit work-package options |
| `GAP-C-012` | The conceptual model is assessed through prose only | Record-level HSB examples, negative scenarios and later source-qualified examples expose contradictions and acceptance limits | Model confidence is evidence-qualified rather than inferred from documentation coherence | `REQ-010`; `WRK-035`; `EVD-011` | Validation experiments and stop conditions before build |

This table begins to address `EVD-007` by stating the connected information gap
and decision consequence. It does not establish differentiation against an
actual combination of BIAN, EA, CMDB, API, GRC and delivery tools. That evidence
gap therefore remains only partially addressed.

## 3. Information domain to platform capability matrix

`P` means the information domain is primary to the capability. `S` means the
capability consumes or contributes to the domain. A blank means no necessary
relationship has yet been identified.

| Information domain | PC-01 | PC-02 | PC-03 | PC-04 | PC-05 | PC-06 | PC-07 |
|---|---:|---:|---:|---:|---:|---:|---:|
| BIAN source context | P | S | S | S | S | S | S |
| Bank or HSB estate |  | P | S | S | S | S |  |
| Mapping and analysis | S | P | P | S | S | S |  |
| Architecture and transformation | S | S | P | S | S | S |  |
| Engineering projection | S | S | S | P | S | S | S |
| Assurance and evidence |  | S | S | S | P | S | S |
| Governance and operation | S | S | S | S | S | P | P |

The matrix demonstrates that the seven domains are not private stores for seven
capabilities. BIAN source context, Mapping and analysis, and Governance and
operation are shared across several capabilities. Future Application
Architecture must allocate one responsibility for each governed record family
and expose it through several capability journeys rather than copy it.

## 4. Information domain to value-stream matrix

| Information domain | VS-01 | VS-02 | VS-03 | VS-04 | VS-05 | VS-06 |
|---|---:|---:|---:|---:|---:|---:|
| BIAN source context | P | S | S | S | S | P |
| Bank or HSB estate |  | P | P | S | S | P |
| Mapping and analysis | S | P | P | S | S | P |
| Architecture and transformation |  | S | P | S | S | P |
| Engineering projection |  |  | S | P | S | P |
| Assurance and evidence |  |  | S | S | P | P |
| Governance and operation | S | S | S | S | S | P |

This mapping is a traceability hypothesis. `WRK-012` must exercise the relevant
path using actual HSB records before the shared-foundation claim is treated as
scenario evidence.

## 5. Information domain by role and authority matrix

The domain is a subject-area grouping, not a shared-owner shortcut. Each
governed record still has one accountable owner. External semantic authority,
project stewardship, decision rights and operational custody remain distinct.

| Information domain | External or source authority | Accountable project role | Required review or decision roles | Operational custody | Gap exposed |
|---|---|---|---|---|---|
| BIAN source context | Authorised, release-qualified BIAN source | BIAN source steward | Source-rights reviewer; Architecture owner for project use | Later source-ingestion responsibility | No independent BIAN reviewer or approved source inventory yet |
| Bank or HSB estate | Named bank source system; HSB synthetic source for current exercises | Bank information steward | Asset owner; Architecture owner; Security owner | External source owner plus later integration responsibility | Real-bank stewardship and correction routes remain unvalidated |
| Mapping and analysis | No external mapping authority; each assertion retains its own source | Architecture owner | BIAN source steward; Bank information steward; affected asset owner | Later analysis and review responsibilities | A reviewed customer mapping must not acquire BIAN authority |
| Architecture and transformation | Recorded bank or HSB architecture decision mandate | Architecture owner | Affected asset, security, assurance and transformation owners | Architecture repository or exported customer record | Real approving body and escalation path remain hypothetical |
| Engineering projection | Approved model inputs and engineering repository for adopted assets | Engineering owner | Architecture owner; Security owner; Operations owner | Engineering and delivery repositories | Generated output ownership is untested because implementation is not authorised |
| Assurance and evidence | External obligation source and named bank control owner | Assurance owner | Security owner; Information governance owner; scoped assessor | Declared GRC, evidence or project record system | No regulatory or bank assurance evidence exists |
| Governance and operation | Enterprise identity, policy and operational sources where present | Determined per record family: Operations owner, Open-source maintainer, Product owner or Architecture owner | Security owner and affected governance role | Platform or external operational system | The domain is too broad for one accountable role; `OQ-049` must determine whether Application Architecture partitions it |

The matrix refines the answered boundary in `OQ-017`. It does not prove that the
roles or source systems exist in a real adopter.

## 6. First-proposition depth

| Information domain | Required depth now | Reason |
|---|---|---|
| BIAN source context | Core boundary, source-qualified content pending | The proposition must distinguish exact BIAN context from a project placeholder even before import is lawful |
| Bank or HSB estate | Core | The decision depends on application, API, owner, lifecycle and dependency assertions |
| Mapping and analysis | Core | Candidate and reviewed relationships, contradiction and uncertainty are central to the decision |
| Architecture and transformation | Core | The outcome is a responsibility-allocation and transition decision |
| Engineering projection | Thin connected proof | One projection tests lineage and the generated-versus-owned boundary; broad generation is north-star scope |
| Assurance and evidence | Thin connected proof | One evidence path tests claim discipline; general regulatory or GRC capability is north-star scope |
| Governance and operation | Supporting foundation | Identity, review, ownership and audit are needed; a portal, scorecard and full operating model are north-star scope |

## 7. Data Architecture section scope

| Data Architecture section | Scope classification | Review implication |
|---|---|---|
| Sections 3 through 12 | First-proposition core | Must be exercised by the record-level example and connected HSB scenario |
| Section 13, sensitivity and tenancy | First-proposition minimum plus later bank-production depth | HSB needs explicit ownership and sensitivity; real residency and lifecycle policy remain deferred |
| Section 14, extension and schema evolution | Namespace boundary required now; schema-evolution workflow is north-star scope | Validate no invented BIAN semantics now; retain later compatibility work under `DAR-025` |
| Section 15, portable exchange | Bounded export required now; general interchange is later scope | Test decision reconstruction for HSB without inventing an enterprise standard |
| Section 16, HSB information slice | First-proposition core | Expected records and outcomes must be explicit before scenario evidence is claimed |
| Sections 17 through 20 | Governance and review controls | Apply to current work; unresolved implementation concerns remain registered rather than treated as validated |

## 8. Phase E hand-off boundary

Phase E may later consume the gaps in this document only after the relevant
Phase C gates pass. A gap is not automatically a software feature or work
package. Phase E must compare integration, reuse, project contribution,
acquisition, bounded experiment, implementation, narrowing and no-build options.

`GAP-C-010` is particularly important: unresolved Application Architecture
responsibilities cannot be disguised as a future implementation detail. They
must be resolved or explicitly bounded before a transition option is credible.
