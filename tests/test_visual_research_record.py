from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
GUIDE = (ROOT / "docs" / "visual-research-guide.md").read_text(encoding="utf-8")
CATALOG = (ROOT / "docs" / "figure-catalog.md").read_text(encoding="utf-8")
DOCS_MAP = (ROOT / "docs" / "README.md").read_text(encoding="utf-8")

FIGURES = (
    "research_program_map.svg",
    "target_evidence_matrix.svg",
    "measurement_architecture.svg",
    "cep_anatomy.svg",
    "identification_uncertainty_pipeline.svg",
    "structural_measurement_pipeline.svg",
    "validation_program_map.svg",
    "theory_falsification_map.svg",
    "claim_ladder.svg",
)


def test_nine_canonical_visuals_exist_and_parse() -> None:
    figure_dir = ROOT / "docs" / "figures"
    for name in FIGURES:
        path = figure_dir / name
        assert path.exists(), name
        root = ET.parse(path).getroot()
        assert root.tag.endswith("svg")


def test_readme_exposes_complete_visual_record() -> None:
    assert "nine canonical scientific visuals" in README
    for name in FIGURES:
        assert f"docs/figures/{name}" in README


def test_visual_guide_and_catalog_stay_synchronized() -> None:
    for name in FIGURES:
        assert f"figures/{name}" in GUIDE
        assert f"figures/{name}" in CATALOG
    assert "prospective human validation" in GUIDE
    assert "direct third-person measurement of qualia" in GUIDE


def test_documentation_map_promotes_visual_audit_path() -> None:
    assert "[Visual Research Guide](visual-research-guide.md)" in DOCS_MAP
    assert "[Figure Catalog](figure-catalog.md)" in DOCS_MAP
    assert "[Evidence-to-Claim Audit](evidence-to-claim-audit.md)" in DOCS_MAP
