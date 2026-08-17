# Contributing

## Current contribution scope

The project is in conceptual architecture. Contributions should improve the
product baseline, Architecture Vision, requirements, viewpoints, evidence,
traceability, governance, or HSB architecture scenarios. Implementation,
solution technology, and scaffolding are out of scope unless a bounded
experiment is explicitly approved.

Start with `AGENTS.md`, `README.md`, and `governance/PROJECT_STATUS.md`. Follow
the BIAN source rules in `product/BIAN_ALIGNMENT_POLICY.md`.

## Change expectations

- Keep each change focused on one coherent outcome.
- Identify whether statements are facts, BIAN assertions, project decisions,
  assumptions, hypotheses, inferences, or open questions.
- Cite authoritative sources for BIAN, standards, licences, and external claims.
- Update traceability, decisions, questions, and status when affected.
- Do not edit the archived spike as part of active product work.
- Run `python3 tools/check_project.py` before requesting review.

Review considers content fitness, provenance, stakeholder impact, security,
simplicity, maintainability, and whether the change belongs in the current stage.
Passing automation does not constitute approval.

## Contribution rights and conduct

The open-source licence, contribution-rights process, Code of Conduct, maintainer
model, and public review workflow are not yet approved. They must be resolved
before the project invites external contributions. Until then, do not represent
the repository as ready to accept public contributions.

## Security matters

Do not place suspected vulnerabilities, credentials, personal information,
customer information, or sensitive bank details in a public issue or change.
Follow `SECURITY.md`.
