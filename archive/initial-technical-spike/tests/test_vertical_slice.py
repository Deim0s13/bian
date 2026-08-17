from __future__ import annotations

import json
import tempfile
import unittest
from contextlib import redirect_stdout
from dataclasses import replace
from io import StringIO
from pathlib import Path

from bian_engine.cli import main
from bian_engine.errors import ModelValidationError
from bian_engine.generate import build_outputs
from bian_engine.ingest import ingest_fixture
from bian_engine.serialization import sha256_bytes
from bian_engine.validate import validate_snapshot

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "synthetic" / "r14-small.json"


class VerticalSliceTests(unittest.TestCase):
    def test_ingestion_and_generation_are_byte_deterministic(self) -> None:
        first_snapshot = ingest_fixture(FIXTURE)
        second_snapshot = ingest_fixture(FIXTURE)
        self.assertEqual(first_snapshot, second_snapshot)

        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            build_outputs(first_snapshot, Path(first))
            build_outputs(second_snapshot, Path(second))
            for filename in ("model.json", "catalog-summary.md", "build-manifest.json"):
                self.assertEqual(
                    (Path(first) / filename).read_bytes(),
                    (Path(second) / filename).read_bytes(),
                    filename,
                )

    def test_every_graph_element_retains_source_provenance(self) -> None:
        snapshot = ingest_fixture(FIXTURE)
        expected_digest = sha256_bytes(FIXTURE.read_bytes())
        self.assertEqual(snapshot.source_set[0].digest, expected_digest)
        for item in (*snapshot.artifacts, *snapshot.relationships):
            self.assertTrue(item.provenance, item)
            for assertion in item.provenance:
                self.assertEqual(assertion.source_id, snapshot.source_set[0].source_id)
                self.assertEqual(assertion.source_digest, expected_digest)
                self.assertEqual(assertion.classification, "synthetic-fixture")
                self.assertTrue(assertion.source_location)

    def test_validation_rejects_provenance_loss(self) -> None:
        snapshot = ingest_fixture(FIXTURE)
        damaged_artifact = replace(snapshot.artifacts[0], provenance=())
        damaged = replace(snapshot, artifacts=(damaged_artifact, *snapshot.artifacts[1:]))
        with self.assertRaisesRegex(ModelValidationError, "provenance is required"):
            validate_snapshot(damaged)

    def test_domain_without_api_does_not_gain_generated_semantics(self) -> None:
        snapshot = ingest_fixture(FIXTURE)
        fraud_id = "fixture:service-domain:fraud-evaluation"
        fraud_domain = next(item for item in snapshot.artifacts if item.artifact_id == fraud_id)
        self.assertFalse(fraud_domain.attributes["publishedApiSpecification"])
        self.assertFalse(
            any(
                relationship.relationship_type == "exposes-api"
                and relationship.source_id == fraud_id
                for relationship in snapshot.relationships
            )
        )

    def test_manifest_digests_match_generated_files(self) -> None:
        snapshot = ingest_fixture(FIXTURE)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            build_outputs(snapshot, output)
            manifest = json.loads((output / "build-manifest.json").read_text())
            for record in manifest["outputs"]:
                generated_digest = sha256_bytes((output / record["path"]).read_bytes())
                self.assertEqual(generated_digest, record["sha256"])

    def test_cli_inspect_exposes_relationships_deterministically(self) -> None:
        arguments = ["inspect", "--source", str(FIXTURE), "--view", "relationships"]
        first_stdout = StringIO()
        second_stdout = StringIO()
        with redirect_stdout(first_stdout):
            self.assertEqual(main(arguments), 0)
        with redirect_stdout(second_stdout):
            self.assertEqual(main(arguments), 0)
        first = first_stdout.getvalue()
        second = second_stdout.getvalue()
        self.assertEqual(first, second)
        payload = json.loads(first)
        self.assertIn("relationships", payload)
        self.assertTrue(payload["relationships"])


if __name__ == "__main__":
    unittest.main()
