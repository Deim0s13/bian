# Project glossary

## Purpose

This is the authoritative glossary for recurring project-defined terms used
across the BIAN Adoption & Engineering Platform documentation.

The glossary does not redefine BIAN terminology. A term attributed to BIAN must
retain the exact meaning, identifier, release and source qualification supplied
by an authorised BIAN source. Where a project term and a BIAN term appear
similar, the authority class and source determine their meaning.

## Usage rules

- Use a defined term consistently or state a narrower meaning where it is used.
- Do not use qualifiers such as "material", "applicable", "appropriate" or
  "supported" to make an obligation optional without a recorded scope rule.
- A requirement must identify the records or events in scope, the accountable
  owner, canonical gate, related records and evidence needed to assess it.
- Undefined specialist terms should be added here when they recur or affect a
  decision. One-off explanations may remain in their source document.

## Terms

### ADM cycle

The project-tailored progression through the architecture phases needed for one
architecture scope or increment, with requirements managed throughout. A later
cycle may revisit only the affected phases; it does not erase the decisions,
baselines or evidence from an earlier cycle.

### Accountable owner

The single role answerable for the outcome, decision or requirement. Other
roles may advise, supply information, review or perform work, but shared
participation does not create shared accountability.

The role name must come from the canonical role catalogue in the Architecture
Register. In this project, `owner` describes organisational accountability;
`authority` describes the provenance or semantic standing of information, or a
formally delegated decision right in an adopting organisation.

### Applicable

Required because an explicit scope rule or triggering condition is met. The
scope rule, trigger and accountable decision must be recorded. "Applicable"
must not mean optional, convenient or left to an implementer without a decision
rule.

### Assertion

A project-defined claim by an identified authority about a subject. It retains
its source, authority class, provenance, time context, review state and known
limitations. Acceptance of an assertion does not change its original authority.

### Architecture baseline

The explicitly approved and versioned architecture state used for comparison,
governance and change impact within a declared scope. A working baseline may
still carry registered gaps; it must not be confused with implementation or
production evidence.

### Architecture increment

A bounded addition or change to the architecture with its own scope,
stakeholders, requirements, decisions, evidence and affected gates. Several
increments may coexist when their identities and relationships remain explicit.

### Authoritative source

The source entitled to define a particular external assertion within a declared
scope. For BIAN-attributed content this must be an authorised, release-qualified
BIAN source. The platform preserves and reports that authority but does not
inherit it.

### Authoritative system

The system designated by its owning organisation to govern a particular bank,
customer or operational record. The platform may capture or reference its
assertions without silently becoming the replacement system of record.

### BIAN release

A specifically identified release of BIAN source material. It is distinct from
a release of this project or of an adopting bank's software.

### BIAN-attributed assertion

An assertion presented as having been defined by BIAN. It requires authorised
source provenance, exact release context and preservation of source meaning.
Project extensions, customer mappings and inferences are not BIAN-attributed
assertions.

### Canonical gate

A governed decision point identified by a `GAT` record in the Architecture
Register. It defines entry criteria, exit criteria, accountable role, blockers
and current state. Architecture phases, work products, capability names and
calendar dates are not substitutes for a canonical gate.

### Customer-owned information

Information supplied by an adopting organisation or created on its behalf that
the organisation is entitled to retrieve, govern and remove, subject to law,
contract, third-party rights and recorded retention obligations.

### Derived projection

A reproducible representation created from declared inputs and transformation
rules. A projection is not an assertion. It retains its lineage and does not
acquire the authority of its source merely because it was generated from that
source. Any claim based on it is a separate assertion.

### Delivery horizon

The canonical `GAT` event by which a requirement must be satisfied. A delivery
horizon sequences an obligation; it does not weaken it, prove satisfaction or
authorise implementation.

### Evidence

A scoped record that supports or challenges an assertion, requirement, control,
test result, finding or conclusion. Evidence retains its source, method, time,
scope, limitations, review and validity state.

### First consumable proposition

The smallest bounded product outcome that an intended user can complete and
evaluate. The current hypothesis is the HSB responsibility-allocation decision
accepted under `DEC-018`. It is not the complete platform vision and does not
constitute build authorisation.

### Governed record

A record whose creation, interpretation, review, change, retention or use can
affect a project or customer decision, claim, right, responsibility, control,
generated output or downstream action. Temporary processing data that cannot
affect or reproduce those outcomes is not a governed record.

### Information governance owner

The single role accountable for translating approved legal, regulatory and
customer information-lifecycle policy into governed residency, retention,
deletion, archival and legal-hold obligations. Security and legal specialists
provide required review without becoming joint owners of the requirement.

### Material

Capable of changing a decision, claim, risk, control conclusion, ownership,
customer outcome, architecture boundary, legal or source-rights position,
security posture, or required downstream action.

When "material" is used, the accountable owner must be able to identify which
of these consequences makes the item material. The term must not be used to
omit records solely because recording them is inconvenient or expensive.

### Platform inference

A project or product-generated interpretation, match, recommendation or
conclusion that is not an authoritative BIAN or customer assertion. It must
retain its method, inputs, uncertainty and review state.

### Record origin

The attributable source and derivation of a governed register record, including
whether it arose from owner direction, architecture analysis, external review,
evidence or AI-assisted drafting. Origin does not imply approval or independent
validation.

### Provenance

The attributable and versioned connection between a governed record, its
sources, the processing or decisions that produced it, and the records that
depend on it.

### Relationship assertion

A project-defined assertion that exactly two identified endpoint subjects are
related in a stated way. It has its own identity and is independently sourced,
classified, versioned and reviewed. Additional context uses identified context
subjects or assertions about the reified relationship. A customer-to-BIAN
mapping is a customer or HSB relationship assertion, not an authoritative BIAN
relationship.

### Source capture

An immutable, integrity-verifiable record of exactly what the platform obtained
or referenced from an external source, including source identity, version,
capture time, method and rights context.

### Solution Architecture

The project-specific application of approved platform and enterprise
architecture to one bounded delivery scope. It may select deployable products
and patterns after its preceding gates pass. It does not replace Technology
Architecture or authorise implementation by itself.

### Supported export

An export whose included record types, semantic guarantees, exclusions and
rights constraints are documented and testable. Labelling an export as
supported does not permit the platform to exclude customer-owned information
required by `DAR-016`.

### Subject

A platform-minted stable identity anchor for a thing about which assertions may
be made. Registration does not itself assert that the thing exists, that an
external source recognises it, or that two source records identify the same
thing.

### Technology Architecture

The architecture of baseline and target technology capabilities, logical
technology building blocks, standards constraints, quality attributes, trust
and operational boundaries, and their gaps. It establishes the technology
context in which later bounded solutions are evaluated.

### Transition architecture

An explicitly governed intermediate architecture state between a baseline and
target. It must identify its purpose, temporary constraints, dependencies,
accepted debt, entry and exit conditions, and affected requirements.

### Truth class

A visible classification showing whether a statement is an authoritative BIAN
assertion, mechanically derived projection, project extension, customer or HSB
assertion, platform inference, third-party assertion or evidence record. The
detailed operational classes are defined by the BIAN alignment policy; the
user-facing groupings are presentation aids and do not replace them.

### View Definition

A governed and versioned policy that states how a selected or current view is
formed from assertions and other governed records, including time, review,
authority, conflict and absence behaviour. It produces a reproducible
materialisation and does not overwrite its inputs.

### View materialisation

The reproducible Derived Projection produced by evaluating a named and versioned
View Definition against an exact input set and evaluation context. It is not an
assertion. `DAR-026` requires a decision to retain the information needed to
reconstruct the materialisation it used.
