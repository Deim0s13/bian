# ADR-0003: Begin with a Python modular monolith

- Status: Accepted
- Date: 2026-08-17

## Context

The first challenge is parsing, modelling, validating, diffing, and generating
structured artefacts. A solo/small team needs fast iteration and simple tests,
not distributed operations.

## Decision

Use Python 3.11+ for a framework-neutral core and application layer. Use the
standard library for the initial executable and CLI. Add a thin FastAPI adapter
only when an HTTP service is needed. Package boundaries represent components;
do not deploy them as microservices initially.

## Consequences

The engine has low setup cost, strong data tooling options, and easy portability.
Runtime type enforcement is explicit rather than compiler-enforced. If future
high-throughput generation warrants another language, the canonical JSON and
ports provide a migration boundary.

