from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from bian_engine.errors import EngineError
from bian_engine.generate import build_outputs
from bian_engine.ingest import ingest_fixture
from bian_engine.serialization import canonical_json_bytes


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bian-engine",
        description="Import, validate, and project a canonical BIAN-shaped model.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="Build deterministic model outputs")
    build.add_argument("--source", type=Path, required=True, help="Synthetic fixture path")
    build.add_argument("--output", type=Path, required=True, help="Generated output directory")

    validate = subparsers.add_parser("validate", help="Validate a synthetic source")
    validate.add_argument("--source", type=Path, required=True, help="Synthetic fixture path")

    inspect = subparsers.add_parser("inspect", help="Print a deterministic canonical view")
    inspect.add_argument("--source", type=Path, required=True, help="Synthetic fixture path")
    inspect.add_argument(
        "--view",
        choices=("metadata", "artifacts", "relationships", "snapshot"),
        default="metadata",
        help="Canonical content to print",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        snapshot = ingest_fixture(args.source)
        if args.command == "validate":
            print(f"valid {snapshot.snapshot_id}")
            return 0
        if args.command == "inspect":
            snapshot_value = snapshot.to_dict()
            views = {
                "metadata": {
                    "schemaVersion": snapshot.schema_version,
                    "snapshotId": snapshot.snapshot_id,
                    "bianRelease": snapshot.bian_release,
                    "sourceSet": snapshot_value["sourceSet"],
                },
                "artifacts": {
                    "snapshotId": snapshot.snapshot_id,
                    "artifacts": snapshot_value["artifacts"],
                },
                "relationships": {
                    "snapshotId": snapshot.snapshot_id,
                    "relationships": snapshot_value["relationships"],
                },
                "snapshot": snapshot_value,
            }
            sys.stdout.write(canonical_json_bytes(views[args.view]).decode("utf-8"))
            return 0
        digests = build_outputs(snapshot, args.output)
        print(f"built {snapshot.snapshot_id}")
        for path, digest in sorted(digests.items()):
            print(f"{digest}  {path}")
        return 0
    except (EngineError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
