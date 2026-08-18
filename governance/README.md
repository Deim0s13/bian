# Project governance and working context

This directory contains the shared context used by contributors and AI agents.
It keeps working preferences and project controls versioned alongside the
product definition.

| Document | Purpose |
|---|---|
| `PROJECT_STATUS.md` | Current stage, focus, evidence position, and next gate |
| `ARCHITECTURE_REGISTER.md` | Canonical gates, roles, provenance, decisions, questions, risks, assumptions, dependencies, evidence gaps, requirements, work items, and issues |
| `GLOSSARY.md` | Authoritative definitions for recurring project-defined terms and scope qualifiers |
| `PROJECT_CONTEXT.md` | Audience, enterprise framing, and stakeholder lenses |
| `WRITING_STYLE.md` | Documentation and communication conventions |
| `ARCHITECTURE_AND_ENGINEERING_PRINCIPLES.md` | Application guidance for TOGAF, BIAN, and cloud-native direction |
| `QUALITY_AND_REVIEW.md` | Review, testing, simplicity, and quality expectations |
| `DECISION_LOG.md` | Compatibility pointer to the Architecture Register |
| `OPEN_QUESTIONS.md` | Compatibility pointer to the Architecture Register |

`AGENTS.md` is the operational entry point for Codex. These documents provide
the detail behind those instructions and are the repository source of truth.
Personal or tool-generated memory may help a working session, but it must not be
the only place where a project rule or decision is recorded.

Governed records have one authoritative home in `ARCHITECTURE_REGISTER.md`.
Other documents provide context and reference stable identifiers without
duplicating lifecycle status, ownership, or resolution.

Architecture stages describe the sequence of work. They are not approval
points. Every approval or readiness reference must use the canonical `GAT`
catalogue, and every register owner must use the canonical `ROL` vocabulary.

The authoritative overarching principle catalogue is
[`product/PROJECT_PRINCIPLES.md`](../product/PROJECT_PRINCIPLES.md). The
requirements-management view is
[`architecture/REQUIREMENTS_AND_TRACEABILITY.md`](../architecture/REQUIREMENTS_AND_TRACEABILITY.md),
while requirement records remain in the Architecture Register.
