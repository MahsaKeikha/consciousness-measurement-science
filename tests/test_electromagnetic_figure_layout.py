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

    assert 'x="395" y="610" text-anchor="end"' in text
    assert 'x="395" y="655" text-anchor="end"' in text
    assert 'x="1125" y="610" text-anchor="end"' in text
    assert 'x="1125" y="655" text-anchor="end"' in text
    assert 'x1="480" y1="570" x2="480"' in text
    assert 'x1="1220" y1="570" x2="1220"' in text
    assert 'x="430" y="610"' not in text
    assert 'x="1160" y="610"' not in text


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


def test_late_stage_panel_copy_is_wrapped_inside_cards() -> None:
    design = (FIGURES / "v31_v35_electromagnetic_design_validation.svg").read_text(
        encoding="utf-8"
    )
    selection = (FIGURES / "v41_v45_electromagnetic_selection_validation.svg").read_text(
        encoding="utf-8"
    )
    replication = (FIGURES / "v46_v50_electromagnetic_replication_validation.svg").read_text(
        encoding="utf-8"
    )

    assert "retained information equals" in design
    assert "sin squared of their angle." in design
    assert "topography error grows." in design
    assert (
        "For one target and one nuisance direction, retained information equals sin squared of their angle."
    ) not in design

    assert "then reuse its ordinary" in selection
    assert "marginal interval." in selection
    assert (
        "Select the largest absolute null statistic, then reuse its ordinary marginal interval."
    ) not in selection

    assert "requiring at least r" in replication
    assert "nonnull sites." in replication
    assert "not evidence from" in replication
    assert "real sites." in replication
    assert (
        "Bonferroni partial-conjunction p-values for requiring at least r nonnull sites."
    ) not in replication


def test_inverse_and_resolution_footer_copy_stays_below_axis_labels() -> None:
    inverse = (FIGURES / "v21_v25_electromagnetic_inverse_validation.svg").read_text(
        encoding="utf-8"
    )
    resolution = (FIGURES / "v26_v30_electromagnetic_resolution_validation.svg").read_text(
        encoding="utf-8"
    )

    assert 'y="744"' in inverse
    assert 'x="86" y="779"' in inverse
    assert 'y1="779"' in inverse
    assert 'y="784"' in inverse
    assert 'y="752"' not in inverse

    assert 'y="744"' in resolution
    assert 'x="86" y="779"' in resolution
    assert 'x="756" y="779"' in resolution
    assert 'y="752"' not in resolution


def test_research_iii_validation_figures_expose_scientific_guidance() -> None:
    guided = {
        "v16_v20_electromagnetic_validation.svg": (
            "SCIENTIFIC QUESTION",
            "phase concentration",
            "Finding: nuisance removal",
        ),
        "v21_v25_electromagnetic_inverse_validation.svg": (
            "SCIENTIFIC QUESTION",
            "sensor mismatch / analytical bound",
            "pass condition: observed mismatch remains below bound",
        ),
        "v26_v30_electromagnetic_resolution_validation.svg": (
            "SCIENTIFIC QUESTION",
            "Fisher information",
            "dashed line = irreducible rank floor",
        ),
        "v31_v35_electromagnetic_design_validation.svg": (
            "SCIENTIFIC QUESTION",
            "rho_ret = sin^2(theta)",
            "I_rob(eps) = [max(||w|| - eps, 0)]^2",
        ),
        "v36_v40_electromagnetic_finite_sample_validation.svg": (
            "SCIENTIFIC QUESTION",
            "P(error) = Phi(-d/2)",
            "FWER = 1 - [2 Phi(t) - 1]^K",
        ),
        "v41_v45_electromagnetic_selection_validation.svg": (
            "SCIENTIFIC QUESTION",
            "t(alpha,K) = Phi^-1(1 - alpha/(2K))",
            "C_selected = c^K",
        ),
        "v46_v50_electromagnetic_replication_validation.svg": (
            "SCIENTIFIC QUESTION",
            "delta_i = mu_hat(-i) - mu_hat",
            "larger r = stronger replication requirement",
        ),
        "v51_v55_transportability_validation.svg": (
            "SCIENTIFIC QUESTION",
            "Information monotonicity: I(PY) &lt;= I(Y)",
            "Pass: |relative bias| &lt;= covariance-weighted bound",
        ),
    }

    for name, markers in guided.items():
        text = (FIGURES / name).read_text(encoding="utf-8")
        for marker in markers:
            assert marker in text, f"{name} is missing publication guidance: {marker}"


def test_research_iii_evidence_architecture_exposes_failure_gates_and_claim_ceiling() -> None:
    path = FIGURES / "research_iii_evidence_architecture.svg"
    root = ET.parse(path).getroot()
    text = path.read_text(encoding="utf-8")

    assert root.attrib["width"] == "1600"
    assert root.attrib["height"] == "1000"
    assert root.attrib["viewBox"] == "0 0 1600 1000"
    assert text.count("FAILURE GATE") == 8
    assert "CLAIM CEILING" in text
    assert "No direct consciousness claim yet" in text
    assert "HOW TO READ THE RESULT FIGURES" in text
    assert 'markerUnits="userSpaceOnUse"' in text


def test_publication_question_panels_use_contained_line_lengths() -> None:
    figures = [
        "v16_v20_electromagnetic_validation.svg",
        "v21_v25_electromagnetic_inverse_validation.svg",
        "v26_v30_electromagnetic_resolution_validation.svg",
        "v31_v35_electromagnetic_design_validation.svg",
        "v36_v40_electromagnetic_finite_sample_validation.svg",
        "v41_v45_electromagnetic_selection_validation.svg",
        "v46_v50_electromagnetic_replication_validation.svg",
        "v51_v55_transportability_validation.svg",
    ]

    for name in figures:
        text = (FIGURES / name).read_text(encoding="utf-8")
        assert "SCIENTIFIC QUESTION" in text
        question_lines = [
            line.split(">", 1)[1].split("</text>", 1)[0]
            for line in text.splitlines()
            if "<text" in line
            and (
                'x="950"' in line
                or 'x="1110"' in line
                or 'x="250"' in line
            )
            and 'font-weight="700"' in line
            and "SCIENTIFIC QUESTION" not in line
        ]
        assert question_lines, f"{name} is missing contained question copy"
        assert max(len(line) for line in question_lines) <= 46, (
            f"{name} has question text too long for its panel: {question_lines}"
        )


def test_evidence_architecture_stage_cards_keep_text_inside_narrow_columns() -> None:
    path = FIGURES / "research_iii_evidence_architecture.svg"
    root = ET.parse(path).getroot()
    stage_x = {"105", "287", "469", "651", "833", "1015", "1197", "1379"}

    stage_lines: list[str] = []
    for node in root.iter():
        if not node.tag.endswith("text"):
            continue
        if node.attrib.get("x") not in stage_x:
            continue
        y = float(node.attrib.get("y", "0"))
        if 250 <= y <= 470:
            stage_lines.append("".join(node.itertext()).strip())

    assert len(stage_lines) >= 64
    assert max(len(line) for line in stage_lines) <= 24, stage_lines
    assert "Field organization" not in stage_lines
    assert "Resolution limits" not in stage_lines
    assert "Selection safety" not in stage_lines
