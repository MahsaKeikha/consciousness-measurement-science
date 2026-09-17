from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG_NS = "{http://www.w3.org/2000/svg}"
FIGURE_DIR = ROOT / "docs" / "figures"


def _connector_figures() -> list[Path]:
    figures: list[Path] = []
    for figure in sorted(FIGURE_DIR.glob("*.svg")):
        text = figure.read_text(encoding="utf-8")
        if "marker-end" in text:
            figures.append(figure)
    return figures


def test_reader_facing_arrowheads_use_absolute_restrained_geometry() -> None:
    figures = _connector_figures()
    assert figures, "reader-facing connector figures must exist"

    for figure in figures:
        root = ET.parse(figure).getroot()
        markers = list(root.iter(f"{SVG_NS}marker"))
        assert markers, f"{figure.name} must declare its connector marker"

        for marker in markers:
            assert marker.attrib.get("markerUnits") == "userSpaceOnUse", (
                f"{figure.name} marker {marker.attrib.get('id')} must not scale "
                "with connector stroke width"
            )
            assert float(marker.attrib["markerWidth"]) <= 10.0
            assert float(marker.attrib["markerHeight"]) <= 10.0


def test_reader_facing_connectors_do_not_restore_stroke_scaled_markers() -> None:
    for figure in _connector_figures():
        text = figure.read_text(encoding="utf-8")
        assert 'markerUnits="strokeWidth"' not in text
        assert 'markerUnits="userSpaceOnUse"' in text
        assert "marker-end" in text
