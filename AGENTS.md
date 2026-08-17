# Repository instructions

These instructions apply to the entire repository unless a more specific
`AGENTS.md` exists in a subdirectory.

## Project position

- This is an independent, open-source BIAN adoption and transformation project.
- The current stage is conceptual architecture. Develop outcomes, requirements,
  viewpoints, information concepts, boundaries, risks, and operating concerns.
  Do not start implementation, select solution technologies, or turn the
  archived spike into an approved design unless the user explicitly changes the
  stage or asks for a bounded experiment.
- Treat `archive/initial-technical-spike/` as historical reference only. Do not
  edit, revive, or cite it as current architecture without explicit instruction.
- Confirm the repository root before editing. Do not work from a copied sibling
  directory or use the archive as the active workspace.

## Required context

Before material work, read the parts of these files relevant to the request:

1. `README.md`
2. `governance/PROJECT_STATUS.md`
3. `governance/PROJECT_CONTEXT.md`
4. `governance/WRITING_STYLE.md`
5. `product/PROJECT_PRINCIPLES.md`
6. `product/BIAN_ALIGNMENT_POLICY.md`
7. `architecture/ARCHITECTURE_VISION.md`
8. `governance/ARCHITECTURE_AND_ENGINEERING_PRINCIPLES.md`
9. `governance/QUALITY_AND_REVIEW.md`

Use `governance/DECISION_LOG.md` and `governance/OPEN_QUESTIONS.md` when a task
creates, changes, or depends on a material decision.

## BIAN integrity

- Use official BIAN language, identifiers, relationships, lifecycle status, and
  release qualification only when supported by an authorised source.
- Never invent, rename, infer, or enrich a BIAN semantic and present it as BIAN.
- Keep authoritative BIAN assertions, derived projections, project extensions,
  fictional-bank assertions, external assertions, and inferences visibly
  separate, with provenance appropriate to their class.
- Preserve the known BIAN R14 distinction between 258 Service Domains and 242
  published API specifications. A Service Domain without published Service
  Operations must not be presented as having a BIAN-defined API.
- Do not imply BIAN, Red Hat, TOGAF, CNCF, regulatory, or bank endorsement,
  certification, conformance, or support without scoped evidence and permission.

## Architecture and engineering

- Begin with customer outcomes, stakeholders, requirements, constraints, risks,
  operating model, trust boundaries, and evidence before components or products.
- Use TOGAF as a method and viewpoint discipline where appropriate. Use BIAN as
  banking reference content and taxonomy. Do not confuse their roles.
- Use the current CNCF Cloud Native Definition and relevant authoritative CNCF
  guidance, with source and version recorded. Do not present a project-authored
  checklist as CNCF guidance. Microservices, Kubernetes, OpenShift, containers,
  and other patterns require an evidenced fit.
- Prefer the simplest architecture that satisfies domain boundaries, security,
  resilience, operability, portability, and evolution needs.
- Security, privacy, provenance, accessibility, operability, testability, and
  software supply-chain integrity are design concerns from the first increment.
- Production readiness is a scoped evidence state, not an aspiration or label.

## Communication

- Write for an experienced enterprise and pre-sales architect and a technically
  capable audience in regulated financial services.
- Be concise, conversational, plainspoken, pragmatic, and constructively direct.
- Lead with customer and stakeholder outcomes, then trade-offs and implications.
- Use British English unless quoting an authoritative source.
- Do not use the Unicode em dash character anywhere in active project content.
- Avoid consultant language, hype, generic vendor claims, robotic phrasing,
  unnecessary theory, and low-level implementation detail unless it is needed.
- Distinguish fact, decision, assumption, hypothesis, inference, and open question.

## Change discipline

- Keep changes small, coherent, reviewable, and free of speculative scaffolding.
- Update `governance/PROJECT_STATUS.md` when the project stage, current focus, or
  next gate changes.
- Record material decisions and consequences in
  `governance/DECISION_LOG.md`; record unresolved matters in
  `governance/OPEN_QUESTIONS.md`.
- Update affected traceability when product scope or meaning changes.
- Run `python3 tools/check_project.py` before completing an active-file change.
- Do not weaken or bypass a check to make a change pass. Fix the issue or record
  an approved, time-bounded exception through the future governance process.
