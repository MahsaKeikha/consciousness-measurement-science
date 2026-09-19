from __future__ import annotations

import pytest

from consciousness_measurement.transportability_simulations import (
    v51_invertible_sensor_coordinate_invariance,
    v52_projection_information_monotonicity,
    v53_cross_hardware_topography_mismatch,
    v54_importance_weighted_transport,
    v55_total_variation_transport_budget,
)


def test_v51_canonical_invariance_record() -> None:
    result = v51_invertible_sensor_coordinate_invariance()
    assert result["transform_determinant"] == pytest.approx(1.1)
    assert result["original_information"] == pytest.approx(0.6156957928802589)
    assert result["transformed_information"] == pytest.approx(
        result["original_information"]
    )
    assert result["original_gls_estimate"] == pytest.approx(0.7624178712220763)
    assert result["transformed_gls_estimate"] == pytest.approx(
        result["original_gls_estimate"]
    )


def test_v52_canonical_projection_information_fractions() -> None:
    rows = {row["projection"]: row for row in v52_projection_information_monotonicity()}
    assert rows["all_sensors"]["information_fraction"] == pytest.approx(1.0)
    assert rows["drop_sensor_3"]["information_fraction"] == pytest.approx(
        0.8243937402938717
    )
    assert rows["single_mixed_channel"]["information_fraction"] == pytest.approx(
        0.6773170799899347
    )


def test_v53_mismatch_bias_remains_inside_exact_cauchy_schwarz_bound() -> None:
    rows = v53_cross_hardware_topography_mismatch()
    assert rows[-1]["expected_amplitude_gain"] == pytest.approx(0.8582286207569035)
    assert rows[-1]["absolute_relative_bias"] == pytest.approx(0.14177137924309646)
    assert rows[-1]["cauchy_schwarz_bias_bound"] == pytest.approx(0.5097730808460976)
    assert all(
        row["absolute_relative_bias"] <= row["cauchy_schwarz_bias_bound"] + 1e-12
        for row in rows
    )


def test_v54_transport_identity_and_effective_fraction() -> None:
    rows = v54_importance_weighted_transport()
    assert all(row["absolute_transport_identity_error"] <= 1e-12 for row in rows)
    assert rows[3]["target_expectation"] == pytest.approx(0.62)
    assert rows[3]["maximum_importance_weight"] == pytest.approx(2.5)
    assert rows[3]["effective_sample_fraction"] == pytest.approx(
        0.6134969325153374
    )


def test_v55_total_variation_budget_is_attained_in_canonical_shift() -> None:
    rows = v55_total_variation_transport_budget()
    assert rows[3]["total_variation"] == pytest.approx(0.3)
    assert rows[3]["actual_expectation_shift"] == pytest.approx(0.3)
    assert rows[3]["sharp_tv_bound"] == pytest.approx(0.3)
    assert abs(rows[3]["bound_slack"]) <= 1e-12
