from __future__ import annotations

import pytest

from consciousness_measurement.electromagnetic_finite_sample_simulations import (
    v36_gls_amplitude_efficiency,
    v37_inverse_covariance_bias,
    v38_gaussian_source_discrimination,
    v39_independent_search_fwer,
    v40_covariance_mismatch_sandwich,
)


def test_v36_gls_monte_carlo_matches_exact_variance_and_nominal_coverage() -> None:
    result = v36_gls_amplitude_efficiency()
    assert result["fisher_information"] == pytest.approx(1.2766666666666668)
    assert result["exact_variance"] == pytest.approx(0.7832898172323759)
    assert result["crlb_variance"] == pytest.approx(result["exact_variance"])
    assert result["empirical_mean"] == pytest.approx(1.2, abs=0.02)
    assert result["empirical_variance"] == pytest.approx(
        result["exact_variance"],
        rel=0.03,
    )
    assert result["empirical_coverage_95"] == pytest.approx(0.95, abs=0.01)


def test_v37_inverse_covariance_bias_decays_with_noise_sample_size() -> None:
    rows = v37_inverse_covariance_bias()
    factors = [row["inverse_covariance_bias_factor"] for row in rows]
    assert factors == pytest.approx([6.0, 2.0, 4.0 / 3.0, 10.0 / 9.0])
    assert factors == sorted(factors, reverse=True)


def test_v38_bayes_error_falls_monotonically_with_mahalanobis_separation() -> None:
    rows = v38_gaussian_source_discrimination()
    errors = [row["equal_prior_bayes_error"] for row in rows]
    assert errors == pytest.approx(
        [
            0.5,
            0.4012936743170763,
            0.3085375387259869,
            0.15865525393145707,
            0.06680720126885809,
        ]
    )
    assert errors == sorted(errors, reverse=True)


def test_v39_threshold_rises_with_search_multiplicity_and_controls_fwer() -> None:
    rows = v39_independent_search_fwer()
    thresholds = [row["two_sided_z_threshold"] for row in rows]
    assert thresholds == pytest.approx(
        [
            1.9599639845400536,
            2.7996252193010864,
            3.473978869154039,
            4.0496605495541695,
        ]
    )
    assert thresholds == sorted(thresholds)
    for row in rows:
        assert row["realized_fwer"] == pytest.approx(0.05, abs=1e-12)


def test_v40_oracle_variance_is_calibrated_and_mismatch_understates_uncertainty() -> None:
    rows = {row["weight_model"]: row for row in v40_covariance_mismatch_sandwich()}
    oracle = rows["oracle_precision"]
    identity = rows["identity_weight"]
    diagonal = rows["diagonal_precision"]

    assert oracle["variance_ratio_exact_over_nominal"] == pytest.approx(1.0)
    assert identity["variance_ratio_exact_over_nominal"] == pytest.approx(1.3312)
    assert diagonal["variance_ratio_exact_over_nominal"] == pytest.approx(
        1.3300589390962674
    )
    assert identity["exact_sandwich_variance"] > identity["nominal_precision_variance"]
    assert diagonal["exact_sandwich_variance"] > diagonal["nominal_precision_variance"]
