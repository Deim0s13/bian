# ADM tailoring statement

## Document status

**Status:** Initial tailored method baseline for review

**Scope:** Architecture method and work-product choices for the current
single-person, open-source concept stage

**Governing decision:** `DEC-025`

## 1. Purpose

This statement makes the project's TOGAF tailoring explicit. It distinguishes a
deliberate omission from an unfinished work product and prevents the amount of
documentation from becoming a proxy for architecture quality.

The project uses the TOGAF Standard as a method and viewpoint discipline. It
does not claim TOGAF conformance, reproduce protected templates or imply review
by The Open Group.

## 2. Tailoring principles

- Produce an artefact only when it answers a named stakeholder concern,
  supports a governed decision or supplies evidence for a canonical gate.
- Keep one authoritative record for status, ownership and decisions in the
  Architecture Register.
- Separate contextual explanation from governed records rather than duplicating
  the same catalogue across documents.
- Use original project formats suited to version-controlled Markdown.
- Preserve the distinction between architecture acceptance, build
  authorisation, implementation readiness and production-supported evidence.
- Tailor for one current project owner without presenting self-review as an
  Architecture Board or independent assurance.
- Revisit this tailoring when the project gains contributors, adopters,
  delivery teams, contractual obligations or a larger architecture landscape.

## 3. Work products produced

| Architecture concern | Project work product | Why this form is used |
|---|---|---|
| Project direction and stakeholder concerns | `ARCHITECTURE_VISION.md` | Supplies the Phase A direction, scope, constraints and stakeholder viewpoints without copying a TOGAF template |
| Business Architecture | `BUSINESS_ARCHITECTURE.md` | Connects value streams, project capabilities, business services, roles, information and the bounded proposition |
| Information Systems Architecture | `INFORMATION_SYSTEMS_ARCHITECTURE.md` plus the Data and later Application Architecture views | Keeps Phase C coordination visible while allowing Data and Application concerns to be reviewed separately |
| Architecture requirements | Architecture Register plus `REQUIREMENTS_AND_TRACEABILITY.md` | The register provides authoritative requirement status and ownership; the traceability view explains the model without duplicating the catalogue |
| Architecture decisions, risks and gaps | Architecture Register | Provides stable identifiers, canonical roles and gates, history and cross-record relationships |
| Phase C model validation | `PHASE_C_MODEL_VALIDATION.md` | Instantiates the conceptual model with synthetic records and records the resulting design decisions and limitations |
| Phase C gap and cross-domain analysis | `PHASE_C_TRACEABILITY.md` | Connects baseline-to-target gaps, Business Architecture capabilities, value streams, information domains, roles and proposition depth |
| Trust-boundary and security architecture | `TRUST_BOUNDARY_AND_SECURITY_ARCHITECTURE.md` | Makes protected information, trust changes, threats, abuse cases, failure behaviour, control outcomes and evidence limits explicit before the connected HSB scenario |
| Architecture lifecycle | `ARCHITECTURE_LIFECYCLE.md` | Plans Phase D through Phase H, continuous Requirements Management and ADM re-entry before those phases begin |
| Current status | `PROJECT_STATUS.md` | Provides a concise check-in without becoming a second decision or risk register |

## 4. Deliberately consolidated work products

| Common TOGAF work product | Project tailoring | Reason and revisit trigger |
|---|---|---|
| Architecture Definition Document | Federated across the Vision, Business, Information Systems, Data, later Application and Technology documents | One large document would duplicate governed content and make bounded review harder. Revisit only if a formal consumer requires a packaged baseline. |
| Architecture Requirements Specification | Architecture Register with the requirements-management view | One register retains wording, owner, status, gate, evidence and related records. Revisit if tooling can preserve the same single-source control. |
| Architecture Roadmap | Planned through Phase E and Phase F under `GAT-013` and `GAT-014` | A detailed roadmap before architecture gaps, options, resources and value evidence exist would create false precision. |
| Architecture Repository tooling | Version-controlled repository and checked Markdown | This is sufficient for the present scale. Revisit under `ASM-011` if relationship density, access or review effort becomes unmanageable. |
| Architecture Content Metamodel implementation | Project-defined register and traceability structures | A formal metamodel tool is not justified during conceptual work. The conceptual information model must remain portable to later tooling. |

## 5. Deliberately deferred or omitted work products

| Work product or mechanism | Current position | Revisit trigger |
|---|---|---|
| ArchiMate models | Deferred under `OQ-024` | A named viewpoint requires formal layered notation or impact analysis that current tables and Mermaid views cannot express clearly. |
| Architecture Contract | Not used before an external or separately accountable implementation party exists | Phase G identifies a delivery relationship requiring explicit conformance responsibilities and commitments. |
| Formal Architecture Board | Not represented by the current role catalogue | Multiple accountable participants exist and a proportionate decision forum is needed. Until then, `RSK-025` and `EVD-008` disclose the lack of independent challenge. |
| Detailed solution designs | Excluded before `GAT-006` and `GAT-007` | A bounded build is authorised and the Solution Architecture scope exists. |
| Physical data and deployment models | Excluded from current Phase C | Phase D and bounded Solution Architecture have approved requirements, workloads and evidence. |
| Procurement and contractual deliverables | Out of scope | Acquisition, commercial delivery or adopter commitments become real. |
| Detailed cost and resource plan | Deferred to Phase F | Credible ranges and delivery-capacity evidence exist under `GAT-014`. |

## 6. Governance and acceptance

The Architecture Register performs requirements control and architecture
governance throughout the lifecycle. Each work product references register
identifiers but does not maintain competing status or ownership.

The current Project owner also performs most specialist roles. A gate can fail
through unmet evidence and explicit failure conditions, but this does not make
the review independent. Independent conceptual review remains `DEP-008` and
`EVD-008` before build authorisation.

## 7. Iteration

This tailoring applies to the current architecture increment. Phase H may
trigger targeted revision or a further ADM cycle. The project revisits only the
affected phases unless the product purpose, stakeholders, scope or investment
basis has changed enough to require a new Architecture Vision.

Tailoring changes are governed architecture changes. They must record the
reason, affected work products, risks and consequences rather than silently
adding or removing ceremony.
