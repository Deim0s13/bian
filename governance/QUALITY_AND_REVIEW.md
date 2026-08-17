# Quality, review, and continuous verification

## Intent

The project will control quality continuously rather than rely on a final review.
The controls must remain proportionate to the current stage and become stronger
as the risk and deployable scope increase.

Automation provides repeatable evidence. It does not replace architectural,
security, BIAN, legal, accessibility, operational, or human judgement.

## Current documentation gate

Every active change must:

- remain within the current project stage or explicitly change the stage;
- preserve BIAN attribution and assertion-class boundaries;
- update decisions, open questions, status, and traceability when affected;
- contain no Unicode em dash characters, trailing whitespace, or broken local
  Markdown links;
- pass `python3 tools/check_project.py`;
- avoid modifying the archived spike unless that is the stated purpose.

The checker is deliberately small. Passing it means the documented mechanical
rules were met, not that the content is correct or approved.

## Review model for future implementation

When code begins, every change should be small enough to understand and should
pass two distinct review lenses:

### Fitness and risk

- requirement and acceptance evidence;
- correctness and failure behaviour;
- BIAN source integrity and provenance;
- security, privacy, abuse, and trust-boundary impact;
- compatibility, migration, recovery, and operational impact;
- tests that would fail if the intended behaviour regressed.

### Simplicity and maintainability

- unnecessary code, abstractions, dependencies, configuration, and services;
- duplicated behaviour or competing sources of truth;
- unclear ownership or leakage across module boundaries;
- dead paths, speculative extension points, and premature optimisation;
- documentation and diagnostics needed to operate the change;
- whether removal or reuse is safer than addition.

Automated code review may identify patterns and prompt investigation. A human
maintainer remains accountable for accepting risk and approving material design.
Security-sensitive, BIAN-attributed, source-rights, and release-control changes
require a reviewer with the relevant competence.

## Continuous test model

The eventual test portfolio should be risk-based and layered:

| Cadence | Purpose |
|---|---|
| Local and pre-commit | Fast formatting, linting, unit, schema, and policy feedback |
| Every pull request | Unit, contract, integration, security, provenance, and compatibility tests affected by the change |
| Main branch and scheduled | Broader integration, dependency, vulnerability, licence, drift, and deterministic-build checks |
| Release candidate | System, migration, rollback, performance, resilience, recovery, accessibility, and operational evidence |
| Production operation | Service objectives, telemetry, security monitoring, synthetic journeys, and controlled recovery exercises |

Test counts and coverage percentages are supporting signals, not the objective.
Critical rules and failure paths require explicit tests. Generated output and
imports require deterministic tests and source-lineage checks. Defects should
normally add a regression test at the lowest useful level.

## Preventing bloat

- Prefer a narrow end-to-end capability over horizontal scaffolding.
- Add a component, service, dependency, or framework only for a named requirement.
- Record high-impact or difficult-to-reverse choices before implementation.
- Track repository size, dependency count, build time, test time, complexity,
  duplication, and unsupported code as trends once code exists.
- Schedule whole-repository architecture, dependency, and dead-code reviews.
- Delete obsolete paths as part of the change that replaces them when safe.
- Time-bound experimental code and state the decision it is intended to inform.

No universal line limit or coverage target is set before the implementation
language and risk profile are known. Those thresholds must be selected through
evidence and recorded when solution architecture begins.

## Exceptions

An exception must identify its owner, reason, affected scope, risk, compensating
control, approval, and expiry or removal condition. A schedule date alone is not
a reason to lower a security, provenance, or correctness gate.

