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
    "governance/PROJECT_STATUS.md",
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
}
FORBIDDEN_PHRASES = (
    "BIAN Adoption & " + "Transformation Platform",
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
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


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_agents_size(errors)
    check_required_content(errors)

    files = active_text_files()
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
