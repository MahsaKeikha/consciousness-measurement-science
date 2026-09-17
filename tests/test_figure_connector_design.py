from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG_NS = "{http://www.w3.org/2000/svg}"
FIGURES = (
    ROOT / "docs" / "figures" / "measurement_architecture.svg",
    ROOT / "docs" / "figures" / "structural_measurement_pipeline.svg",
)


def test_reader_facing_arrowheads_use_absolute_restrained_geometry() -> None:
    for figure in FIGURES:
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
    for figure in FIGURES:
        text = figure.read_text(encoding="utf-8")
        assert 'markerUnits="strokeWidth"' not in text
        assert 'markerUnits="userSpaceOnUse"' in text
        assert "marker-end" in text
