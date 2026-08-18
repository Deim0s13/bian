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
    "governance/PROJECT_STATUS.md",
    "governance/ARCHITECTURE_REGISTER.md",
    "governance/PROJECT_CONTEXT.md",
    "governance/WRITING_STYLE.md",
    "governance/ARCHITECTURE_AND_ENGINEERING_PRINCIPLES.md",
    "governance/QUALITY_AND_REVIEW.md",
    "governance/DECISION_LOG.md",
    "governance/OPEN_QUESTIONS.md",
    "product/BIAN_ALIGNMENT_POLICY.md",
    "product/PROJECT_PRINCIPLES.md",
    "product/VALUE_AND_VALIDATION.md",
)
REQUIRED_CONTENT = {
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
        "Initial Business Architecture requirements",
        "Initial HSB business scenario",
        "Failure and stop signals",
    ),
    "architecture/REQUIREMENTS_AND_TRACEABILITY.md": (
        "sole authoritative record",
        "REQ-001",
        "REQ-020",
        "Requirement quality tests",
        "Lifecycle and change control",
    ),
    "architecture/INFORMATION_SYSTEMS_ARCHITECTURE.md": (
        "Information Systems Architecture",
        "Data and Application Architecture boundary",
        "Stage review criteria",
        "DAR-017",
    ),
    "architecture/DATA_ARCHITECTURE.md": (
        "Conceptual Data Architecture",
        "Relationship assertion",
        "Authority and truth classification",
        "Explicit non-decisions",
        "DAR-017",
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
    "governance/ARCHITECTURE_REGISTER.md": (
        "single canonical control record",
        "## Decisions",
        "DEC-015",
        "DEC-016",
        "DEC-018",
        "DEC-019",
        "## Open questions",
        "## Risks",
        "## Assumptions",
        "## Dependencies",
        "## Evidence gaps",
        "## Requirements",
        "REQ-020",
        "BAR-014",
        "DAR-017",
        "OQ-038",
        "RSK-023",
        "## Work items",
        "WRK-014",
        "WRK-018",
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
    r"\b(?:DEC|OQ|RSK|ASM|DEP|EVD|REQ|BAR|DAR|WRK|ISS)-\d{3}\b"
)
REGISTER_ROW = re.compile(
    r"^\| ((?:DEC|OQ|RSK|ASM|DEP|EVD|REQ|BAR|DAR|WRK|ISS)-\d{3}) \|",
    re.MULTILINE,
)
PRINCIPLE_ID = re.compile(r"\bPRN-\d{3}\b")
PRINCIPLE_HEADING = re.compile(r"^## (PRN-\d{3}):", re.MULTILINE)
REGISTER_PIPE_COUNTS = {
    "DEC": 9,
    "OQ": 8,
    "RSK": 9,
    "ASM": 8,
    "DEP": 8,
    "EVD": 8,
    "REQ": 9,
    "BAR": 8,
    "DAR": 8,
    "WRK": 8,
    "ISS": 8,
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
