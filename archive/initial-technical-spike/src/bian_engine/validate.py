from __future__ import annotations

from collections import Counter

from bian_engine.errors import ModelValidationError
from bian_engine.model import ModelSnapshot, Provenance

KNOWN_ARTIFACT_KINDS = {"service-domain", "api-specification", "service-operation"}
KNOWN_RELATIONSHIP_TYPES = {"exposes-api", "contains-operation", "relates-to"}


def _validate_provenance(
    owner_id: str,
    provenance: tuple[Provenance, ...],
    source_digests: dict[str, str],
    errors: list[str],
) -> None:
    if not provenance:
        errors.append(f"{owner_id}: provenance is required")
        return
    for assertion in provenance:
        expected_digest = source_digests.get(assertion.source_id)
        if expected_digest is None:
            errors.append(f"{owner_id}: unknown provenance source {assertion.source_id}")
        elif assertion.source_digest != expected_digest:
            errors.append(f"{owner_id}: provenance digest does not match source record")
        if not assertion.source_item_id:
            errors.append(f"{owner_id}: provenance source item ID is required")
        if not assertion.classification:
            errors.append(f"{owner_id}: provenance classification is required")


def validate_snapshot(snapshot: ModelSnapshot) -> None:
    errors: list[str] = []
    source_ids = [source.source_id for source in snapshot.source_set]
    artifact_ids = [artifact.artifact_id for artifact in snapshot.artifacts]
    relationship_ids = [rel.relationship_id for rel in snapshot.relationships]

    for label, values in (
        ("source", source_ids),
        ("artifact", artifact_ids),
        ("relationship", relationship_ids),
    ):
        duplicates = sorted(value for value, count in Counter(values).items() if count > 1)
        if duplicates:
            errors.append(f"duplicate {label} IDs: {', '.join(duplicates)}")

    source_digests = {source.source_id: source.digest for source in snapshot.source_set}
    artifact_id_set = set(artifact_ids)
    artifacts_by_id = {artifact.artifact_id: artifact for artifact in snapshot.artifacts}

    for artifact in snapshot.artifacts:
        if artifact.kind not in KNOWN_ARTIFACT_KINDS:
            errors.append(f"{artifact.artifact_id}: unknown kind {artifact.kind}")
        if artifact.release != snapshot.bian_release:
            errors.append(f"{artifact.artifact_id}: release differs from snapshot")
        _validate_provenance(artifact.artifact_id, artifact.provenance, source_digests, errors)

    for relationship in snapshot.relationships:
        if relationship.relationship_type not in KNOWN_RELATIONSHIP_TYPES:
            errors.append(
                f"{relationship.relationship_id}: unknown type {relationship.relationship_type}"
            )
        if relationship.source_id not in artifact_id_set:
            errors.append(f"{relationship.relationship_id}: missing source artifact")
        if relationship.target_id not in artifact_id_set:
            errors.append(f"{relationship.relationship_id}: missing target artifact")
        if relationship.release != snapshot.bian_release:
            errors.append(f"{relationship.relationship_id}: release differs from snapshot")
        _validate_provenance(
            relationship.relationship_id,
            relationship.provenance,
            source_digests,
            errors,
        )

    exposed_api_domains = {
        relationship.source_id
        for relationship in snapshot.relationships
        if relationship.relationship_type == "exposes-api"
    }
    for artifact in snapshot.artifacts:
        if artifact.kind != "service-domain":
            continue
        declared = artifact.attributes.get("publishedApiSpecification")
        if not isinstance(declared, bool):
            errors.append(f"{artifact.artifact_id}: publishedApiSpecification must be a boolean")
        elif declared != (artifact.artifact_id in exposed_api_domains):
            errors.append(f"{artifact.artifact_id}: API presence contradicts relationships")

    for relationship in snapshot.relationships:
        if relationship.relationship_type != "contains-operation":
            continue
        source = artifacts_by_id.get(relationship.source_id)
        target = artifacts_by_id.get(relationship.target_id)
        if source is not None and source.kind != "api-specification":
            errors.append(f"{relationship.relationship_id}: operation container is not an API")
        if target is not None and target.kind != "service-operation":
            errors.append(f"{relationship.relationship_id}: contained item is not an operation")

    if errors:
        raise ModelValidationError("Canonical model validation failed:\n- " + "\n- ".join(errors))
