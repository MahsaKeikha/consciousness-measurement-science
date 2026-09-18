from __future__ import annotations

import numpy as np
import pytest

from consciousness_measurement.electromagnetic_design_simulations import (
    v31_point_spread_cross_talk,
    v32_noise_aware_source_distinguishability,
    v33_sensor_design_information,
    v34_nuisance_subspace_information_loss,
    v35_robust_information_under_model_uncertainty,
)


def test_v31_distinguishes_point_spread_from_cross_talk() -> None:
    result = v31_point_spread_cross_talk()
    assert result["point_spread"] == pytest.approx([0.1, 0.7, 0.1, 0.0])
    assert result["cross_talk"] == pytest.approx([0.2, 0.7, 0.2, 0.0])
    assert result["cross_talk_leakage_norm"] > result["point_spread_leakage_norm"]


def test_v32_noise_aware_distance_separates_close_and_distinct_topographies() -> None:
    rows = v32_noise_aware_source_distinguishability()
    values = {row["comparison"]: row["mahalanobis_distance_squared"] for row in rows}
    assert values["close"] == pytest.approx(0.003229357798165141)
    assert values["distinct"] == pytest.approx(2.3394495412844036)
    assert values["distinct"] > 100.0 * values["close"]


def test_v33_complementary_sensor_design_improves_information_geometry() -> None:
    rows = {row["design"]: row for row in v33_sensor_design_information()}
    redundant = rows["redundant"]
    complementary = rows["complementary"]
    assert redundant["determinant"] == pytest.approx(0.0024)
    assert complementary["determinant"] == pytest.approx(2.0)
    assert redundant["minimum_eigenvalue"] == pytest.approx(0.0008)
    assert complementary["minimum_eigenvalue"] == pytest.approx(1.0)


def test_v34_information_fraction_is_sine_squared_principal_angle() -> None:
    rows = v34_nuisance_subspace_information_loss()
    for row in rows:
        assert row["retained_information_fraction"] == pytest.approx(
            row["sin_squared_angle"],
            abs=1e-14,
        )
    assert rows[0]["retained_information_fraction"] == pytest.approx(0.0)
    assert rows[-1]["retained_information_fraction"] == pytest.approx(1.0)


def test_v35_robust_bound_is_attained_and_monotone() -> None:
    rows = v35_robust_information_under_model_uncertainty()
    bounds = [row["robust_information_lower_bound"] for row in rows]
    assert bounds == sorted(bounds, reverse=True)
    for row in rows:
        assert row["realized_worst_case_information"] == pytest.approx(
            row["robust_information_lower_bound"],
            abs=1e-14,
        )
    assert rows[-1]["robust_information_lower_bound"] == pytest.approx(0.0)
    assert np.isfinite(bounds).all()
