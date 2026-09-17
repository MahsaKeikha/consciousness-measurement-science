"""Repository-wide publication, documentation, and style policy checks."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".json",
    ".yml",
    ".yaml",
    ".toml",
    ".cff",
    ".svg",
    ".txt",
}
TEXT_NAMES = {"LICENSE", "Makefile"}
PROHIBITED_DASHES = {"\u2013": "en dash", "\u2014": "em dash"}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDER_TOKENS = ("TO" + "DO", "T" + "BD", "FIX" + "ME", "FILL" + "_ME")
REQUIRED_READER_FILES = {
    "CONTRIBUTING.md",
    "RESEARCH_QUESTIONS.md",
    "ROADMAP.md",
    "claims/README.md",
    "data/README.md",
    "docs/README.md",
    "docs/assumption-registry.md",
    "docs/claim-registry.md",
    "docs/clinical-translation.md",
    "docs/edge-cases.md",
    "docs/epistemic-boundaries.md",
    "docs/ethics.md",
    "docs/evidence-to-claim-audit.md",
    "docs/experimental-program.md",
    "docs/failure-modes.md",
    "docs/falsification-matrix.md",
    "docs/figure-catalog.md",
    "docs/glossary.md",
    "docs/literature.md",
    "docs/measurement-framework.md",
    "docs/measurement-instrument-spec.md",
    "docs/phenomenal-structure.md",
    "docs/preregistration-template.md",
    "docs/protocol-phase1.md",
    "docs/repository-policy.md",
    "docs/reproducibility.md",
    "docs/software-guide.md",
    "docs/start-here.md",
    "docs/statistical-validation.md",
    "docs/theory-landscape.md",
    "docs/visual-research-guide.md",
    "examples/README.md",
    "examples/cep_example.json",
    "examples/claim_example.json",
    "schemas/README.md",
    "schemas/cep.schema.json",
    "schemas/claim.schema.json",
}
REQUIRED_README_MARKERS = {
    "Consciousness Evidence Profile",
    "Measurement claim ladder",
    "Current implementation status",
    "Not yet established",
    "Negative evidence rule",
    "Machine-readable research objects",
    "Visual research record",
}
CANONICAL_FIGURES = (
    "docs/figures/research_program_map.svg",
    "docs/figures/target_evidence_matrix.svg",
    "docs/figures/measurement_architecture.svg",
    "docs/figures/cep_anatomy.svg",
    "docs/figures/identification_uncertainty_pipeline.svg",
    "docs/figures/structural_measurement_pipeline.svg",
    "docs/figures/validation_program_map.svg",
    "docs/figures/theory_falsification_map.svg",
    "docs/figures/claim_ladder.svg",
)


def tracked_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in TEXT_NAMES:
            files.append(path)
    return sorted(files)


def check_prohibited_dashes(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for char, label in PROHIBITED_DASHES.items():
            if char in text:
                line = text[: text.index(char)].count("\n") + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: prohibited {label}")
    return errors


def check_placeholders(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        relative = path.relative_to(ROOT)
        if relative == Path("scripts/verify_repository_policy.py"):
            continue
        text = path.read_text(encoding="utf-8")
        for token in PLACEHOLDER_TOKENS:
            if token in text:
                line = text[: text.index(token)].count("\n") + 1
                errors.append(f"{relative}:{line}: unresolved placeholder token {token}")
    return errors


def check_json() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.json")):
        if ".git" in path.parts:
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    return errors


def check_svg() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.svg")):
        if ".git" in path.parts:
            continue
        try:
            ET.parse(path)
        except (OSError, ET.ParseError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid SVG/XML: {exc}")
    return errors


def check_markdown_links() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            clean = target.strip().split("#", 1)[0]
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            destination = (path.parent / clean).resolve()
            try:
                destination.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not destination.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local link: {target}")
    return errors


def check_reader_contract() -> list[str]:
    errors: list[str] = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for relative in sorted(REQUIRED_READER_FILES):
        if not (ROOT / relative).exists():
            errors.append(f"missing required reader file: {relative}")
        if f"]({relative})" not in readme:
            errors.append(f"README does not link required reader file: {relative}")
    for marker in sorted(REQUIRED_README_MARKERS):
        if marker not in readme:
            errors.append(f"README missing required reader marker: {marker}")
    for figure in CANONICAL_FIGURES:
        if not (ROOT / figure).exists():
            errors.append(f"missing canonical figure: {figure}")
        if figure not in readme:
            errors.append(f"README does not expose required figure: {figure}")
    return errors


def main() -> int:
    files = tracked_text_files()
    checks = [
        *check_prohibited_dashes(files),
        *check_placeholders(files),
        *check_json(),
        *check_svg(),
        *check_markdown_links(),
        *check_reader_contract(),
    ]
    if checks:
        print("Repository policy check failed:")
        for error in checks:
            print(f"- {error}")
        return 1
    print("Repository policy check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
