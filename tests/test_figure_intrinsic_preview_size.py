from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = ROOT / "docs" / "figures"
SVG_NS = "{http://www.w3.org/2000/svg}"
NUMBER = re.compile(r"^[0-9]+(?:\.[0-9]+)?$")


def test_canonical_svgs_declare_large_intrinsic_preview_dimensions() -> None:
    figures = sorted(FIGURE_DIR.glob("*.svg"))
    assert figures

    for figure in figures:
        root = ET.parse(figure).getroot()
        assert root.tag == f"{SVG_NS}svg"
        width = root.attrib.get("width")
        height = root.attrib.get("height")
        assert width and NUMBER.match(width), (
            f"{figure.name} must declare a numeric intrinsic width so GitHub does not "
            "fall back to a tiny default SVG preview"
        )
        assert height and NUMBER.match(height), (
            f"{figure.name} must declare a numeric intrinsic height so GitHub does not "
            "fall back to a tiny default SVG preview"
        )
        assert float(width) >= 1000
        assert float(height) >= 600


def test_intrinsic_preview_aspect_ratio_matches_viewbox() -> None:
    for figure in sorted(FIGURE_DIR.glob("*.svg")):
        root = ET.parse(figure).getroot()
        viewbox = [float(value) for value in root.attrib["viewBox"].split()]
        _, _, viewbox_width, viewbox_height = viewbox
        intrinsic_ratio = float(root.attrib["width"]) / float(root.attrib["height"])
        viewbox_ratio = viewbox_width / viewbox_height
        assert abs(intrinsic_ratio - viewbox_ratio) < 0.01, (
            f"{figure.name} intrinsic size must preserve the SVG viewBox aspect ratio"
        )
