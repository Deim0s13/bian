# Architecture Register

## Purpose

This is the canonical control register for the BIAN Adoption & Engineering
Platform. It records the decisions, active questions, risks, assumptions,
dependencies, evidence gaps, architecture requirements, work items, and issues
that govern product and architecture progression.

Architecture and product documents may explain an item in context and reference
its identifier. They must not maintain a competing status, owner, resolution, or
decision. If a conflict exists, this register governs until the conflict is
resolved explicitly.

## Register rules

- Every governed record has a stable identifier that is never reused.
- The register retains resolved, closed, rejected, and superseded records.
- The accountable owner is a role until a named person or group is formally
  assigned.
- A record changes state only when evidence or an authorised decision supports
  the change.
- A document reference does not close or approve a record.
- Related records must reference each other where the relationship affects a
  decision or gate.
- Discovery prompts and scenario-review questions remain reusable research
  material. Promote one into this register only when it becomes an active
  project question, risk, requirement, evidence gap, or work item.
- Review affected records with every material architecture change and before
  each stage gate.

## Status vocabulary

| Record type | Permitted status |
|---|---|
| Decision | Accepted, Revisit required, Superseded |
| Open question | Open, In analysis, Answered, Deferred |
| Risk | Open, Mitigating, Accepted, Closed |
| Assumption | Untested, Supported, Invalidated |
| Dependency | Unmet, In progress, Met, Removed |
| Evidence gap | Open, Partial, Closed, Not obtainable |
| Requirement | Proposed, Accepted, Deferred, Rejected, Superseded |
| Work item | Planned, In progress, Blocked, Complete, Cancelled |
| Issue | Open, In progress, Resolved, Closed |

## Decisions

| ID | Date | Decision | Consequence | Revisit trigger | Owner | Status | Reviewed |
|---|---|---|---|---|---|---|---|
| DEC-001 | 2026-08-17 | Define the full use case before implementation or solution architecture. | Implementation was held while product discovery and architecture inputs were developed. | Owner closes the product-definition gate. | Project owner | Accepted | 2026-08-17 |
| DEC-002 | 2026-08-17 | Use Horizon Synthetic Bank and synthetic information as the repeatable validation environment. | No claim of customer demand or real-bank fit may be derived from synthetic results. | A future external validation model is authorised. | Project owner | Accepted | 2026-08-17 |
| DEC-003 | 2026-08-17 | Develop the project as independent open source. | Governance, contribution rights, source rights, support, and security processes are product requirements. | Rights review or sustainability evidence requires change. | Project owner | Accepted | 2026-08-17 |
| DEC-004 | 2026-08-17 | Attribute content to BIAN only when it is authoritative, release-qualified, and traceable. | Project extensions and inferences require separate classes and provenance. | Never for convenience; refine only with authoritative BIAN guidance. | Project owner | Accepted | 2026-08-17 |
| DEC-005 | 2026-08-17 | Treat production readiness as an evidenced release state. | Early work may be concept, experimental, or preview without weakening engineering expectations. | The readiness model is replaced by an approved evidence framework. | Project owner | Accepted | 2026-08-17 |
| DEC-006 | 2026-08-17 | Use TOGAF to guide architecture method and viewpoints and BIAN for banking reference content. | Architecture maintains stakeholder, requirements, domain, transition, and governance traceability while preserving the different roles of TOGAF and BIAN. | TOGAF tailoring or licensing review changes the approach. | Project owner | Accepted | 2026-08-17 |
| DEC-007 | 2026-08-17 | Align cloud-native architecture and engineering to the current CNCF definition and relevant authoritative CNCF guidance. Treat common practice lists as discovery inputs, not CNCF standards, and do not mandate microservices or Kubernetes for every component. | CNCF sources and versions must be traceable to project requirements and evidence. Deployment boundaries and platforms require an evidenced fit. | CNCF guidance changes or solution architecture supplies evidence for a narrower choice. | Project owner | Accepted | 2026-08-17 |
| DEC-008 | 2026-08-17 | Store durable project instructions and context in the repository. | Repository content is the source of truth across tools and sessions. | Repository governance changes. | Project owner | Accepted | 2026-08-17 |
| DEC-009 | 2026-08-17 | Do not use the Unicode em dash character in active project content. | Automated checks reject it and alternative punctuation is required. | Project owner changes the writing convention. | Project owner | Accepted | 2026-08-17 |
| DEC-010 | 2026-08-17 | Keep the initial technical spike archived and outside active design. | Its existing choices carry no product or architecture preference. It may be consulted only when a later, independently defined question makes it relevant. | Explicit review accepts a specific finding based on current requirements and new evidence. | Project owner | Accepted | 2026-08-17 |
| DEC-011 | 2026-08-17 | Accept the product definition as an evolving baseline and begin conceptual architecture with a TOGAF-informed Architecture Vision. Carry unresolved buyer, demand, rights, and operating-model matters as explicit hypotheses rather than waiting for final certainty. | Architecture may define conceptual requirements, viewpoints, information, boundaries, risks, and operating concerns. Implementation and solution technology remain out of scope. | Architecture Vision review identifies a material product contradiction, or the owner changes the stage. | Project owner | Accepted | 2026-08-17 |
| DEC-012 | 2026-08-17 | Define the product as the BIAN Adoption & Engineering Platform. Its north-star structure is BIAN Sources to BIAN Model Registry to the Service Generator, Adoption & Architecture, and Assurance & Compliance pillars, supported by Platform Control and Runtime Targets. No third-party BIAN API portal has architectural authority. | Active product and architecture work uses the platform's affirmative model-led definition and does not use another portal as a baseline, comparison point, constraint, or source of scope. | The project owner explicitly changes the product identity or north-star structure. | Project owner | Accepted | 2026-08-17 |
| DEC-013 | 2026-08-17 | Continue product discovery and conceptual architecture, but do not treat the full platform vision or an accepted Architecture Vision as build authorisation. Require a bounded proposition to demonstrate decision value, connected differentiation, feasible inputs, trust, adoption fit, sustainable scope, and explicit stop conditions. | Architecture may cover the full north-star, while future implementation approval is limited to the proposition supported by evidence. HSB cannot establish external desirability by itself. | Credible evidence passes the build-authorisation gate, a stop condition is reached, or the project owner changes the investment position. | Project owner | Accepted | 2026-08-17 |
| DEC-014 | 2026-08-17 | Develop the Business Architecture as the next conceptual work product after the initial Architecture Vision. Use value streams, project-defined platform capabilities, business services, organisation and information mapping, decision rights, measures, and an HSB business scenario to test how the platform creates value. | Business Architecture deepens the value proposition without selecting solution components or presenting project capabilities as BIAN Business Capabilities or Service Domains. | Review finds a material contradiction in the value model, terminology boundary, operating model, or Architecture Vision. | Project owner | Accepted | 2026-08-17 |
| DEC-015 | 2026-08-17 | Use this Architecture Register as the single canonical control record for decisions, active questions, risks, assumptions, dependencies, evidence gaps, architecture requirements, work items, and issues. | Context documents reference stable register identifiers. The former Decision Log and Open Questions files are compatibility pointers and hold no duplicate records. | The register becomes unmanageable or an approved governance design provides equivalent single-source control and traceability. | Project owner | Accepted | 2026-08-17 |

## Open questions

| ID | Question | Owner | Status | Required by | Source | Reviewed |
|---|---|---|---|---|---|---|
| OQ-001 | Which problem and bounded banking area should form the first product proposition? | Product authority | Open | Business Architecture review | Product definition; Business Architecture | 2026-08-17 |
| OQ-002 | Who is the first primary user, economic buyer, sponsor, operational owner, and approving authority? Are the leading BIAN lead, enterprise architect, domain architect, and architecture enablement hypotheses correct? | Product authority | Open | Business Architecture review | Product definition; Business Architecture | 2026-08-17 |
| OQ-003 | Which named decision will the product materially improve, and how will HSB demonstrate the before and after decision process? | Architecture authority | Open | Business Architecture review | Product definition; Business Architecture | 2026-08-17 |
| OQ-004 | What evidence can make the project useful and challenge external desirability without a real bank trial, while keeping demand and real-bank fit explicitly unvalidated? | Product authority | Open | Build-authorisation gate | Value validation; Business Architecture | 2026-08-17 |
| OQ-005 | What connected outcome cannot readily be achieved through authoritative BIAN tooling and established EA, API, GRC, generation, portal, and runtime tools? | Product authority | Open | Build-authorisation gate | Value validation; Business Architecture | 2026-08-17 |
| OQ-006 | What evidence would justify build authorisation for the first bounded proposition? | Product authority | Open | Build-authorisation gate | Value validation | 2026-08-17 |
| OQ-007 | Which result would cause the proposition to stop or materially narrow? | Product authority | Open | Business Architecture review | Value validation; Business Architecture | 2026-08-17 |
| OQ-008 | Which exact BIAN artefacts and releases are required by the first proposition? | BIAN source steward | Open | Source ingestion approval | BIAN and source rights | 2026-08-17 |
| OQ-009 | What rights permit import, transformation, redistribution, hosted use, and commercial use of each exact source? | Source-rights reviewer | Open | Source ingestion approval | BIAN and source rights | 2026-08-17 |
| OQ-010 | What project name and descriptive use of BIAN terminology are acceptable under trademark and affiliation constraints? | Source-rights reviewer | Open | Public release | BIAN and source rights | 2026-08-17 |
| OQ-011 | Who can provide competent BIAN conformance review before a public release? | Product authority | Open | Public release | BIAN and source rights | 2026-08-17 |
| OQ-012 | Which minimum bank information is available, maintainable, and sufficient for the selected decision? | Bank or HSB information steward | Open | Business Architecture review | Business Architecture | 2026-08-17 |
| OQ-013 | Which participant owns each mapping, architecture decision, engineering action, control conclusion, and change response? | Architecture authority | Open | Business Architecture review | Business Architecture | 2026-08-17 |
| OQ-014 | Which platform capabilities should be provided through integration with established tools rather than implemented by this project? | Architecture authority | Open | Application Architecture | Business Architecture | 2026-08-17 |
| OQ-015 | Which measures can distinguish decision value from increased documentation or feature activity? | Product authority | Open | Business Architecture review | Business Architecture | 2026-08-17 |
| OQ-016 | What level of stewardship and review effort is sustainable for an adopter, and who receives enough local value to perform it? | Product authority | Open | Operating-model review | Business Architecture | 2026-08-17 |
| OQ-017 | Which system owns each bank assertion and how will drift, conflict, and reconciliation be governed? | Architecture authority | Open | Information Architecture | Business Architecture | 2026-08-17 |
| OQ-018 | Is Apache License 2.0 appropriate after the complete rights inventory? | Open-source maintainer | Open | Public release | Open-source governance | 2026-08-17 |
| OQ-019 | Will contributions use a Developer Certificate of Origin, a contributor licence agreement, or another contribution-rights process? | Open-source maintainer | Open | Public contribution | Open-source governance | 2026-08-17 |
| OQ-020 | What maintainer, decision, Code of Conduct, security-reporting, support, and release processes are sustainable before the repository is publicised? | Open-source maintainer | Open | Public release | Open-source governance | 2026-08-17 |
| OQ-021 | Which public and private channels will handle vulnerabilities and sensitive reports? | Security owner | Open | Public release | Open-source governance | 2026-08-17 |
| OQ-022 | How should the TOGAF Standard, 10th Edition be tailored to this small project? | Architecture authority | In analysis | Conceptual Architecture completion | Architecture method | 2026-08-17 |
| OQ-023 | Which public TOGAF terminology and original project templates can be used without redistributing protected material or implying conformance? | Architecture authority | Open | Public release | Architecture method | 2026-08-17 |
| OQ-024 | Will ArchiMate be used for selected views, and which concerns would justify it? | Architecture authority | Deferred | Viewpoint requiring formal notation | Architecture method | 2026-08-17 |
| OQ-025 | Which architecture repository structure and traceability model will remain usable without creating documentation overhead? | Architecture authority | In analysis | Conceptual Architecture completion | Architecture method; DEC-015 | 2026-08-17 |
| OQ-026 | Which CNCF Technical Advisory Group publications and project guidance apply to the first proposition, and which are informative rather than requirements? | Architecture authority | Open | Solution Architecture | Engineering and assurance | 2026-08-17 |
| OQ-027 | What evidence model will demonstrate each applicable CNCF-derived quality without implying generic CNCF compliance or endorsement? | Architecture authority | Open | Solution Architecture | Engineering and assurance | 2026-08-17 |
| OQ-028 | Which quality attributes and measurable service objectives apply to the first deployable scope? | Product and architecture authority | Deferred | Solution Architecture | Engineering and assurance | 2026-08-17 |
| OQ-029 | Which languages, deployment boundaries, data stores, and integration patterns best satisfy approved requirements? | Architecture authority | Deferred | Solution Architecture | Engineering and assurance | 2026-08-17 |
| OQ-030 | Which checks, review roles, coverage measures, and complexity thresholds are proportionate once implementation begins? | Open-source maintainer | Deferred | Implementation approval | Engineering and assurance | 2026-08-17 |
| OQ-031 | What constitutes acceptable independent evidence for production-supported status in a bank environment? | Product and security authority | Open | Production-supported release | Engineering and assurance | 2026-08-17 |

## Risks

| ID | Risk | Consequence | Current response | Owner | Status | Affected gate | Reviewed |
|---|---|---|---|---|---|---|---|
| RSK-001 | BIAN source rights or terminology are misunderstood. | Invalid redistribution, misleading claims, or loss of trust | Maintain a source register, rights review, exact release provenance, and no invented semantics. | BIAN source steward | Open | Source ingestion approval | 2026-08-17 |
| RSK-002 | The vision becomes fourteen disconnected products. | Cost, duplication, and incoherent workflows | Use the shared BIAN Model Registry, three pillars, Platform Control, and connected validation scenarios. | Product authority | Open | Business Architecture review | 2026-08-17 |
| RSK-003 | A shallow feature is added to every platform block. | A broad demonstration solves no user problem well enough to adopt. | Validate one complete decision journey and deepen only the capabilities required by it. | Product authority | Open | Build-authorisation gate | 2026-08-17 |
| RSK-004 | Mature adjacent tools are recreated. | High delivery cost, weak differentiation, and poor enterprise fit | Complement or integrate EA, API, GRC, generation, portal, and runtime products unless evidence justifies implementation. | Architecture authority | Open | Application Architecture | 2026-08-17 |
| RSK-005 | The canonical model becomes a copy of OpenAPI or one BIAN artefact. | Later architecture and adoption uses become constrained. | Base the conceptual model on identity, assertion, relationship, provenance, review, and evidence. | Information architect | Open | Information Architecture | 2026-08-17 |
| RSK-006 | Automated mapping appears authoritative. | Unsafe decisions and rapid stakeholder distrust | Retain confidence, explanation, review, dispute, and explicit authority classes. | Architecture authority | Open | Business Architecture review | 2026-08-17 |
| RSK-007 | HSB becomes unrealistically clean. | Architecture passes tests that do not represent enterprise conditions. | Use contradictory, stale, incomplete, adversarial, and changing synthetic records. | HSB information steward | Open | HSB scenario approval | 2026-08-17 |
| RSK-008 | Security and assurance are treated as generated paperwork. | Weak controls and inflated compliance claims | Use threat-led design and requirement-to-evidence traceability with explicit gaps. | Security and control owner | Open | Assurance scope approval | 2026-08-17 |
| RSK-009 | Cloud-native becomes a product checklist. | Premature distribution, operational complexity, or platform coupling | Trace decisions to current CNCF guidance and measurable requirements. | Architecture authority | Open | Solution Architecture | 2026-08-17 |
| RSK-010 | Open-source ambition exceeds maintainer capacity. | Unsafe releases, slow response, and abandoned scope | Use narrow increments, explicit support status, automation, and sustainable governance. | Open-source maintainer | Open | Public release | 2026-08-17 |
| RSK-011 | An experience or vendor layer dictates the core. | Lock-in and distorted boundaries | Keep Platform Control separate from the BIAN Model Registry and use governed integrations. | Architecture authority | Open | Application Architecture | 2026-08-17 |
| RSK-012 | Architecture documentation becomes the product. | Slow learning and little validated value | Use every view to answer a decision and exercise it through HSB scenarios. | Architecture authority | Open | Every architecture review | 2026-08-17 |
| RSK-013 | Bank or HSB source data is incomplete, inconsistent, sensitive, or difficult to access. | Mapping and decision effort overwhelms potential value. | Bound the scope, model data quality and conflict, assign owners, and measure reconciliation effort. | Bank or HSB information steward | Open | Business Architecture review | 2026-08-17 |
| RSK-014 | API contracts and names are semantically insufficient for reliable BIAN alignment. | Poor explanations and false confidence undermine trust. | Require broader context, supporting evidence, uncertainty, and accountable review. | Architecture authority | Open | API-alignment proposition | 2026-08-17 |
| RSK-015 | Release-impact value depends on reviewed customer mappings that do not yet exist. | The use case has little bank-specific value as an initial proposition. | Treat release impact as a later connected outcome unless the required mapping baseline exists. | Product authority | Open | Proposition selection | 2026-08-17 |
| RSK-016 | Generated assets are adopted without clear ownership, boundaries, or target-architecture context. | Technical output creates duplication or misplaced responsibility. | Generate only from approved context and preserve ownership, lineage, and generated-versus-owned boundaries. | Engineering owner | Open | Engineering proposition | 2026-08-17 |
| RSK-017 | Assurance expands into unsupported regulatory interpretation or a general GRC product. | Liability, incorrect claims, excessive scope, and unsustainable expertise burden | Limit assurance to scoped evidence and integrate established standards and systems. | Security and control owner | Open | Assurance proposition | 2026-08-17 |
| RSK-018 | Adoption requires several organisational teams before any primary user receives value. | High coordination cost prevents adoption. | Design one consumable decision journey with local value and measure stewardship effort. | Product authority | Open | Build-authorisation gate | 2026-08-17 |

## Assumptions

| ID | Assumption | Validation or consequence | Owner | Status | Required by | Reviewed |
|---|---|---|---|---|---|---|
| ASM-001 | Connected HSB scenarios can create useful architecture learning before customer desirability is validated. | Exercise repeatable scenarios while preserving EVD-001. | Architecture authority | Untested | Business Architecture review | 2026-08-17 |
| ASM-002 | Authorised BIAN material will be available for the selected scope under compatible terms. | Resolve OQ-008 and OQ-009 before source ingestion. | BIAN source steward | Untested | Source ingestion approval | 2026-08-17 |
| ASM-003 | HSB can represent enough ambiguity and change to test enterprise concerns. | Design negative, conflicting, stale, and adversarial cases. | HSB information steward | Untested | HSB scenario approval | 2026-08-17 |
| ASM-004 | Human review remains acceptable for material mappings and recommendations. | Measure review effort and test OQ-016. | Product authority | Untested | Business Architecture review | 2026-08-17 |
| ASM-005 | Banks will prefer integration and export over replacement of established tools. | Test system-of-record boundaries and OQ-014. | Architecture authority | Untested | Application Architecture | 2026-08-17 |
| ASM-006 | Architecture can preserve deployment optionality until requirements mature. | Defer OQ-029 and avoid product-specific topology commitments. | Architecture authority | Supported | Solution Architecture | 2026-08-17 |
| ASM-007 | A federated stewardship model can keep bank assertions, mappings, decisions, and evidence current. | Test ownership, local incentives, backlog, and maintenance effort in HSB. | Architecture authority | Untested | Operating-model review | 2026-08-17 |

## Dependencies

| ID | Dependency | Why it matters | Owner | Status | Required by | Reviewed |
|---|---|---|---|---|---|---|
| DEP-001 | Complete the source-rights record for every BIAN artefact used. | No source may be imported, transformed, or redistributed on assumption. | Source-rights reviewer | Unmet | Source ingestion approval | 2026-08-17 |
| DEP-002 | Define coherent HSB scenarios and expected outcomes spanning the required platform capabilities. | Scenarios are the primary internal validation mechanism. | Architecture authority | In progress | HSB scenario approval | 2026-08-17 |
| DEP-003 | Define the conceptual information and provenance model. | The connected value thread depends on stable identity, authority, relationship, and history. | Information architect | Unmet | Information Architecture | 2026-08-17 |
| DEP-004 | Define identity, tenancy, sensitivity, retention, and evidence concepts. | Trust and bank-operating boundaries cannot be assessed without them. | Security and information authority | Unmet | Security and Information Architecture | 2026-08-17 |
| DEP-005 | Establish sustainable open-source licensing, contribution, security, and release governance. | Public adoption cannot rely on informal maintainer behaviour. | Open-source maintainer | Unmet | Public release | 2026-08-17 |
| DEP-006 | Obtain later review by people competent in BIAN, banking architecture, security, operations, accessibility, and open-source maintenance. | HSB and internal review cannot establish all required confidence. | Product authority | Unmet | Public or production-supported release | 2026-08-17 |

## Evidence gaps

| ID | Evidence gap | Why it matters | Owner | Status | Closure evidence | Reviewed |
|---|---|---|---|---|---|---|
| EVD-001 | No evidence yet establishes external desirability, buyer commitment, or willingness to maintain the platform. | HSB can test internal coherence but not market demand or real-bank adoption. | Product authority | Open | Qualified external feedback, independent usage, contribution, or later authorised stakeholder research | 2026-08-17 |
| EVD-002 | No evidence yet establishes the availability, quality, sensitivity, and maintenance cost of real bank inputs. | Input feasibility may make the proposition impractical. | Product authority | Open | Public evidence, qualified review, or later authorised real-world evidence with explicit limitations | 2026-08-17 |
| EVD-003 | The complete rights position is not established for all intended BIAN sources and uses. | Open-source distribution may be restricted or require a user-supplied source model. | Source-rights reviewer | Open | Artefact-level rights record and competent review | 2026-08-17 |
| EVD-004 | The federated stewardship operating model has not been shown to be sustainable. | Records may become stale or central teams may inherit unsustainable work. | Architecture authority | Open | HSB effort measures and later qualified operating-model review | 2026-08-17 |
| EVD-005 | No evidence establishes regulatory acceptance or the sufficiency of assurance outputs for a real bank. | Assurance claims could create legal, audit, or risk exposure. | Security and control owner | Open | Competent scoped review and later authorised adopter evidence | 2026-08-17 |
| EVD-006 | Production-supported evidence criteria are not yet defined or independently tested. | Production readiness cannot be asserted from intent. | Product and security authority | Open | Accepted readiness framework, tests, operational evidence, and independent review | 2026-08-17 |
| EVD-007 | Connected differentiation has not been demonstrated against a practical combination of existing tools. | The project may be integration glue without sufficient user value. | Product authority | Open | Reproducible comparison based on one end-to-end decision journey | 2026-08-17 |

## Requirements

These Business Architecture requirements are proposed. Acceptance requires
project-owner review and traceability to scenarios and evidence.

| ID | Requirement | Rationale | Owner | Status | Acceptance evidence | Reviewed |
|---|---|---|---|---|---|---|
| BAR-001 | Every bounded proposition shall name its primary user, trigger, decision, outcome, alternative, required inputs, evidence, and stop condition. | Prevent features from substituting for value. | Product authority | Proposed | Reviewed proposition record linked to OQ-001 through OQ-007 | 2026-08-17 |
| BAR-002 | The platform shall preserve a traceable thread from BIAN source through mapping, decision, engineering asset, assurance evidence, ownership, and change impact where applicable. | Establish connected differentiation. | Architecture authority | Proposed | HSB scenario demonstrates reproducible cross-capability traceability | 2026-08-17 |
| BAR-003 | BIAN-attributed content shall remain distinguishable from bank, HSB, project, external, derived, and inferred assertions. | Preserve semantic authority and trust. | BIAN source steward | Proposed | Negative and positive provenance tests in the selected scenario | 2026-08-17 |
| BAR-004 | Material mappings, architecture decisions, exceptions, and assurance conclusions shall have explicit human decision rights and recorded accountability. | Prevent unsafe automation and unclear ownership. | Architecture authority | Proposed | Organisation and decision-right view plus scenario approvals | 2026-08-17 |
| BAR-005 | The platform shall coexist with established systems of record through explicit ownership, reconciliation, import, and export boundaries. | Avoid unnecessary replacement and stale duplicate truth. | Architecture authority | Proposed | System-context and information-ownership views | 2026-08-17 |
| BAR-006 | A consumable proposition shall complete a meaningful user journey without project-developer intervention. | Test operability and real usefulness. | Product authority | Proposed | Independently executed HSB journey with recorded support required | 2026-08-17 |
| BAR-007 | Change analysis shall connect affected sources, mappings, decisions, assets, controls, evidence, and owners within the supported scope. | Convert maintained knowledge into actionable value. | Architecture authority | Proposed | Controlled HSB source and estate changes with expected impact results | 2026-08-17 |
| BAR-008 | Assurance outputs shall state assessed scope, version, method, evidence, findings, gaps, expiry, and responsible reviewer. | Prevent inflated compliance claims. | Security and control owner | Proposed | Scoped assurance scenario including explicit unverified areas | 2026-08-17 |
| BAR-009 | Generated assets shall remain disposable and separate from bank-owned logic, adapters, decisions, and configuration. | Enable safe regeneration and ownership. | Engineering owner | Proposed | Regeneration scenario proves owned content is not overwritten | 2026-08-17 |
| BAR-010 | Product measures shall support a named decision and permit drill-down to evidence. | Avoid opaque activity or maturity reporting. | Product authority | Proposed | Measure-to-decision traceability in the HSB journey | 2026-08-17 |
| BAR-011 | HSB evidence shall be labelled synthetic and shall not be used to claim customer demand, bank adoption, regulatory acceptance, or realised benefit. | Preserve evidence honesty. | Product authority | Proposed | Documentation and outputs retain synthetic scope and limitations | 2026-08-17 |
| BAR-012 | Open-source releases shall declare source rights, support status, compatibility, security response, and production-readiness evidence for their exact scope. | Support trustworthy adoption. | Open-source maintainer | Proposed | Release gate and published evidence manifest | 2026-08-17 |
| BAR-013 | User journeys and outputs shall be understandable and accessible to their intended roles without requiring knowledge of internal implementation. | Make the product consumable. | Product authority | Proposed | Role-based usability and accessibility review | 2026-08-17 |
| BAR-014 | The product shall support portable export of customer-owned assertions, decisions, and evidence with provenance. | Reduce lock-in and support bank control. | Architecture authority | Proposed | Round-trip export evidence for the selected scope | 2026-08-17 |

## Work items

| ID | Work item | Outcome or acceptance | Owner | Status | Depends on | Reviewed |
|---|---|---|---|---|---|---|
| WRK-001 | Confirm the primary user, sponsor, decision, trigger, and bounded HSB scope. | OQ-001 through OQ-003 and OQ-012 have accepted answers or explicit bounded hypotheses. | Product authority | Planned | None | 2026-08-17 |
| WRK-002 | Review and promote accepted Business Architecture requirements. | Each BAR item is accepted, deferred, rejected, or revised with rationale and evidence expectation. | Architecture authority | Planned | WRK-001 | 2026-08-17 |
| WRK-003 | Elaborate VS-02 Bank-Estate Understanding and VS-03 Target Architecture and Change. | Stages, actors, information, decisions, measures, failure paths, and capability dependencies are explicit. | Architecture authority | Planned | WRK-001 | 2026-08-17 |
| WRK-004 | Create the platform capability heatmap. | Capabilities are assessed by value, differentiation, evidence, maturity, dependency, risk, and proposed investment. | Product and architecture authority | Planned | WRK-001, WRK-003 | 2026-08-17 |
| WRK-005 | Develop the HSB organisation, stewardship, and decision-right map. | OQ-013, OQ-016, and ASM-007 are exercised with accountable roles and escalation paths. | Architecture authority | Planned | WRK-001 | 2026-08-17 |
| WRK-006 | Define conceptual business information and provenance needs for the scenario. | Information groups, ownership, authority, identity, history, sensitivity, and exchange needs are ready for Information Architecture. | Information architect | Planned | WRK-001, WRK-003 | 2026-08-17 |
| WRK-007 | Compare the current decision process with the proposed platform-enabled process. | Decision effort, information hand-offs, review, outcomes, measures, and failure signals can be compared without assuming benefit. | Product authority | Planned | WRK-003, WRK-005, WRK-006 | 2026-08-17 |
| WRK-008 | Review Business Architecture value evidence and investment position. | Evidence supports continued architecture, a bounded experiment, narrower scope, or a stop decision. | Project owner | Planned | WRK-002 through WRK-007 | 2026-08-17 |
| WRK-009 | Develop the conceptual system context and ecosystem view. | Platform boundary, external actors, systems of record, exchanges, and ownership are explicit. | Architecture authority | Planned | WRK-001, OQ-014, OQ-017 | 2026-08-17 |
| WRK-010 | Develop the conceptual information and provenance model. | DEP-003 is met for the bounded scope and BAR-002, BAR-003, BAR-005, and BAR-014 have model traceability. | Information architect | Planned | WRK-006, WRK-009 | 2026-08-17 |
| WRK-011 | Develop the trust-boundary and security view. | Identity, authority, sensitive flows, tenant boundaries, threats, controls, and evidence responsibilities are explicit. | Security authority | Planned | WRK-009, WRK-010 | 2026-08-17 |
| WRK-012 | Elaborate the connected HSB scenario view. | One scenario traverses the required value streams, decisions, capabilities, information, trust boundaries, measures, and stop signals. | Architecture authority | Planned | WRK-003, WRK-005, WRK-010, WRK-011 | 2026-08-17 |
| WRK-013 | Develop the conceptual component interaction view. | Responsibilities and interactions are explicit without selecting deployable service boundaries or technologies. | Architecture authority | Planned | WRK-009 through WRK-012 | 2026-08-17 |
| WRK-014 | Develop the architecture roadmap and transition view. | Work packages, dependencies, evidence gates, option points, and stop conditions form a credible sequence. | Architecture authority | Planned | WRK-004, WRK-008, WRK-013 | 2026-08-17 |

## Issues

There are no active issues recorded at this time. Use `ISS-001` for the first
issue that requires active resolution rather than evidence gathering or a future
decision.

## Register review

At each review:

1. confirm new records have the correct type and a unique identifier;
2. assign an accountable owner and affected gate;
3. update status only from evidence or an authorised decision;
4. link related records and affected architecture documents;
5. retain the previous outcome when a record is superseded; and
6. update `governance/PROJECT_STATUS.md` when the current focus, evidence
   position, or next gate changes.
