from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from bian_engine.errors import SourceFormatError
from bian_engine.model import Artifact, ModelSnapshot, Provenance, Relationship, SourceRecord
from bian_engine.serialization import canonical_json_bytes, sha256_bytes
from bian_engine.validate import validate_snapshot

SCHEMA_VERSION = "1.0"


def _required_string(value: dict[str, Any], key: str, context: str) -> str:
    result = value.get(key)
    if not isinstance(result, str) or not result.strip():
        raise SourceFormatError(f"{context}.{key} must be a non-empty string")
    return result


def _optional_string(value: dict[str, Any], key: str, default: str = "") -> str:
    result = value.get(key, default)
    if not isinstance(result, str):
        raise SourceFormatError(f"{key} must be a string")
    return result


def _object(value: Any, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SourceFormatError(f"{context} must be an object")
    return value


def _array(value: Any, context: str) -> list[Any]:
    if not isinstance(value, list):
        raise SourceFormatError(f"{context} must be an array")
    return value


def _relationship_id(rel_type: str, source_id: str, target_id: str) -> str:
    return f"relationship:{rel_type}:{source_id}:{target_id}"


def ingest_fixture(path: Path) -> ModelSnapshot:
    """Import the Phase 1 synthetic JSON envelope into a canonical snapshot."""
    raw = path.read_bytes()
    digest = sha256_bytes(raw)
    try:
        document = _object(json.loads(raw), "document")
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise SourceFormatError(f"Source is not valid UTF-8 JSON: {exc}") from exc

    dataset = _object(document.get("dataset"), "dataset")
    source_id = _required_string(dataset, "id", "dataset")
    release = _required_string(dataset, "bianRelease", "dataset")
    classification = _required_string(dataset, "classification", "dataset")
    if classification != "synthetic-fixture":
        raise SourceFormatError(
            "The fixture adapter only accepts classification 'synthetic-fixture'"
        )

    source = SourceRecord(
        source_id=source_id,
        title=_required_string(dataset, "title", "dataset"),
        classification=classification,
        release=release,
        locator=_required_string(dataset, "locator", "dataset"),
        digest=digest,
        license_status=_required_string(dataset, "licenseStatus", "dataset"),
    )

    artifacts: list[Artifact] = []
    relationships: list[Relationship] = []

    def provenance(item_id: str, location: str) -> tuple[Provenance, ...]:
        return (
            Provenance(
                source_id=source_id,
                source_item_id=item_id,
                source_digest=digest,
                classification=classification,
                source_location=location,
            ),
        )

    domains = _array(document.get("serviceDomains"), "serviceDomains")
    for domain_index, untyped_domain in enumerate(domains):
        location = f"/serviceDomains/{domain_index}"
        domain = _object(untyped_domain, location)
        domain_id = _required_string(domain, "id", location)
        api_value = domain.get("apiSpecification")
        has_api = api_value is not None
        artifacts.append(
            Artifact(
                artifact_id=domain_id,
                kind="service-domain",
                name=_required_string(domain, "name", location),
                description=_optional_string(domain, "description"),
                lifecycle_status=_optional_string(domain, "lifecycleStatus", "published"),
                release=release,
                attributes={"publishedApiSpecification": has_api},
                provenance=provenance(domain_id, location),
            )
        )
        if not has_api:
            continue

        api = _object(api_value, f"{location}/apiSpecification")
        api_id = _required_string(api, "id", f"{location}/apiSpecification")
        api_location = f"{location}/apiSpecification"
        artifacts.append(
            Artifact(
                artifact_id=api_id,
                kind="api-specification",
                name=_required_string(api, "name", api_location),
                description=_optional_string(api, "description"),
                lifecycle_status=_optional_string(api, "lifecycleStatus", "published"),
                release=release,
                attributes={
                    "specificationFormat": _required_string(
                        api, "specificationFormat", api_location
                    ),
                    "specificationVersion": _required_string(
                        api, "specificationVersion", api_location
                    ),
                },
                provenance=provenance(api_id, api_location),
            )
        )
        relationships.append(
            Relationship(
                relationship_id=_relationship_id("exposes-api", domain_id, api_id),
                relationship_type="exposes-api",
                source_id=domain_id,
                target_id=api_id,
                release=release,
                provenance=provenance(api_id, api_location),
            )
        )

        operations = _array(api.get("operations", []), f"{api_location}/operations")
        for operation_index, untyped_operation in enumerate(operations):
            operation_location = f"{api_location}/operations/{operation_index}"
            operation = _object(untyped_operation, operation_location)
            operation_id = _required_string(operation, "id", operation_location)
            artifacts.append(
                Artifact(
                    artifact_id=operation_id,
                    kind="service-operation",
                    name=_required_string(operation, "name", operation_location),
                    description=_optional_string(operation, "description"),
                    lifecycle_status="published",
                    release=release,
                    attributes={
                        "httpMethod": _required_string(
                            operation, "httpMethod", operation_location
                        ).upper(),
                        "path": _required_string(operation, "path", operation_location),
                    },
                    provenance=provenance(operation_id, operation_location),
                )
            )
            relationships.append(
                Relationship(
                    relationship_id=_relationship_id("contains-operation", api_id, operation_id),
                    relationship_type="contains-operation",
                    source_id=api_id,
                    target_id=operation_id,
                    release=release,
                    provenance=provenance(operation_id, operation_location),
                )
            )

    for relationship_index, untyped_relationship in enumerate(
        _array(document.get("relationships", []), "relationships")
    ):
        location = f"/relationships/{relationship_index}"
        item = _object(untyped_relationship, location)
        rel_type = _required_string(item, "type", location)
        source_artifact_id = _required_string(item, "sourceId", location)
        target_artifact_id = _required_string(item, "targetId", location)
        item_id = _required_string(item, "id", location)
        relationships.append(
            Relationship(
                relationship_id=item_id,
                relationship_type=rel_type,
                source_id=source_artifact_id,
                target_id=target_artifact_id,
                release=release,
                attributes=_object(item.get("attributes", {}), f"{location}/attributes"),
                provenance=provenance(item_id, location),
            )
        )

    sorted_artifacts = tuple(sorted(artifacts, key=lambda item: item.artifact_id))
    sorted_relationships = tuple(sorted(relationships, key=lambda item: item.relationship_id))
    provisional = ModelSnapshot(
        schema_version=SCHEMA_VERSION,
        snapshot_id="",
        bian_release=release,
        source_set=(source,),
        artifacts=sorted_artifacts,
        relationships=sorted_relationships,
    )
    snapshot_id = "sha256:" + sha256_bytes(
        canonical_json_bytes(provisional.to_dict(include_snapshot_id=False))
    )
    snapshot = ModelSnapshot(
        schema_version=SCHEMA_VERSION,
        snapshot_id=snapshot_id,
        bian_release=release,
        source_set=(source,),
        artifacts=sorted_artifacts,
        relationships=sorted_relationships,
    )
    validate_snapshot(snapshot)
    return snapshot
