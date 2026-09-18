from __future__ import annotations

import pytest

from consciousness_measurement.electromagnetic_inverse_simulations import (
    v21_reference_invariance_grid,
    v22_lead_field_nonidentifiability,
    v23_regularization_path,
    v24_multimodal_nullity,
    v25_forward_model_perturbation_grid,
)


def test_v21_common_rereferencing_preserves_pairwise_sensor_differences() -> None:
    rows = v21_reference_invariance_grid()
    assert len(rows) == 5
    assert max(row["max_pairwise_difference_error"] for row in rows) < 2e-14


def test_v22_lead_field_has_exact_nonidentifiable_source_alternative() -> None:
    result = v22_lead_field_nonidentifiability()
    assert result["rank"] == pytest.approx(3.0)
    assert result["nullity"] == pytest.approx(3.0)
    assert result["sensor_residual"] < 1e-14
    assert result["source_separation"] == pytest.approx(1.0)


def test_v23_regularization_changes_resolution_tradeoff() -> None:
    rows = v23_regularization_path()
    estimate_norms = [row["estimate_norm"] for row in rows]
    residuals = [row["measurement_residual"] for row in rows]
    assert estimate_norms == sorted(estimate_norms, reverse=True)
    assert residuals == sorted(residuals)
    assert residuals[-1] > 1000.0 * residuals[0]


def test_v24_combined_modalities_reduce_nullity_without_guaranteeing_uniqueness() -> None:
    rows = v24_multimodal_nullity()
    by_code = {int(row["modality_code"]): row for row in rows}
    assert by_code[1]["nullity"] == pytest.approx(3.0)
    assert by_code[2]["nullity"] == pytest.approx(3.0)
    assert by_code[3]["nullity"] == pytest.approx(1.0)


def test_v25_forward_model_error_respects_declared_bound() -> None:
    rows = v25_forward_model_perturbation_grid()
    for row in rows:
        assert row["sensor_mismatch"] <= row["upper_bound"] + 1e-15
        assert 0.0 <= row["bound_ratio"] <= 1.0 + 1e-12
    assert rows[-1]["sensor_mismatch"] > rows[1]["sensor_mismatch"]
