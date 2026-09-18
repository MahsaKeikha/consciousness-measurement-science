from __future__ import annotations

import pytest

from consciousness_measurement.electromagnetic_resolution_simulations import (
    v26_correlated_noise_whitening,
    v27_resolution_leakage_path,
    v28_correlated_noise_fisher_information,
    v29_temporal_aliasing,
    v30_inverse_noise_amplification,
)


def test_v26_whitening_preserves_weighted_residual_geometry() -> None:
    result = v26_correlated_noise_whitening()
    assert result["weighted_residual_energy"] == pytest.approx(
        result["whitened_residual_energy"],
        abs=1e-14,
    )
    assert result["absolute_identity_error"] < 1e-14


def test_v27_inverse_resolution_retains_leakage_and_identity_error() -> None:
    rows = v27_resolution_leakage_path()
    assert len(rows) == 4
    for row in rows:
        assert 0.0 < row["off_diagonal_leakage_fraction"] < 1.0
        assert row["identity_error"] > 0.7
        assert row["resolution_trace"] < 3.0
    assert rows[-1]["identity_error"] > rows[0]["identity_error"]


def test_v28_common_sensor_noise_reduces_information_for_common_topography() -> None:
    rows = v28_correlated_noise_fisher_information()
    information = [row["fisher_information"] for row in rows]
    bounds = [row["crlb_variance"] for row in rows]
    assert information == sorted(information, reverse=True)
    assert bounds == sorted(bounds)
    assert rows[0]["fisher_information"] == pytest.approx(4.0)
    assert rows[-1]["crlb_variance"] == pytest.approx(0.925)


def test_v29_two_distinct_continuous_frequencies_alias_to_same_samples() -> None:
    result = v29_temporal_aliasing()
    assert result["frequency_hz"] != result["alias_frequency_hz"]
    assert result["alias_frequency_hz"] > result["sample_rate_hz"] / 2.0
    assert result["max_sample_difference"] < 2e-13


def test_v30_weak_singular_direction_amplifies_sensor_noise_exactly() -> None:
    rows = v30_inverse_noise_amplification()
    for row in rows:
        expected = 1.0 / row["smallest_singular_value"]
        assert row["pseudoinverse_norm"] == pytest.approx(expected)
        assert row["realized_noise_amplification"] == pytest.approx(expected)
    assert rows[-1]["realized_noise_amplification"] == pytest.approx(100.0)
