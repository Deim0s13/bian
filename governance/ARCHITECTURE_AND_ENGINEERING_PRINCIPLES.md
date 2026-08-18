# Architecture and engineering application guidance

## Status

The authoritative overarching principles are maintained in the
[project principles catalogue](../product/PROJECT_PRINCIPLES.md). This document
applies `PRN-002`, `PRN-004`, `PRN-006`, `PRN-007`, `PRN-010`, `PRN-013`,
`PRN-016`, and `PRN-017` to architecture method and future engineering. It does
not create a second principle catalogue.

The active conceptual direction is in the
[Architecture Vision](../architecture/ARCHITECTURE_VISION.md). This principles
guidance is not a solution architecture and does not approve an implementation
style or technology stack.

## How TOGAF and BIAN will work together

The project intends to align its architecture practice to the TOGAF Standard,
10th Edition. TOGAF will provide the method, governance discipline, stakeholder
concerns, viewpoints, requirements management, and progression from vision to
change governance.

BIAN will provide banking reference content, language, and relationships within
the scope of authorised BIAN sources. BIAN is not a substitute for an enterprise
architecture method, and TOGAF is not the source of banking semantics.

Architecture work should therefore:

- begin with an Architecture Vision grounded in users, outcomes, scope, and
  stakeholder concerns;
- maintain requirements and traceability throughout the lifecycle;
- distinguish Business, Data, Application, and Technology Architecture;
- describe baseline, transition, and target states where those distinctions are
  useful;
- select views because they answer named stakeholder concerns;
- record principles, decisions, risks, gaps, work packages, and governance;
- retain reusable architecture assets in a deliberate repository structure;
- tailor the method to a small open-source project rather than reproduce every
  possible TOGAF deliverable.

No TOGAF conformity, certification, or endorsement will be claimed. The project
must review The Open Group licensing terms before copying or distributing TOGAF
templates or protected content. Its own architecture artefacts should express
original project analysis and provide attribution where needed.

## Architecture sequence

The tailored lifecycle is defined in
[Architecture lifecycle and ADM tailoring](../architecture/ARCHITECTURE_LIFECYCLE.md).
Its intended progression is:

1. Architecture Vision and Business Architecture;
2. Information Systems Architecture, covering Data and Application
   Architecture;
3. Technology Architecture;
4. Opportunities and Solutions;
5. Migration Planning and bounded build authorisation;
6. bounded Solution Architecture and implementation readiness;
7. Implementation Governance, release evidence and operational learning; and
8. Architecture Change Management, targeted revision and later ADM cycles.

Requirements Management and continuous architecture governance operate across
the entire lifecycle. The sequence is iterative, but iteration does not justify
silently skipping an unresolved gate. Solution Architecture is a project
delivery activity for a bounded authorised scope; it does not replace TOGAF
Technology Architecture.

## Cloud-native position

CNCF defines cloud native in terms of programmatic and repeatable delivery at
scale, with loosely coupled systems that are secure, resilient, manageable,
sustainable, and observable. The project adopts those qualities as its direction.

CNCF does not publish a single ten-point application-development standard. The
ten practices supplied during discovery, and similar lists found elsewhere, are
useful prompts but are not authoritative CNCF guidance. They must not be quoted
or assessed as though they were a CNCF standard.

### Guidance hierarchy

Cloud-native decisions and claims will use the following source hierarchy:

1. The current CNCF Cloud Native Definition establishes the foundational
   characteristics and intent.
2. CNCF Technical Advisory Group publications, whitepapers, and maintained
   guidance provide concern-specific direction, such as security, application
   delivery, observability, platform engineering, and sustainability.
3. Official documentation from CNCF projects provides implementation guidance
   only when that project or interface is actually in scope.
4. CNCF surveys, technology radars, end-user reports, and blog posts provide
   market or practitioner context, not normative requirements.
5. Third-party interpretations remain external assertions and are never
   presented as CNCF guidance.

Each source used for an architecture requirement should retain its title,
publisher, version or publication date, stable location, access date, applicable
scope, and the project interpretation derived from it. Material guidance changes
should trigger impact review, just as a BIAN release change will.

The project will eventually maintain a cloud-native alignment matrix connecting:

```text
CNCF source and version
        -> applicable guidance
        -> project requirement or quality attribute
        -> architecture decision and implementation
        -> test or operational measure
        -> evidence, exception, and review status
```

This supports narrow, evidenced statements. The project will not claim generic
"CNCF compliance", CNCF certification, or CNCF endorsement.

### Working architecture concerns

Until the alignment matrix is established, the following project-authored
concerns will help route discovery. They are an interpretation to be tested
against the relevant CNCF source, not a reproduction of CNCF guidance:

1. Design around cohesive BIAN-informed and project-owned domain boundaries.
2. Use independently deployable services only where ownership, scaling,
   isolation, resilience, or release needs justify them.
3. Package deployable workloads as secure, minimal OCI containers.
4. Automate build, test, security, release, deployment, and rollback paths.
5. Design scaling from workload characteristics, service objectives, and cost,
   rather than assuming every component must scale independently.
6. Build identity, least privilege, policy, privacy, and supply-chain security
   into design and delivery.
7. Make health, logs, metrics, traces, audit events, and service objectives part
   of the service contract.
8. Manage infrastructure and policy declaratively through reviewed code and
   reproducible automation.
9. Define APIs, events, schemas, compatibility, and failure behaviour as governed
   contracts before implementation.
10. Engineer and test for dependency failure, recovery, rollback, and degraded
    operation.
11. Establish shared ownership across product, architecture, engineering,
    security, risk, platform, and operations.
12. Preserve portability and support restricted-network and self-managed bank
    environments where product requirements justify them.

Microservices are an available technique, not a starting mandate. A modular
deployment may be the safer first design if it preserves boundaries and future
separation while reducing distributed-system overhead. Kubernetes and OpenShift
are expected deployment contexts, but must not contaminate the cloud-neutral
core or replace sound application architecture.

## Decision tests

A material architecture choice should answer:

- Which customer or stakeholder outcome does this support?
- Which requirements and quality attributes drive it?
- What trust boundary, failure mode, or operational responsibility changes?
- What are the simplest credible alternatives?
- What evidence supports the decision, and what remains an assumption?
- How can the choice be reversed or evolved?
- Does it preserve BIAN provenance and the separation of assertion classes?
- What will prove the architecture works in Horizon Synthetic Bank?

## Authoritative references

- [The TOGAF Standard, 10th Edition](https://www.opengroup.org/togaf)
- [TOGAF Standard licensing information](https://www.opengroup.org/togaf-standard-10th-edition-downloads)
- [CNCF Cloud Native Definition](https://github.com/cncf/toc/blob/main/DEFINITION.md)
- [CNCF TAG Security Cloud Native Security Whitepaper](https://tag-security.cncf.io/community/resources/security-whitepaper/)
