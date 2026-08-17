# Fictional bank and synthetic validation policy

## Purpose

The project will use a fictional institution to develop and evaluate every
capability without requesting access to a bank's systems, data, or staff.

Working name: **Horizon Synthetic Bank (HSB)**.

HSB is not intended to represent or imitate a particular institution. Its name,
organisational structure, systems, people, products, identifiers, events, and
records will be explicitly fictional.

## What HSB must provide

HSB should eventually be a coherent synthetic bank, not a handful of unrelated
test records. It needs enough internal history and imperfection to exercise the
fourteen product use cases.

### Business context

- customer segments and channels;
- products and services;
- selected business scenarios;
- organisation, teams, accountable roles, and ownership conflicts;
- strategic objectives and transformation constraints.

### Technology estate

- application portfolio and lifecycle states;
- API catalogue, consumers, versions, and mixed-responsibility examples;
- events, messages, batch exchanges, and integrations;
- data assets, ownership, lineage, and quality concerns;
- platforms, environments, deployment units, and technology obsolescence;
- vendor products and customer-built systems;
- current, transition, and proposed target architectures.

### Governance and assurance context

- architecture principles, decisions, review submissions, and exceptions;
- security profiles and enforcement points;
- fictionalised requirements, controls, implementations, tests, and evidence;
- lifecycle, incident, change, vulnerability, and release histories;
- BIAN mapping proposals with accepted, rejected, disputed, and unreviewed states.

### Change over time

HSB needs versioned snapshots. Its estate should evolve through acquisitions,
modernisation, API creation, vendor replacement, ownership change, and BIAN
release adoption so that impact and roadmap capabilities can be evaluated.

## Synthetic data rules

- Never use copied customer, employer, partner, or production information.
- Never use real personal data, account data, credentials, secrets, keys, tokens,
  private endpoints, or confidential topology.
- Use reserved domains such as `.example` and standards-reserved test ranges.
- Mark every synthetic dataset and record family with its fictional origin.
- Avoid realistic identifiers that could be mistaken for routable bank, card,
  payment, tax, or legal identifiers unless an applicable standard explicitly
  defines a safe test range.
- Generate test identities and transaction narratives independently; do not
  lightly pseudonymise real records.
- Keep seeds and generation rules versioned so scenarios are reproducible.
- Include invalid, incomplete, stale, contradictory, and adversarial records;
  production systems cannot assume clean inputs.
- Publish a synthetic-data manifest describing purpose, generator/source,
  schema, version, limitations, and expected relationships.

## Validation layers

### 1. Source conformance

Verify that BIAN-attributed model elements exactly match the authoritative source
for the declared release and that project extensions remain distinguishable.

### 2. Scenario correctness

Define expected HSB outcomes before exercising a capability. For example, an API
alignment scenario should specify the accepted mapping, ambiguous evidence,
known false lead, and expected reviewer decision.

### 3. Functional verification

Prove that workflows, calculations, mappings, version comparisons, generation,
and review states behave as specified, including negative and failure cases.

### 4. Security verification

Exercise authentication, authorisation, tenancy, input handling, secrets,
logging, supply-chain, abuse, isolation, recovery, and secure-default scenarios.

### 5. Operational verification

Exercise installation, upgrade, rollback, backup, restore, disaster recovery,
observability, incident diagnosis, capacity, and dependency failure.

### 6. Outcome simulation

Use role-based HSB scenarios to test whether outputs support the intended
decision. Record the expected action and evidence required, not merely whether a
screen or report was produced.

### 7. Independent review

When the project is sufficiently mature, invite qualified peers to review model
fidelity, architecture, security, operability, and usability using the public HSB
environment. Review findings become evidence and tracked work—not endorsement.

## What synthetic validation cannot prove

- that a bank will buy, adopt, or operate the product;
- that the assumed user workflow matches a particular institution;
- that findings create measurable commercial or transformation value;
- that real enterprise data can be accessed, reconciled, or governed as assumed;
- that the product is certified, officially endorsed, or regulatory compliant;
- that production behaviour will match HSB without bank-specific assessment.

Documentation and scorecards must not imply otherwise.

## Scenario catalogue required before architecture completion

At minimum, the future HSB scenario catalogue should cover:

1. map a fragmented payments landscape;
2. analyse a mixed-responsibility payment API;
3. model an international-payment Business Scenario overlay;
4. design a payments target state and transition roadmap;
5. identify a proposed duplicate service through governance;
6. assess a BIAN release change against HSB mappings;
7. safely regenerate affected engineering assets;
8. apply distinct internal and external API security profiles;
9. produce scoped evidence with explicit unverified controls;
10. compare a fictional vendor product with HSB's current estate;
11. answer a modernisation question with traceable evidence; and
12. produce a multidimensional adoption view with honest data-quality indicators.

