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


def test_finite_sample_annotations_do_not_cross_plot_axes() -> None:
    text = (FIGURES / "v36_v40_electromagnetic_finite_sample_validation.svg").read_text(
        encoding="utf-8"
    )

    assert 'x="430" y="610" text-anchor="end"' in text
    assert 'x="430" y="655" text-anchor="end"' in text
    assert 'x="1160" y="610" text-anchor="end"' in text
    assert 'x="1160" y="655" text-anchor="end"' in text
    assert 'x="390" y="610"' not in text
    assert 'x="1105" y="610"' not in text


def test_transportability_panel_copy_is_wrapped_inside_cards() -> None:
    text = (FIGURES / "v51_v55_transportability_validation.svg").read_text(
        encoding="utf-8"
    )

    assert "An invertible sensor-coordinate change preserves the Gaussian likelihood" in text
    assert "when the data and complete model are transformed consistently." in text
    assert "Concentrated weights reduce effective information and expose unstable transport." in text
    assert "Cauchy-Schwarz bound =" in text

    assert (
        "An invertible change of sensor coordinates preserves the full Gaussian likelihood "
        "information when the complete model is transformed consistently."
    ) not in text
    assert (
        "Exact reweighting can recover a target expectation under covariate shift, but "
        "concentrated weights reduce effective information and expose unstable transport."
    ) not in text
