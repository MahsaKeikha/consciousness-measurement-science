from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATION = (ROOT / "VALIDATION.md").read_text(encoding="utf-8")
ATLAS = (ROOT / "docs" / "validation-atlas.md").read_text(encoding="utf-8")
RESULTS_INDEX = (ROOT / "results" / "README.md").read_text(encoding="utf-8")
RUNNER_V1_V5 = (ROOT / "scripts" / "run_validation_program.py").read_text(encoding="utf-8")
RUNNER_V6_V10 = (ROOT / "scripts" / "run_robustness_validation.py").read_text(
    encoding="utf-8"
)
RUNNER_V11_V15 = (ROOT / "scripts" / "run_identification_design_validation.py").read_text(
    encoding="utf-8"
)

RESULT_FIGURES = (
    "finite_sample_identification.svg",
    "finite_sample_coverage.svg",
    "transport_bias_surface.svg",
    "dependence_stress.svg",
    "structural_alignment_power.svg",
    "calibration_sample_uncertainty.svg",
    "missingness_identification_loss.svg",
    "inverse_conditioning_youden.svg",
    "two_site_partial_identification.svg",
    "resolution_abstention_frontier.svg",
    "v11_missingness_information_law.svg",
    "v12_v13_multisite_heterogeneity.svg",
    "v14_resolution_sample_size.svg",
    "v15_independent_pilot_gate.svg",
)

RESULT_FILES = (
    "finite_sample_coverage.csv",
    "dependence_stress.csv",
    "transport_stress.csv",
    "structural_alignment_power.csv",
    "validation_summary.json",
    "calibration_sample_uncertainty.csv",
    "missingness_stress.csv",
    "conditioning_stress.csv",
    "two_site_nonidentifiability.csv",
    "resolution_abstention_frontier.csv",
    "robustness_validation_summary.json",
    "v11_missingness_information_law.csv",
    "v12_v13_multisite_identification.csv",
    "v14_resolution_sample_size.csv",
    "v15_independent_pilot_gate.csv",
    "identification_design_summary.json",
)


def test_validation_entry_point_covers_all_fifteen_stages() -> None:
    assert "Research III Formal Validation V1-V15" in VALIDATION
    assert "docs/validation-atlas.md" in VALIDATION
    for stage in range(1, 16):
        assert f"**V{stage}**" in VALIDATION


def test_validation_atlas_exposes_every_result_figure() -> None:
    assert "fourteen validation-result figures" in ATLAS
    for figure in RESULT_FIGURES:
        assert (ROOT / "docs" / "figures" / figure).is_file()
        assert f"figures/{figure}" in ATLAS


def test_machine_readable_record_is_complete_and_linked() -> None:
    for result in RESULT_FILES:
        assert (ROOT / "results" / result).is_file()
        assert result in RESULTS_INDEX
        assert result in ATLAS or "summary.json" in result


def test_all_validation_runners_are_reader_visible() -> None:
    assert "run_validation_program.py" in VALIDATION
    assert "run_robustness_validation.py" in VALIDATION
    assert "run_identification_design_validation.py" in VALIDATION
    assert "20260917" in RESULTS_INDEX
    assert "20260918" in RESULTS_INDEX
    assert "20260919" in RESULTS_INDEX


def test_result_figures_are_regenerated_by_the_declared_runners() -> None:
    for figure in RESULT_FIGURES[:5]:
        assert figure in RUNNER_V1_V5
    for figure in RESULT_FIGURES[5:10]:
        assert figure in RUNNER_V6_V10
    for figure in RESULT_FIGURES[10:]:
        assert figure in RUNNER_V11_V15


def test_reader_surfaces_preserve_empirical_boundary() -> None:
    required = (
        "not human empirical data",
        "not human empirical evidence",
    )
    combined = f"{VALIDATION}\n{ATLAS}\n{RESULTS_INDEX}".lower()
    assert all(phrase in combined for phrase in required)
