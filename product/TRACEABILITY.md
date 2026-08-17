# Traceability to the original outline

This document ensures the source concept is not silently reduced while product
discovery proceeds.

| Original section | Preserved product definition | Location |
|---|---|---|
| 1. Overall architecture and BIAN Model Registry | Shared trusted knowledge-model foundation | `PRODUCT_VISION.md`, FDN-01 in `USE_CASE_CATALOGUE.md` |
| 2. Treat BIAN as compiler input | UC-01: model-driven engineering artefact generation | `USE_CASE_CATALOGUE.md` |
| 3. Keep generated code and banking logic separate | UC-02: safe regeneration with owned implementation preserved | `USE_CASE_CATALOGUE.md` |
| 4. BIAN release management | UC-03: release impact and upgrade management | `USE_CASE_CATALOGUE.md` |
| 5. Security as a platform layer | UC-04: consistent security profiles | `USE_CASE_CATALOGUE.md` |
| 6. Compliance as evidence | UC-05: evidence-based scoped control assurance | `USE_CASE_CATALOGUE.md` |
| 7. Red Hat Developer Hub as front door | UC-06: developer and architect self-service front door | `USE_CASE_CATALOGUE.md` |
| 8. BIAN Landscape Mapper | UC-07: customer landscape mapping | `USE_CASE_CATALOGUE.md` |
| 9. BIAN API Alignment | UC-08: existing API alignment analysis | `USE_CASE_CATALOGUE.md` |
| 10. Current-state to target-state | UC-09: target design and transition planning | `USE_CASE_CATALOGUE.md` |
| 11. Business Scenario Studio | UC-10: scenarios with customer implementation overlays | `USE_CASE_CATALOGUE.md` |
| 12. BIAN Modernisation Advisor | UC-11: evidence-backed modernisation advice | `USE_CASE_CATALOGUE.md` |
| 13. Vendor/product mapping | UC-12: vendor capability and estate mapping | `USE_CASE_CATALOGUE.md` |
| 14. BIAN architecture governance | UC-13: BIAN-informed design governance | `USE_CASE_CATALOGUE.md` |
| 15. BIAN adoption scorecard | UC-14: multidimensional adoption reporting | `USE_CASE_CATALOGUE.md` |

## Important interpretation

The pasted source contains an overall architectural concept followed by fourteen
product ideas in sections 2–15. This pack therefore treats the Model Registry as
the shared foundation and preserves fourteen customer-facing use cases.

No original idea has been intentionally removed. Some concepts appear in more
than one place because their value emerges through combined journeys:

- the release diff engine supports UC-03 and triggers UC-02;
- generated-vs-owned separation governs UC-01 and UC-02;
- security profiles feed evidence in UC-05;
- RHDH/Backstage is a possible front door for several workflows, not the core;
- mapping underpins alignment, modernisation, governance, and scorecards;
- AI is positioned as an evidence-backed analytical capability within UC-11,
  not a separate generic chatbot.

## Traceability rule for future changes

If a use case is merged, removed, or materially reinterpreted later, record:

- the customer evidence supporting the change;
- what original problem remains covered;
- which journey and capability now owns it; and
- what is explicitly no longer in product scope.

