# Open-source governance and production-readiness policy

## Intent

The project is intended to be a trustworthy open-source platform that a bank can
evaluate and, when a release satisfies its declared readiness gates, adopt in a
production environment.

This policy defines product expectations before technology choices are made.

## Honest use of “production ready”

No application is production ready merely because that was its design intent.
Production readiness is a scoped, evidenced release state.

The project will distinguish:

- **Concept:** product behaviour is being defined.
- **Experimental:** implementation exists for learning; not supported for
  production.
- **Preview:** architecture is stabilising; evaluation use only with documented
  limitations.
- **Production candidate:** all mandatory readiness evidence exists and is under
  independent review.
- **Production supported:** defined scope, environments, versions, upgrade path,
  security response, and operational documentation are maintained.
- **Deprecated/end of support:** migration and support dates are published.

“Secure by design from the first increment” is mandatory. “Production supported
from the first commit” would be neither credible nor safe.

## Open-source foundation required before public launch

- an OSI-approved project licence and complete third-party licence inventory;
- `README`, contribution guide, governance model, maintainer list, and roadmap;
- Code of Conduct and enforcement process;
- Developer Certificate of Origin or another explicit contribution-rights model;
- `SECURITY.md` with private vulnerability-reporting and disclosure process;
- issue, review, release, deprecation, and support policies;
- documented decision-making and conflict-resolution process;
- automated contributor and release checks;
- source provenance and required attribution/notice files;
- public documentation that separates project claims from BIAN assertions.

Apache License 2.0 is the preferred candidate, subject to legal/source-rights
review. The choice should support enterprise use, contribution, modification,
distribution, and patent clarity without changing third-party obligations.

## Secure engineering baseline

### Architecture and design

- documented system context, data classification, trust boundaries, abuse cases,
  and threat models before affected capabilities are implemented;
- secure defaults, least privilege, defence in depth, and explicit failure modes;
- tenant, identity, authorisation, encryption, key/secrets, and audit models;
- no implicit trust in imported BIAN, customer, plugin, or generated content;
- privacy and data-minimisation assessment even when development uses synthetic
  data;
- architecture decisions include rejected alternatives and security consequences.

### Software supply chain

- pinned and continuously monitored dependencies;
- dependency provenance, licence policy, and vulnerability policy;
- SBOMs for releases and deployable artefacts;
- reproducible or verifiable builds;
- protected build/release workflows and short-lived credentials;
- signed release artefacts and provenance attestations;
- secret scanning, static analysis, dependency analysis, and infrastructure scans;
- defined handling for unmaintained or compromised dependencies.

### Verification

- unit, integration, contract, system, migration, and failure tests;
- negative tests and adversarial input coverage;
- authentication/authorisation and tenant-isolation tests;
- security regression tests tied to threat models;
- performance, capacity, concurrency, endurance, and resource-limit tests;
- backup, restore, rollback, disaster-recovery, and dependency-outage exercises;
- accessibility and supported-browser/client verification where relevant;
- independent security review and penetration testing before production support.

### Operations

- documented installation, configuration, hardening, upgrade, rollback, backup,
  restore, incident response, and troubleshooting;
- health, metrics, logs, traces, audit events, and actionable alerts;
- documented retention, deletion, export, and recovery behaviour;
- version compatibility and supported-environment matrix;
- safe schema/data migrations with rehearsal and recovery;
- resource sizing and capacity guidance;
- high-availability and disaster-recovery objectives for each supported topology;
- no default credentials, embedded secrets, or silent outbound data collection.

### Release evidence

Every release candidate needs a machine-readable and human-readable evidence
pack covering:

- requirements and change scope;
- architecture and threat-model changes;
- test results and unresolved failures;
- vulnerabilities, exceptions, and accepted risks;
- SBOM, dependencies, licences, signatures, and build provenance;
- BIAN conformance scope and source lineage;
- upgrade/rollback results and compatibility;
- operational-readiness review;
- known limitations and support status;
- accountable approvals.

## Bank-adoption qualities

The architecture phase must consider, without prematurely selecting products:

- self-managed and restricted-network deployment;
- Kubernetes/OpenShift suitability and portable packaging;
- enterprise identity and policy integration;
- external secret and key management;
- audit export and security-monitoring integration;
- customer-controlled encryption and data location;
- tenant and environment isolation;
- configurable retention and deletion;
- backup, restore, migration, and exit/export;
- accessibility, localisation, and supportability;
- extension points that do not require unsafe code execution;
- integration with architecture, CMDB, API, source-control, CI/CD, and developer
  portal ecosystems through governed interfaces.

These are requirements to evaluate during architecture, not permission to claim
support before it is implemented and verified.

## Quality gates cannot be waived for schedule

If a feature cannot meet the required security, conformance, testability,
operability, maintainability, or source-rights standard, reduce or defer its
scope. Do not bypass the gate, conceal the limitation, or call it production
ready.

## External review

Future review by Red Hat colleagues or other qualified peers should evaluate:

- architectural fitness and maintainability;
- cloud-native and OpenShift operational qualities;
- security and software supply chain;
- open-source governance and contributor experience;
- usability of installation, operation, upgrade, and troubleshooting;
- evidence supporting BIAN and readiness claims.

Review findings should be published or tracked where disclosure is safe. Such
review does not imply Red Hat sponsorship, support, certification, or endorsement.

