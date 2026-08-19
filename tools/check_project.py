#!/usr/bin/env python3
"""Run dependency-free policy checks for active project files."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {
    ".git",
    ".venv",
    "archive",
    "node_modules",
    "out",
    "sources",
}
TEXT_SUFFIXES = {".json", ".md", ".py", ".toml", ".txt", ".yaml", ".yml"}
REQUIRED_FILES = (
    "AGENTS.md",
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "architecture/README.md",
    "architecture/ARCHITECTURE_VISION.md",
    "architecture/BUSINESS_ARCHITECTURE.md",
    "architecture/REQUIREMENTS_AND_TRACEABILITY.md",
    "architecture/INFORMATION_SYSTEMS_ARCHITECTURE.md",
    "architecture/DATA_ARCHITECTURE.md",
    "architecture/PHASE_C_MODEL_VALIDATION.md",
    "architecture/PHASE_C_TRACEABILITY.md",
    "architecture/ADM_TAILORING.md",
    "architecture/TRUST_BOUNDARY_AND_SECURITY_ARCHITECTURE.md",
    "architecture/ARCHITECTURE_LIFECYCLE.md",
    "governance/PROJECT_STATUS.md",
    "governance/ARCHITECTURE_REGISTER.md",
    "governance/PROJECT_CONTEXT.md",
    "governance/WRITING_STYLE.md",
    "governance/GLOSSARY.md",
    "governance/ARCHITECTURE_AND_ENGINEERING_PRINCIPLES.md",
    "governance/QUALITY_AND_REVIEW.md",
    "governance/DECISION_LOG.md",
    "governance/OPEN_QUESTIONS.md",
    "product/BIAN_ALIGNMENT_POLICY.md",
    "product/PROJECT_PRINCIPLES.md",
    "product/VALUE_AND_VALIDATION.md",
)
REQUIRED_CONTENT = {
    "AGENTS.md": (
        "Keep governance proportionate to the decisions and evidence it improves",
    ),
    "README.md": ("BIAN Adoption & Engineering Platform", "BIAN Model Registry"),
    "product/PRODUCT_VISION.md": (
        "BIAN Adoption & Engineering Platform",
        "BIAN Sources",
        "BIAN Model Registry",
        "Service Generator",
        "Adoption & Architecture",
        "Assurance & Compliance",
        "Platform Control",
        "Runtime Targets",
    ),
    "architecture/ARCHITECTURE_VISION.md": (
        "BIAN Adoption & Engineering Platform",
        "BIAN Sources",
        "BIAN Model Registry",
        "Service Generator",
        "Adoption & Architecture",
        "Assurance & Compliance",
        "Platform Control",
        "Runtime Targets",
    ),
    "architecture/BUSINESS_ARCHITECTURE.md": (
        "Business Architecture proposition",
        "Connected value flow",
        "Platform capability map",
        "Capability investment hypothesis",
        "Value-stream to capability cross-map",
        "Platform business services",
        "Accepted working proposition and decision boundary",
        "Business Architecture requirements",
        "Initial HSB business scenario",
        "Failure and stop signals",
    ),
    "architecture/REQUIREMENTS_AND_TRACEABILITY.md": (
        "sole authoritative record",
        "REQ-001",
        "REQ-025",
        "DEC-030",
        "Requirement quality tests",
        "Initial relationship to trust and security architecture",
        "Lifecycle and change control",
    ),
    "architecture/INFORMATION_SYSTEMS_ARCHITECTURE.md": (
        "Information Systems Architecture",
        "Data and Application Architecture boundary",
        "Stage review criteria",
        "DAR-028",
    ),
    "architecture/DATA_ARCHITECTURE.md": (
        "Conceptual Data Architecture",
        "Relationship assertion",
        "Authority and truth classification",
        "Explicit non-decisions",
        "DAR-017",
        "DAR-028",
        "View definition",
        "View materialisation",
    ),
    "architecture/PHASE_C_MODEL_VALIDATION.md": (
        "Phase C model validation",
        "Entity and record type catalogue exercised",
        "SUBJ-PRJ-BIAN-SCOPE-001",
        "VIEWDEF-HSB-001",
        "EVD-011",
    ),
    "architecture/PHASE_C_TRACEABILITY.md": (
        "Phase C gap and traceability analysis",
        "Phase C baseline-to-target gap analysis",
        "Information domain to platform capability matrix",
        "Information domain by role and authority matrix",
        "First-proposition depth",
    ),
    "architecture/ADM_TAILORING.md": (
        "ADM tailoring statement",
        "Work products produced",
        "Deliberately consolidated work products",
        "Deliberately deferred or omitted work products",
        "DEC-025",
    ),
    "architecture/TRUST_BOUNDARY_AND_SECURITY_ARCHITECTURE.md": (
        "Trust-boundary and security architecture",
        "Protected information and assets",
        "Logical trust zones",
        "Lifecycle boundaries outside the runtime zone model",
        "Trust-boundary catalogue",
        "Identity, access and decision authority",
        "Privacy position",
        "Threat and abuse-case analysis",
        "TB-11",
        "THR-15",
        "Unclassified",
        "HSB negative security scenarios",
        "Explicit non-decisions",
        "EVD-012",
    ),
    "architecture/ARCHITECTURE_LIFECYCLE.md": (
        "Architecture lifecycle and ADM tailoring",
        "Phase D: Technology Architecture plan",
        "Phase E: Opportunities and Solutions plan",
        "Phase F: Migration Planning plan",
        "Phase G: Implementation Governance plan",
        "Phase H: Architecture Change Management plan",
        "Iteration and improvement model",
        "GAT-016",
    ),
    "product/PROJECT_PRINCIPLES.md": (
        "authoritative catalogue",
        "PRN-001",
        "PRN-017",
        "Governing decision rule",
    ),
    "product/VALUE_AND_VALIDATION.md": (
        "Continue product discovery and conceptual architecture",
        "Primary value hypothesis",
        "Existing alternatives and market constraints",
        "Minimum consumable product hypothesis",
        "Validation tests",
        "Stop or narrow conditions",
        "Build-authorisation gate",
    ),
    "governance/PROJECT_STATUS.md": (
        "not to authorise a full platform build",
        "Connected decision value",
    ),
    "governance/GLOSSARY.md": (
        "authoritative glossary",
        "Accountable owner",
        "ADM cycle",
        "Architecture baseline",
        "Delivery horizon",
        "Material",
        "Solution Architecture",
        "Supported export",
        "Subject",
        "Technology Architecture",
        "Transition architecture",
        "Truth class",
        "View Definition",
        "View materialisation",
    ),
    "governance/ARCHITECTURE_REGISTER.md": (
        "single canonical control record",
        "## Decisions",
        "DEC-015",
        "DEC-016",
        "DEC-018",
        "DEC-019",
        "DEC-020",
        "DEC-021",
        "DEC-022",
        "DEC-023",
        "DEC-024",
        "DEC-025",
        "DEC-026",
        "DEC-027",
        "DEC-028",
        "DEC-029",
        "GAT-001",
        "GAT-011",
        "GAT-012",
        "GAT-016",
        "ROL-001",
        "ROL-013",
        "## Open questions",
        "## Risks",
        "## Assumptions",
        "## Dependencies",
        "## Evidence gaps",
        "## Requirements",
        "REQ-025",
        "BAR-014",
        "DAR-017",
        "DAR-028",
        "OQ-038",
        "OQ-039",
        "OQ-041",
        "OQ-047",
        "OQ-049",
        "OQ-051",
        "OQ-052",
        "RSK-023",
        "RSK-024",
        "RSK-028",
        "RSK-032",
        "RSK-035",
        "RSK-038",
        "RSK-041",
        "EVD-013",
        "## Work items",
        "WRK-014",
        "WRK-018",
        "WRK-019",
        "WRK-020",
        "WRK-021",
        "WRK-024",
        "WRK-027",
        "WRK-034",
        "WRK-040",
        "WRK-042",
        "## Issues",
    ),
    "governance/DECISION_LOG.md": (
        "compatibility pointer",
        "Architecture Register",
    ),
    "governance/OPEN_QUESTIONS.md": (
        "compatibility pointer",
        "Architecture Register",
    ),
}
FORBIDDEN_PHRASES = (
    "BIAN Adoption & " + "Transformation Platform",
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
GOVERNED_ID = re.compile(
    r"\b(?:GAT|ROL|DEC|OQ|RSK|ASM|DEP|EVD|REQ|BAR|DAR|WRK|ISS)-\d{3}\b"
)
REGISTER_ROW = re.compile(
    r"^\| ((?:GAT|ROL|DEC|OQ|RSK|ASM|DEP|EVD|REQ|BAR|DAR|WRK|ISS)-\d{3}) \|",
    re.MULTILINE,
)
PRINCIPLE_ID = re.compile(r"\bPRN-\d{3}\b")
PRINCIPLE_HEADING = re.compile(r"^## (PRN-\d{3}):", re.MULTILINE)
REGISTER_PIPE_COUNTS = {
    "GAT": 9,
    "ROL": 7,
    "DEC": 9,
    "OQ": 8,
    "RSK": 11,
    "ASM": 8,
    "DEP": 9,
    "EVD": 9,
    "REQ": 11,
    "BAR": 10,
    "DAR": 10,
    "WRK": 8,
    "ISS": 8,
}
DAR_HORIZONS = {
    "GAT-004",
    "GAT-005",
    "GAT-006",
    "GAT-008",
    "GAT-010",
}
RISK_RATINGS = {"Low", "Medium", "High"}
STATUS_VALUES = {
    "GAT": {
        "Not started",
        "In progress",
        "Passed",
        "Failed",
        "Revisit required",
        "Continuous",
    },
    "DEC": {"Accepted", "Declined", "Revisit required", "Superseded"},
    "OQ": {"Open", "In analysis", "Answered", "Deferred"},
    "RSK": {"Open", "Mitigating", "Accepted", "Closed"},
    "ASM": {"Untested", "Supported", "Invalidated"},
    "DEP": {"Unmet", "In progress", "Met", "Removed"},
    "EVD": {"Open", "Partial", "Closed", "Not obtainable"},
    "REQ": {"Proposed", "Accepted", "Deferred", "Rejected", "Superseded"},
    "BAR": {"Proposed", "Accepted", "Deferred", "Rejected", "Superseded"},
    "DAR": {"Proposed", "Accepted", "Deferred", "Rejected", "Superseded"},
    "WRK": {"Planned", "In progress", "Blocked", "Complete", "Cancelled"},
    "ISS": {"Open", "In progress", "Resolved", "Closed"},
}
STATUS_FIELD_INDEX = {
    "GAT": 6,
    "DEC": 6,
    "OQ": 3,
    "RSK": 7,
    "ASM": 4,
    "DEP": 4,
    "EVD": 4,
    "REQ": 5,
    "BAR": 4,
    "DAR": 4,
    "WRK": 4,
    "ISS": 4,
}
OWNER_FIELD_INDEX = {
    "GAT": 2,
    "DEC": 5,
    "OQ": 2,
    "RSK": 6,
    "ASM": 3,
    "DEP": 3,
    "EVD": 3,
    "REQ": 4,
    "BAR": 3,
    "DAR": 3,
    "WRK": 3,
}
EM_DASH = chr(0x2014)


def active_text_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in TEXT_SUFFIXES
        and not EXCLUDED_PARTS.intersection(path.relative_to(ROOT).parts)
    )


def check_required_files(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")


def check_agents_size(errors: list[str]) -> None:
    agents = ROOT / "AGENTS.md"
    if agents.is_file() and agents.stat().st_size > 32 * 1024:
        errors.append("AGENTS.md exceeds the default 32 KiB Codex instruction limit")


def check_required_content(errors: list[str]) -> None:
    for relative, required_phrases in REQUIRED_CONTENT.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(f"{relative}: missing required project concept: {phrase}")


def check_text(path: Path, errors: list[str]) -> str | None:
    relative = path.relative_to(ROOT)
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        errors.append(f"{relative}: not valid UTF-8 ({exc})")
        return None

    for line_number, line in enumerate(text.splitlines(), start=1):
        if EM_DASH in line:
            errors.append(f"{relative}:{line_number}: Unicode em dash is not permitted")
        for phrase in FORBIDDEN_PHRASES:
            if phrase in line:
                errors.append(
                    f"{relative}:{line_number}: legacy product name is not permitted"
                )
        if line.rstrip(" \t") != line:
            errors.append(f"{relative}:{line_number}: trailing whitespace")

    if text and not text.endswith("\n"):
        errors.append(f"{relative}: missing final newline")

    return text


def check_markdown_links(path: Path, text: str, errors: list[str]) -> None:
    for match in MARKDOWN_LINK.finditer(text):
        raw_target = match.group(1).strip()
        if not raw_target or raw_target.startswith(("#", "<http", "http", "mailto:")):
            continue

        target_text = raw_target.split(maxsplit=1)[0].strip("<>")
        target_text = unquote(target_text.split("#", maxsplit=1)[0])
        if not target_text or "://" in target_text:
            continue

        target = (path.parent / target_text).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(
                f"{path.relative_to(ROOT)}: local link escapes repository: {raw_target}"
            )
            continue

        if not target.exists():
            errors.append(
                f"{path.relative_to(ROOT)}: broken local link: {raw_target}"
            )


def check_architecture_register(files: list[Path], errors: list[str]) -> None:
    register_path = ROOT / "governance/ARCHITECTURE_REGISTER.md"
    if not register_path.is_file():
        return

    register_text = register_path.read_text(encoding="utf-8")
    definitions = REGISTER_ROW.findall(register_text)
    defined_ids = set(definitions)

    for identifier in sorted(defined_ids):
        if definitions.count(identifier) > 1:
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md: "
                f"duplicate governed record definition: {identifier}"
            )

    for line_number, line in enumerate(register_text.splitlines(), start=1):
        match = REGISTER_ROW.match(line)
        if not match:
            continue
        prefix = match.group(1).split("-", maxsplit=1)[0]
        expected = REGISTER_PIPE_COUNTS[prefix]
        actual = line.count("|")
        if actual != expected:
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {match.group(1)} has {actual - 1} fields; "
                f"expected {expected - 1}"
            )

    for path in files:
        if path.suffix.lower() != ".md" or path == register_path:
            continue
        text = path.read_text(encoding="utf-8")
        for identifier in sorted(set(GOVERNED_ID.findall(text))):
            if identifier not in defined_ids:
                errors.append(
                    f"{path.relative_to(ROOT)}: undefined Architecture Register "
                    f"reference: {identifier}"
                )

    for relative in (
        "governance/DECISION_LOG.md",
        "governance/OPEN_QUESTIONS.md",
    ):
        path = ROOT / relative
        if path.is_file() and REGISTER_ROW.search(path.read_text(encoding="utf-8")):
            errors.append(
                f"{relative}: governed records must be defined only in "
                "governance/ARCHITECTURE_REGISTER.md"
            )


def check_data_architecture_requirements(errors: list[str]) -> None:
    register_path = ROOT / "governance/ARCHITECTURE_REGISTER.md"
    if not register_path.is_file():
        return

    for line_number, line in enumerate(
        register_path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.startswith("| DAR-"):
            continue

        fields = [field.strip() for field in line.strip("|").split("|")]
        if len(fields) != 9:
            continue

        identifier, requirement, _, owner, status, horizon, _, related, _ = fields
        lower_requirement = requirement.lower()
        for phrase in ("as applicable", "where applicable"):
            if phrase in lower_requirement:
                errors.append(
                    "governance/ARCHITECTURE_REGISTER.md:"
                    f"{line_number}: {identifier} uses discretionary qualifier: "
                    f"{phrase}"
                )
        if re.search(r"\bmaterial\b", lower_requirement):
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {identifier} must use an explicit scope rule "
                "instead of material"
            )
        if " and " in owner.lower() or "&" in owner:
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {identifier} must have one accountable owner"
            )
        horizon_identifier = horizon.strip("`")
        if horizon_identifier not in DAR_HORIZONS:
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {identifier} has unknown delivery horizon: "
                f"{horizon}"
            )
        if status == "Deferred" and horizon_identifier in {"GAT-006", "GAT-008"}:
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {identifier} is deferred but assigned to {horizon}"
            )
        if not related:
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {identifier} has no related-record traceability"
            )


def check_crosscutting_requirements(errors: list[str]) -> None:
    register_path = ROOT / "governance/ARCHITECTURE_REGISTER.md"
    if not register_path.is_file():
        return

    for line_number, line in enumerate(
        register_path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.startswith("| REQ-"):
            continue

        fields = [field.strip() for field in line.strip("|").split("|")]
        if len(fields) != 10 or fields[5] != "Accepted":
            continue

        identifier, requirement = fields[0], fields[2]
        lower_requirement = requirement.lower()
        for phrase in (
            "as applicable",
            "where applicable",
            "appropriate to that state",
            "within the maintained scope",
        ):
            if phrase in lower_requirement:
                errors.append(
                    "governance/ARCHITECTURE_REGISTER.md:"
                    f"{line_number}: {identifier} uses an unbounded qualifier: "
                    f"{phrase}"
                )
        if re.search(r"\bproportionate\b", lower_requirement):
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {identifier} uses proportionate without an "
                "explicit scope rule"
            )


def check_register_controls(errors: list[str]) -> None:
    register_path = ROOT / "governance/ARCHITECTURE_REGISTER.md"
    if not register_path.is_file():
        return

    rows: list[tuple[int, list[str]]] = []
    for line_number, line in enumerate(
        register_path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if REGISTER_ROW.match(line):
            rows.append(
                (line_number, [field.strip() for field in line.strip("|").split("|")])
            )

    canonical_roles = {
        fields[1] for _, fields in rows if fields[0].startswith("ROL-")
    }
    canonical_gates = {
        fields[0] for _, fields in rows if fields[0].startswith("GAT-")
    }
    for line_number, fields in rows:
        identifier = fields[0]
        prefix = identifier.split("-", maxsplit=1)[0]
        owner_index = OWNER_FIELD_INDEX.get(prefix)
        if owner_index is not None and fields[owner_index] not in canonical_roles:
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {identifier} uses non-canonical owner: "
                f"{fields[owner_index]}"
            )

        status_index = STATUS_FIELD_INDEX.get(prefix)
        if (
            status_index is not None
            and fields[status_index] not in STATUS_VALUES[prefix]
        ):
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {identifier} has invalid status: "
                f"{fields[status_index]}"
            )

        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fields[-1]):
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {identifier} has invalid last-reviewed date: "
                f"{fields[-1]}"
            )

        if prefix == "RSK":
            for label, rating in (("likelihood", fields[3]), ("impact", fields[4])):
                if rating not in RISK_RATINGS:
                    errors.append(
                        "governance/ARCHITECTURE_REGISTER.md:"
                        f"{line_number}: {identifier} has invalid {label}: {rating}"
                    )
            if fields[7] == "Accepted" and not re.search(
                r"\bDEC-\d{3}\b", fields[5]
            ):
                errors.append(
                    "governance/ARCHITECTURE_REGISTER.md:"
                    f"{line_number}: {identifier} is accepted without a recorded "
                    "decision reference"
                )

        related_index = {"DEP": 6, "REQ": 8, "BAR": 7, "DAR": 7}.get(prefix)
        if related_index is not None and not fields[related_index]:
            errors.append(
                "governance/ARCHITECTURE_REGISTER.md:"
                f"{line_number}: {identifier} has no related-record traceability"
            )

        gate_index = {
            "OQ": 4,
            "RSK": 8,
            "ASM": 5,
            "DEP": 5,
            "EVD": 6,
            "REQ": 6,
            "BAR": 5,
            "DAR": 5,
        }.get(prefix)
        if gate_index is not None:
            gate_references = set(re.findall(r"\bGAT-\d{3}\b", fields[gate_index]))
            if not gate_references:
                errors.append(
                    "governance/ARCHITECTURE_REGISTER.md:"
                    f"{line_number}: {identifier} has no canonical gate reference"
                )
            for gate_reference in sorted(gate_references - canonical_gates):
                errors.append(
                    "governance/ARCHITECTURE_REGISTER.md:"
                    f"{line_number}: {identifier} references unknown canonical gate: "
                    f"{gate_reference}"
                )


def check_project_principles(files: list[Path], errors: list[str]) -> None:
    principles_path = ROOT / "product/PROJECT_PRINCIPLES.md"
    if not principles_path.is_file():
        return

    principles_text = principles_path.read_text(encoding="utf-8")
    definitions = PRINCIPLE_HEADING.findall(principles_text)
    defined_ids = set(definitions)

    for identifier in sorted(defined_ids):
        if definitions.count(identifier) > 1:
            errors.append(
                "product/PROJECT_PRINCIPLES.md: "
                f"duplicate principle definition: {identifier}"
            )

    for path in files:
        if path.suffix.lower() != ".md" or path == principles_path:
            continue
        text = path.read_text(encoding="utf-8")
        for identifier in sorted(set(PRINCIPLE_ID.findall(text))):
            if identifier not in defined_ids:
                errors.append(
                    f"{path.relative_to(ROOT)}: undefined project principle "
                    f"reference: {identifier}"
                )


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_agents_size(errors)
    check_required_content(errors)

    files = active_text_files()
    check_architecture_register(files, errors)
    check_data_architecture_requirements(errors)
    check_crosscutting_requirements(errors)
    check_register_controls(errors)
    check_project_principles(files, errors)
    for path in files:
        text = check_text(path, errors)
        if text is not None and path.suffix.lower() == ".md":
            check_markdown_links(path, text, errors)

    if errors:
        print("Project checks failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Project checks passed for {len(files)} active text files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
