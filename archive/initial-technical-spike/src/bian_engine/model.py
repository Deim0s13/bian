from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    title: str
    classification: str
    release: str
    locator: str
    digest: str
    license_status: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "sourceId": self.source_id,
            "title": self.title,
            "classification": self.classification,
            "release": self.release,
            "locator": self.locator,
            "digest": self.digest,
            "licenseStatus": self.license_status,
        }


@dataclass(frozen=True)
class Provenance:
    source_id: str
    source_item_id: str
    source_digest: str
    classification: str
    source_location: str | None = None

    def to_dict(self) -> dict[str, Any]:
        value: dict[str, Any] = {
            "sourceId": self.source_id,
            "sourceItemId": self.source_item_id,
            "sourceDigest": self.source_digest,
            "classification": self.classification,
        }
        if self.source_location is not None:
            value["sourceLocation"] = self.source_location
        return value


@dataclass(frozen=True)
class Artifact:
    artifact_id: str
    kind: str
    name: str
    description: str
    lifecycle_status: str
    release: str
    attributes: dict[str, Any] = field(default_factory=dict)
    provenance: tuple[Provenance, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.artifact_id,
            "kind": self.kind,
            "name": self.name,
            "description": self.description,
            "lifecycleStatus": self.lifecycle_status,
            "release": self.release,
            "attributes": self.attributes,
            "provenance": [item.to_dict() for item in self.provenance],
        }


@dataclass(frozen=True)
class Relationship:
    relationship_id: str
    relationship_type: str
    source_id: str
    target_id: str
    release: str
    attributes: dict[str, Any] = field(default_factory=dict)
    provenance: tuple[Provenance, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.relationship_id,
            "type": self.relationship_type,
            "sourceId": self.source_id,
            "targetId": self.target_id,
            "release": self.release,
            "attributes": self.attributes,
            "provenance": [item.to_dict() for item in self.provenance],
        }


@dataclass(frozen=True)
class ModelSnapshot:
    schema_version: str
    snapshot_id: str
    bian_release: str
    source_set: tuple[SourceRecord, ...]
    artifacts: tuple[Artifact, ...]
    relationships: tuple[Relationship, ...]

    def to_dict(self, *, include_snapshot_id: bool = True) -> dict[str, Any]:
        value: dict[str, Any] = {
            "schemaVersion": self.schema_version,
            "bianRelease": self.bian_release,
            "sourceSet": [item.to_dict() for item in self.source_set],
            "artifacts": [item.to_dict() for item in self.artifacts],
            "relationships": [item.to_dict() for item in self.relationships],
        }
        if include_snapshot_id:
            value["snapshotId"] = self.snapshot_id
        return value
