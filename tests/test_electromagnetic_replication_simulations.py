from __future__ import annotations

import pytest

from consciousness_measurement.electromagnetic_replication_simulations import (
    v46_common_effect_pooling,
    v47_common_effect_heterogeneity,
    v48_leave_one_site_out_influence,
    v49_partial_conjunction_replicability,
    v50_site_weight_concentration,
)


def test_v46_canonical_common_effect_pooling() -> None:
    result = v46_common_effect_pooling()
    assert result["pooled_estimate"] == pytest.approx(0.426860025220681)
    assert result["pooled_standard_error"] == pytest.approx(0.06391987418055915)
    assert result["pooled_variance"] == pytest.approx(0.004085750315258513)
    assert result["site_count"] == pytest.approx(4.0)


def test_v47_q_simulation_matches_known_variance_common_effect_moments() -> None:
    result = v47_common_effect_heterogeneity()
    assert result["observed_q"] == pytest.approx(0.9200868712344125)
    assert result["degrees_of_freedom"] == pytest.approx(3.0)
    assert result["simulated_mean_q"] == pytest.approx(3.0115441661730187)
    assert result["theoretical_mean_q"] == pytest.approx(3.0)
    assert result["simulated_variance_q"] == pytest.approx(6.037871716780914)
    assert result["theoretical_variance_q"] == pytest.approx(6.0)


def test_v48_delete_one_influence_identity_matches_each_site() -> None:
    rows = v48_leave_one_site_out_influence()
    expected = [
        0.0027174395680514274,
        -0.017769116129771834,
        0.03928069972601422,
        -0.01179068777846215,
    ]
    for row, shift in zip(rows, expected, strict=True):
        assert row["leave_one_out_shift"] == pytest.approx(shift)
        assert row["identity_shift"] == pytest.approx(shift)


def test_v49_partial_conjunction_sequence() -> None:
    rows = v49_partial_conjunction_replicability()
    assert [row["partial_conjunction_p_value"] for row in rows] == pytest.approx(
        [0.005, 0.048, 0.12, 0.42, 0.45]
    )


def test_v50_site_weight_concentration_exposes_dominance() -> None:
    rows = {row["design"]: row for row in v50_site_weight_concentration()}
    assert rows["balanced"]["effective_site_count"] == pytest.approx(4.0)
    assert rows["balanced"]["maximum_normalized_weight"] == pytest.approx(0.25)
    assert rows["balanced"]["maximum_delete_variance_inflation"] == pytest.approx(4.0 / 3.0)

    assert rows["dominant_site"]["effective_site_count"] == pytest.approx(
        1.3938223938223941
    )
    assert rows["dominant_site"]["maximum_normalized_weight"] == pytest.approx(16.0 / 19.0)
    assert rows["dominant_site"]["maximum_delete_variance_inflation"] == pytest.approx(
        19.0 / 3.0
    )
