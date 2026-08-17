# Requirements and traceability

## Document status

**Status:** Proposed baseline for project-owner review

**Scope:** Cross-cutting project and architecture requirements

**Excluded:** Resolution of the minimum Business Architecture questions,
Information Systems Architecture, solution requirements, technology selection,
and implementation specifications

## Purpose

This document defines how requirements are derived, classified, reviewed,
traced, and changed across the BIAN Adoption & Engineering Platform. The
[Architecture Register](../governance/ARCHITECTURE_REGISTER.md#requirements) is
the sole authoritative record for requirement wording, ownership, status,
acceptance evidence, and review state.

This document is a requirements-management view. It must not become a competing
requirements catalogue.

## Requirements model

The current baseline uses two requirement levels:

| Identifier | Level | Purpose |
|---|---|---|
| `REQ` | Overarching project and architecture requirement | Governs enduring cross-cutting outcomes and constraints across architecture domains and lifecycle stages |
| `BAR` | Business Architecture requirement | Expresses the business behaviour, governance, value, information, and operating-model needs derived from the Business Architecture |

Future Data, Application, Technology, security, operational, and solution
requirements will be introduced only when the relevant architecture work needs
them. They must refine or trace to an accepted `REQ`, `BAR`, stakeholder concern,
or approved scope change. They must not silently weaken an overarching
requirement.

Principles guide judgement; requirements state something that must be satisfied
or evaluated. A principle is not treated as implemented merely because a
requirement references it.

## Traceability thread

The intended thread is:

```text
Product outcome and stakeholder concern
        -> project principle
        -> overarching requirement
        -> domain or solution requirement
        -> architecture view and decision
        -> work item and implementation
        -> test, operational measure, or review
        -> evidence, finding, exception, and change impact
```

Not every record needs every link. Each material conclusion must retain enough
of the thread to explain why it exists, who owns it, how it will be assessed,
and what is affected when it changes.

## Baseline coverage

The proposed `REQ-001` through `REQ-020` baseline covers:

| Concern | Requirement references |
|---|---|
| Bounded value and investment discipline | `REQ-001` |
| Authoritative BIAN use and authority separation | `REQ-002`, `REQ-003` |
| Canonical model, identity, provenance, and connected traceability | `REQ-004` through `REQ-006` |
| Human decision rights and evidence-based claims | `REQ-007`, `REQ-008` |
| Security, privacy, resilience, and synthetic validation | `REQ-009`, `REQ-010` |
| Open-source trust and bank readiness | `REQ-011`, `REQ-012` |
| Enterprise coexistence, customer control, and runtime neutrality | `REQ-013` through `REQ-015` |
| Extensibility, deterministic generation, and change impact | `REQ-016` through `REQ-018` |
| Consumable experience and proportionate operability | `REQ-019`, `REQ-020` |

This coverage is deliberately architectural. It does not specify a deployment
topology, programming language, database, user-interface framework, cloud,
container platform, service decomposition, or product integration.

## Initial relationship to Business Architecture requirements

The existing Business Architecture requirements refine the cross-cutting
baseline as follows:

| Overarching requirement | Principal Business Architecture refinements |
|---|---|
| `REQ-001` | `BAR-001`, `BAR-006`, `BAR-010` |
| `REQ-002`, `REQ-003` | `BAR-003`, `BAR-011` |
| `REQ-004` through `REQ-006` | `BAR-002`, `BAR-005`, `BAR-007` |
| `REQ-007` | `BAR-004` |
| `REQ-008` | `BAR-008` |
| `REQ-010` | `BAR-011` |
| `REQ-011`, `REQ-012` | `BAR-012` |
| `REQ-013`, `REQ-014` | `BAR-005`, `BAR-014` |
| `REQ-017` | `BAR-009` |
| `REQ-019` | `BAR-013` |

The absence of a direct `BAR` refinement does not make an overarching
requirement optional. Some concerns will be refined primarily through later
Data, Application, Technology, security, or operational architecture work.

## Requirement quality tests

Before acceptance, a requirement should:

- identify a required outcome, constraint, behaviour, or quality rather than a
  preferred technology;
- have an accountable owner and traceable source or rationale;
- be sufficiently bounded to assess without claiming universal coverage;
- define credible acceptance evidence or an explicit evidence gap;
- avoid combining unrelated obligations that need different owners or gates;
- preserve BIAN, project, bank, inference, and evidence authority boundaries;
- identify material dependencies, risks, conflicts, and exceptions;
- be understandable to the stakeholders responsible for approving or meeting it;
- remain compatible with the governing principles or record an explicit
  decision where a conflict exists; and
- be testable, reviewable, measurable, or otherwise verifiable at the stage
  where it is required.

## Lifecycle and change control

Requirement status is governed by the Architecture Register vocabulary:
`Proposed`, `Accepted`, `Deferred`, `Rejected`, or `Superseded`.

- Proposed requirements do not authorise implementation.
- Acceptance confirms that the requirement belongs in the governed baseline;
  it does not prove that the product already satisfies it.
- A deferred requirement retains its rationale and required gate.
- A rejected requirement retains the decision and evidence that rejected it.
- A superseded requirement remains traceable to its replacement.
- Exceptions identify the owner, scope, rationale, risk, compensating control,
  approval, expiry, and removal condition.
- Material requirement changes trigger review of related principles, decisions,
  architecture views, risks, work items, tests, evidence, and downstream assets.

## Review outcome required

Project-owner review should determine for each `PRN` and `REQ` record whether it
is accepted, revised, deferred, rejected, or requires further analysis. Once
that review is recorded through `WRK-016` and `WRK-018`, the project can address
the minimum Business Architecture questions without relying on unstated
constraints.
