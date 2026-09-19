from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "docs" / "figures"

TARGETS = {
    "v16_v20_electromagnetic_validation.svg": (1400.0, 850.0),
    "v21_v25_electromagnetic_inverse_validation.svg": (1400.0, 900.0),
    "v26_v30_electromagnetic_resolution_validation.svg": (1400.0, 900.0),
}


def test_electromagnetic_validation_figures_use_publication_layout() -> None:
    for name, expected_size in TARGETS.items():
        path = FIGURES / name
        root = ET.parse(path).getroot()

        assert float(root.attrib["width"]) == expected_size[0]
        assert float(root.attrib["height"]) == expected_size[1]
        assert root.attrib["viewBox"] == f"0 0 {int(expected_size[0])} {int(expected_size[1])}"

        text = path.read_text(encoding="utf-8")
        assert 'transform="rotate' not in text
        assert 'font-size="31"' in text
        assert 'rx="12"' in text
        assert "<polyline " in text
        assert "<circle " in text


def test_electromagnetic_validation_figures_keep_explanation_out_of_plot_area() -> None:
    for name in TARGETS:
        root = ET.parse(FIGURES / name).getroot()
        labels = [
            (node.text or "").strip()
            for node in root.iter()
            if node.tag.endswith("text") and (node.text or "").strip()
        ]

        assert labels
        assert max(len(label) for label in labels) <= 145
        assert not any("therefore enters the sensor prediction" in label for label in labels)
        assert not any("Sensor-level synchrony therefore requires" in label for label in labels)
