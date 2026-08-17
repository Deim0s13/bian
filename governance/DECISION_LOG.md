# Decision log

This log records material project decisions before formal architecture decision
records are appropriate. A decision may be revisited when its stated trigger is
met. Proposed ideas belong in `OPEN_QUESTIONS.md`, not here.

| ID | Date | Decision | Consequence | Revisit trigger |
|---|---|---|---|---|
| DEC-001 | 2026-08-17 | Define the full use case before implementation or solution architecture. | Current contributions focus on product discovery and architecture inputs. | Owner closes the product-definition gate. |
| DEC-002 | 2026-08-17 | Use Horizon Synthetic Bank and synthetic information as the repeatable validation environment. | No claim of customer demand or real-bank fit may be derived from synthetic results. | A future external validation model is authorised. |
| DEC-003 | 2026-08-17 | Develop the project as independent open source. | Governance, contribution rights, source rights, support, and security processes are product requirements. | Rights review or sustainability model requires change. |
| DEC-004 | 2026-08-17 | Attribute content to BIAN only when it is authoritative, release-qualified, and traceable. | Project extensions and inferences need separate classes and provenance. | Never for convenience; refine only with authoritative BIAN guidance. |
| DEC-005 | 2026-08-17 | Treat production readiness as an evidenced release state. | Early work may be concept, experimental, or preview without weakening engineering expectations. | Readiness model is replaced by an approved evidence framework. |
| DEC-006 | 2026-08-17 | Use TOGAF to guide architecture method and viewpoints and BIAN for banking reference content. | Future architecture will maintain stakeholder, requirements, domain, transition, and governance traceability. | TOGAF tailoring or licensing review changes the approach. |
| DEC-007 | 2026-08-17 | Align cloud-native architecture and engineering to the current CNCF definition and relevant authoritative CNCF guidance. Treat common practice lists as discovery inputs, not CNCF standards, and do not mandate microservices or Kubernetes for every component. | CNCF sources and versions must be traceable to project requirements and evidence. Deployment boundaries and platforms require an evidenced fit. | CNCF guidance changes or solution architecture supplies evidence for a narrower choice. |
| DEC-008 | 2026-08-17 | Store durable project instructions and context in the repository. | `AGENTS.md` and governance documents are the source of truth across tools and sessions. | Repository governance model changes. |
| DEC-009 | 2026-08-17 | Do not use the Unicode em dash character in active project content. | Automated checks reject it; punctuation must use alternatives. | Project owner changes the writing convention. |
| DEC-010 | 2026-08-17 | Keep the initial technical spike archived and outside active design. | It may inform later experiments but carries no architectural authority. | Explicit review promotes a specific finding with new evidence. |
