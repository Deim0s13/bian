# Discovery questions

This is the working research agenda. Answers should be supported by interviews,
observed workflows, artefact review, or authoritative source analysis—not only
internal opinion.

## 1. Customer and buying context

- Which banks are actively trying to adopt BIAN, and why now?
- Is the initiating event a transformation programme, architecture uplift, API
  rationalisation, core replacement, regulatory programme, or platform strategy?
- Who feels the problem most acutely?
- Who controls budget and who can stop adoption?
- Is the first engagement expected to be software, advisory work, an assessment,
  or a combined service?
- What alternatives are customers using today—consultancies, spreadsheets,
  architecture tools, BIAN portal capabilities, internal teams, or doing nothing?

## 2. Decisions and value

- What decision does the customer struggle to make today?
- What happens when that decision is wrong or delayed?
- Which output would cause a customer to change a roadmap, design, ownership, or
  investment decision?
- How does the customer currently measure BIAN adoption or architecture quality?
- Which claimed benefits matter: simplification, speed, reuse, cost, reduced risk,
  clearer ownership, or transformation confidence?
- What evidence would be required to attribute an outcome to the product?

## 3. Scope and starting point

- Is payments the right first domain, or merely a familiar example?
- What is a useful bounded scope: value stream, product, business unit, legal
  entity, application cluster, API portfolio, or programme?
- How many assets and owners can be reviewed without overwhelming participants?
- What minimum mapping coverage is needed before useful findings emerge?
- Which use cases are essential to the first customer outcome and which can wait?

## 4. Customer information availability

- Which systems contain application, API, integration, data, ownership, vendor,
  lifecycle, and dependency information?
- Can stable identifiers reconcile the same asset across those systems?
- How complete, current, and trusted are descriptions and ownership records?
- Are API contracts available, and do they describe business purpose adequately?
- What telemetry or source metadata may be used, and under what restrictions?
- Which topology, security, customer, or commercial information is too sensitive
  to centralise?
- Can the platform operate where customer data resides if extraction is restricted?

## 5. Mapping and review workflow

- Who is qualified and accountable to approve a BIAN mapping?
- Should application owners, domain architects, and enterprise architects approve
  different parts of a mapping?
- How much evidence must accompany a suggested mapping?
- Which confidence language is understandable and acceptable?
- How should disputed or deliberately non-BIAN responsibilities be represented?
- How are exceptions, superseded decisions, and local terminology maintained?
- What level of ongoing review is sustainable?

## 6. BIAN source and semantic questions

- Which authorised BIAN artefacts are necessary for each proposed use case?
- What identifiers and relationships are stable across releases?
- Which semantics are explicit, and which would require inference?
- How should Service Domains without published API specifications be represented?
- Which official tools already address scenario design or API alignment, and where
  would this product complement rather than duplicate them?
- What licence and commercial terms apply to APIs, model data, diagrams,
  documentation, derived outputs, caching, and hosted use?

## 7. Architecture and transformation workflow

- How are current, transition, and target states documented today?
- What makes an architecture view authoritative enough for a programme?
- How are architecture decisions connected to initiatives and delivery backlogs?
- Which dependencies matter most for sequencing?
- How are retirement, coexistence, and exception decisions governed?
- Where should platform recommendations stop and accountable human judgment begin?

## 8. API alignment and governance

- What does “aligned to BIAN” mean to the customer in operational terms?
- Are operation, data, ownership, implementation, and domain-boundary alignment
  separate dimensions?
- What false-positive rate would make automated suggestions unusable?
- What is the existing process for discovering and approving APIs?
- Which duplicate or mixed-responsibility finding would trigger remediation?
- How should legacy APIs be treated when redesign would cost more than the benefit?

## 9. Security and assurance

- Who owns security-profile definitions and version changes?
- Which enforcement points exist across gateway, identity, policy, application,
  network, and runtime layers?
- Which evidence systems and test environments are authoritative?
- Who is allowed to approve control mappings and attestation language?
- How are evidence freshness, exceptions, compensating controls, and unverified
  areas managed today?
- What liability or regulatory risk could arise from product wording?

## 10. Vendor mapping

- Is vendor mapping a bank-owned assessment, vendor-submitted claim, independent
  analysis, or some combination?
- What evidence supports coverage claims at a useful granularity?
- Who owns corrections and release updates?
- How will confidential vendor and RFP information be protected?
- What decision criteria beyond functional coverage must remain outside BIAN?

## 11. Adoption measurement

- What behaviour should an adoption scorecard encourage?
- Which measures can be defined consistently across the selected scope?
- What denominators and data-quality indicators are required?
- How can the product prevent teams gaming a headline score?
- Which trends matter to executives versus practitioners?
- What does “successfully not mapped to BIAN” look like?

## 12. Product operating model

- Is the platform operated centrally, federated by domain, or delivered as a
  managed assessment service?
- Who owns source connectors, vocabulary, mapping quality, and review queues?
- How does stale data get detected and assigned?
- Which systems remain authoritative and which information is mastered here?
- What import/export and audit capabilities are non-negotiable?
- What would cause the model to become another abandoned architecture repository?

## 13. Interview prompts

Use prompts that elicit actual behaviour rather than asking whether the concept
sounds useful:

- “Tell me about the last time you tried to map a domain or portfolio to BIAN.”
- “Show me the artefacts and systems you used.”
- “Which part took the most effort?”
- “Where did reviewers disagree, and how was that resolved?”
- “What decision resulted from the work?”
- “When was the output last updated?”
- “Tell me about the last API or architecture proposal that duplicated something.”
- “How did you discover the duplication?”
- “Describe the last framework release impact assessment you performed.”
- “Which evidence would you require before trusting an automated recommendation?”
- “Who else would need to approve or maintain this?”

## 14. Evidence log template

For each material discovery finding, record:

| Field | Meaning |
|---|---|
| Finding | Concise statement of what was learned |
| Evidence type | Interview, observed workflow, document, data sample, source analysis |
| Participant/context | Relevant role and organisation context without unnecessary personal data |
| Use cases affected | FDN/UC identifiers |
| Strength | Single signal, repeated signal, contradicted, or validated |
| Implication | Product scope, workflow, trust rule, or architecture consequence |
| Follow-up | What must be learned next |

