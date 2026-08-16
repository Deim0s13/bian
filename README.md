# BIAN Adoption & Engineering Platform

This repository contains the architecture and first executable slice of a
model-first BIAN engineering platform. The current code is intentionally
small: it imports a clearly labelled synthetic, BIAN-shaped fixture into a
canonical model, validates it, and produces deterministic outputs.

It does **not** contain or redistribute official BIAN artefacts, and it does
not claim that fixture operations are BIAN-defined semantics.

## Quick start

Requires Python 3.11 or newer and has no runtime dependencies.

```bash
PYTHONPATH=src python -m bian_engine build \
  --source fixtures/synthetic/r14-small.json \
  --output out
PYTHONPATH=src python -m unittest discover -s tests -v
```

Inspect canonical metadata or relationships without generating files:

```bash
PYTHONPATH=src python -m bian_engine inspect \
  --source fixtures/synthetic/r14-small.json \
  --view relationships
```

The build creates:

- `out/model.json` — the canonical snapshot;
- `out/catalog-summary.md` — a generated human-readable projection; and
- `out/build-manifest.json` — input and output digests for reproducibility.

See [PRODUCT.md](PRODUCT.md), [ARCHITECTURE.md](ARCHITECTURE.md), and the
[ADRs](docs/adr/README.md) before expanding the implementation.
# bian
