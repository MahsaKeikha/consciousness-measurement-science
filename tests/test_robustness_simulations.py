from math import isclose

from consciousness_measurement.robustness_simulations import (
    calibration_sample_coverage_experiment,
    canonical_two_site_counterexample,
    conditioning_experiment,
    missingness_stress_experiment,
    resolution_abstention_frontier,
    two_site_nonidentifiability_experiment,
)


def test_calibration_sample_experiment_improves_with_more_calibration_data() -> None:
    rows = calibration_sample_coverage_experiment(
        prevalence=0.40,
        sensitivity=0.84,
        specificity=0.91,
        deployment_n=800,
        calibration_sizes=(100, 500, 2000),
        repetitions=300,
        delta=0.05,
        seed=20260918,
    )
    assert rows[-1]["identified_rate"] >= rows[0]["identified_rate"]
    assert rows[-1]["mean_width"] < rows[0]["mean_width"]
    assert rows[-1]["conditional_coverage"] >= 0.94


def test_missingness_width_grows_with_missing_fraction() -> None:
    rows = missingness_stress_experiment(
        prevalence=0.40,
        sensitivity=0.84,
        specificity=0.91,
        total_trials=1000,
        missing_fractions=(0.0, 0.1, 0.2, 0.3),
    )
    widths = [row["width"] for row in rows]
    assert widths == sorted(widths)
    assert widths[-1] > widths[0]


def test_conditioning_amplification_diverges_as_youden_shrinks() -> None:
    rows = conditioning_experiment(
        youden_values=(0.05, 0.1, 0.2, 0.5, 0.8),
        proxy_rate_error=0.02,
    )
    assert rows[0]["amplification"] > rows[-1]["amplification"]
    assert isclose(rows[0]["latent_error_from_proxy_error"], 0.4, abs_tol=1e-12)


def test_two_site_identified_width_is_positive_for_mixed_calibration() -> None:
    rows = two_site_nonidentifiability_experiment(
        pooled_proxy_rates=(0.35, 0.45, 0.55),
        site1_weight=0.5,
        site1_sensitivity=0.9,
        site1_specificity=0.9,
        site2_sensitivity=0.7,
        site2_specificity=0.8,
    )
    assert rows
    assert any(row["identified_width"] > 0.0 for row in rows)


def test_abstention_frontier_claim_rate_increases_with_deployment_sample() -> None:
    rows = resolution_abstention_frontier(
        prevalence=0.40,
        sensitivity=0.84,
        specificity=0.91,
        deployment_sizes=(100, 500, 2000),
        calibration_n_per_class=1500,
        repetitions=250,
        delta=0.05,
        maximum_width=0.30,
        seed=20260918,
    )
    assert rows[-1]["resolution_claim_rate"] >= rows[0]["resolution_claim_rate"]


def test_canonical_counterexample_is_numerically_exact() -> None:
    record = canonical_two_site_counterexample()
    assert abs(record["pooled_proxy_rate_a"] - record["pooled_proxy_rate_b"]) < 1e-12
    assert record["average_prevalence_gap"] == 0.1875
