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
RUNNER_V16_V20 = (ROOT / "scripts" / "run_electromagnetic_validation.py").read_text(
    encoding="utf-8"
)
RUNNER_V21_V25 = (
    ROOT / "scripts" / "run_electromagnetic_inverse_validation.py"
).read_text(encoding="utf-8")
RUNNER_V26_V30 = (
    ROOT / "scripts" / "run_electromagnetic_resolution_validation.py"
).read_text(encoding="utf-8")
RUNNER_V31_V35 = (ROOT / "scripts" / "run_electromagnetic_design_validation.py").read_text(
    encoding="utf-8"
)
RUNNER_V36_V40 = (
    ROOT / "scripts" / "run_electromagnetic_finite_sample_validation.py"
).read_text(encoding="utf-8")
RUNNER_V41_V45 = (
    ROOT / "scripts" / "run_electromagnetic_selection_validation.py"
).read_text(encoding="utf-8")
RUNNER_V46_V50 = (
    ROOT / "scripts" / "run_electromagnetic_replication_validation.py"
).read_text(encoding="utf-8")

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
    "v16_v20_electromagnetic_validation.svg",
    "v21_v25_electromagnetic_inverse_validation.svg",
    "v26_v30_electromagnetic_resolution_validation.svg",
    "v31_v35_electromagnetic_design_validation.svg",
    "v36_v40_electromagnetic_finite_sample_validation.svg",
    "v41_v45_electromagnetic_selection_validation.svg",
    "v46_v50_electromagnetic_replication_validation.svg",
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
    "v17_em_scale_invariance.csv",
    "v19_common_mode_confound.csv",
    "v20_frequency_specific_structure.csv",
    "electromagnetic_validation_summary.json",
    "v21_reference_invariance.csv",
    "electromagnetic_inverse_validation_summary.json",
    "v23_regularization_path.csv",
    "v24_multimodal_nullity.csv",
    "v25_forward_model_perturbation.csv",
    "v26_correlated_noise_whitening.csv",
    "v27_resolution_leakage.csv",
    "v28_fisher_information.csv",
    "v29_temporal_aliasing.csv",
    "v30_inverse_noise_amplification.csv",
    "electromagnetic_resolution_validation_summary.json",
    "v31_point_spread_cross_talk.csv",
    "v32_source_distinguishability.csv",
    "v33_sensor_design_information.csv",
    "v34_nuisance_information_loss.csv",
    "v35_robust_model_information.csv",
    "electromagnetic_design_validation_summary.json",
    "v36_gls_amplitude_efficiency.csv",
    "v37_inverse_covariance_bias.csv",
    "v38_gaussian_source_discrimination.csv",
    "v39_independent_search_fwer.csv",
    "v40_covariance_mismatch_sandwich.csv",
    "electromagnetic_finite_sample_validation_summary.json",
    "v41_bonferroni_arbitrary_dependence.csv",
    "v42_holm_step_down.csv",
    "v43_sign_flip_max_statistic.csv",
    "v44_post_selection_coverage.csv",
    "v45_independent_holdout.csv",
    "electromagnetic_selection_validation_summary.json",
    "v46_common_effect_pooling.csv",
    "v47_common_effect_heterogeneity.csv",
    "v48_leave_one_site_out.csv",
    "v49_partial_conjunction_replicability.csv",
    "v50_site_weight_concentration.csv",
    "electromagnetic_replication_validation_summary.json",
)


def test_validation_entry_point_covers_all_fifty_stages() -> None:
    assert "Research III Formal Validation V1-V50" in VALIDATION
    assert "docs/validation-atlas.md" in VALIDATION
    for stage in range(1, 51):
        assert f"**V{stage}**" in VALIDATION


def test_validation_atlas_exposes_every_result_figure() -> None:
    assert "twenty-one validation-result figures" in ATLAS
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
    assert "run_electromagnetic_validation.py" in VALIDATION
    assert "run_electromagnetic_inverse_validation.py" in VALIDATION
    assert "run_electromagnetic_resolution_validation.py" in VALIDATION
    assert "run_electromagnetic_design_validation.py" in VALIDATION
    assert "run_electromagnetic_finite_sample_validation.py" in VALIDATION
    assert "run_electromagnetic_selection_validation.py" in VALIDATION
    assert "run_electromagnetic_replication_validation.py" in VALIDATION
    assert "20260917" in RESULTS_INDEX
    assert "20260918" in RESULTS_INDEX
    assert "20260919" in RESULTS_INDEX
    assert "deterministic" in RESULTS_INDEX.lower()


def test_result_figures_are_regenerated_by_the_declared_runners() -> None:
    for figure in RESULT_FIGURES[:5]:
        assert figure in RUNNER_V1_V5
    for figure in RESULT_FIGURES[5:10]:
        assert figure in RUNNER_V6_V10
    for figure in RESULT_FIGURES[10:14]:
        assert figure in RUNNER_V11_V15
    assert RESULT_FIGURES[14] in RUNNER_V16_V20
    assert RESULT_FIGURES[15] in RUNNER_V21_V25
    assert RESULT_FIGURES[16] in RUNNER_V26_V30
    assert RESULT_FIGURES[17] in RUNNER_V31_V35
    assert RESULT_FIGURES[18] in RUNNER_V36_V40
    assert RESULT_FIGURES[19] in RUNNER_V41_V45
    assert RESULT_FIGURES[20] in RUNNER_V46_V50


def test_reader_surfaces_preserve_empirical_boundary() -> None:
    required = (
        "not human empirical data",
        "not human empirical evidence",
    )
    combined = f"{VALIDATION}\n{ATLAS}\n{RESULTS_INDEX}".lower()
    assert all(phrase in combined for phrase in required)
