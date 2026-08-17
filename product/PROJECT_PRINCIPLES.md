# Project principles and non-negotiable constraints

## Status

These principles apply to product discovery, future architecture, implementation,
release, and operation. They supersede any conflicting assumption in the
archived technical spike.

## 1. Validate with a fictional bank and synthetic information

The project will not depend on banks or customers participating in product
trials. A deliberately fictional institution and comprehensive synthetic estate
will provide the repeatable validation environment.

Synthetic evaluation can demonstrate functional behaviour, internal consistency,
security properties, failure handling, performance, repeatability, and expected
outputs. It cannot establish real-bank desirability, procurement readiness,
operating-model fit, or realised business value. Those outcomes must remain
labelled **unvalidated** unless later supported by appropriate external review or
real-world evidence.

See [FICTIONAL_BANK_AND_SYNTHETIC_VALIDATION.md](FICTIONAL_BANK_AND_SYNTHETIC_VALIDATION.md).

## 2. Build as an open-source project

The intended product, documentation, build processes, and governance will be
publicly inspectable and reusable under an approved open-source licence.

Open source means more than publishing source code. The project will require
transparent governance, contribution rules, security reporting, dependency and
licence controls, reproducible releases, maintained documentation, and a clear
support policy.

Apache License 2.0 is the initial project-licence candidate because it is
permissive, enterprise-friendly, and used by BIAN's public Semantic API
repository. It will not be adopted until a source-rights inventory confirms
that the project can satisfy all third-party obligations.

## 3. Engineer for bank adoption from the outset

Future implementation must follow bank-grade engineering and security practices
from its first increment. “Production ready” is not a marketing label or a claim
made on day one. A release becomes eligible for production only when it satisfies
defined, evidenced readiness gates for its declared scope.

Early versions may therefore be explicitly labelled experimental or not approved
for production while the underlying architecture and controls are developed.
This is not a shortcut; it is honest lifecycle management.

See [OPEN_SOURCE_AND_PRODUCTION_READINESS.md](OPEN_SOURCE_AND_PRODUCTION_READINESS.md).

## 4. Attribute only authoritative BIAN content to BIAN

Every item represented as BIAN must be traceable to an authorised, authoritative
BIAN source and exact release. The project must not invent, reinterpret, rename,
or silently enrich BIAN semantics and continue to label them as BIAN-defined.

This does not mean that every concept in the product is defined by BIAN. Customer
landscapes, project workflows, security profiles, regulatory mappings, vendor
claims, implementation choices, and synthetic-bank data require separate
namespaces and provenance. They must never be confused with authoritative BIAN
content.

See [BIAN_ALIGNMENT_POLICY.md](BIAN_ALIGNMENT_POLICY.md).

## 5. Use BIAN language precisely, without implying affiliation

Where a BIAN concept exists, the project will use BIAN's official name,
definition, hierarchy, relationship, and lifecycle status for the selected
release. Project documentation will use BIAN terminology consistently and link
to its source glossary or model element.

Project-specific concepts must use clearly identified project terminology. The
project must not present itself as an official BIAN deliverable, use BIAN marks
beyond lawful descriptive attribution, or imply review or endorsement that has
not occurred.

## 6. Prepare for rigorous external review

The project should be capable of surviving review by banking architects,
security specialists, open-source maintainers, BIAN subject-matter experts, and
Red Hat colleagues. Reviewability requires:

- written requirements and traceability;
- explicit assumptions and limitations;
- architecture decisions with alternatives and consequences;
- threat models and abuse cases;
- verifiable builds and tests;
- evidence for conformance and readiness statements;
- clean licences and software supply-chain records;
- operational, deployment, upgrade, recovery, and support documentation;
- no reliance on private knowledge to understand or reproduce the system.

Peer review, including possible future Red Hat review, is valuable evidence but
does not by itself establish BIAN endorsement, regulatory compliance, security,
or fitness for a specific bank.

## Decision rule

When speed conflicts with provenance, security, maintainability, source rights,
or truthful claims, those qualities take precedence. Scope may be reduced;
engineering and trust standards may not.

