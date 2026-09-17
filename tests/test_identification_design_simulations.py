from __future__ import annotations

import pytest

from consciousness_measurement.identification_design_simulations import (
    independent_pilot_gate_experiment,
    missingness_information_design_grid,
    multisite_heterogeneity_design_grid,
    point_calibration_coverage_experiment,
    resolution_sample_size_design_grid,
)


def test_v11_design_grid_obeys_exact_missingness_over_information_law() -> None:
    rows = missingness_information_design_grid(
        missing_fractions=(0.05, 0.10, 0.20),
        youden_values=(0.4, 0.6, 0.8),
    )
    for row in rows:
        assert row["interior_latent_width"] == pytest.approx(
            row["missing_fraction"] / row["youden"]
        )


def test_v12_v13_multisite_width_is_zero_only_at_equal_information_margins() -> None:
    rows = multisite_heterogeneity_design_grid(
        spreads=(0.0, 0.05, 0.10, 0.20, 0.30),
    )
    assert rows[0]["identified_width"] == pytest.approx(0.0, abs=1e-12)
    assert all(row["identified_width"] > 0.0 for row in rows[1:])
    assert rows[-1]["identified_width"] > rows[1]["identified_width"]
    for row in rows:
        assert row["identified_lower"] <= row["true_average_prevalence"] <= row["identified_upper"]


def test_v14_design_grid_requires_more_data_for_weaker_channels_and_tighter_resolution() -> None:
    rows = resolution_sample_size_design_grid(
        youden_values=(0.3, 0.5, 0.8),
        maximum_widths=(0.20, 0.10),
        delta=0.05,
    )
    lookup = {(row["youden"], row["maximum_width"]): row["required_n"] for row in rows}
    assert lookup[(0.3, 0.10)] > lookup[(0.5, 0.10)] > lookup[(0.8, 0.10)]
    assert lookup[(0.5, 0.10)] > lookup[(0.5, 0.20)]


def test_v14_point_calibration_simulation_is_conservative_at_design_size() -> None:
    coverage = point_calibration_coverage_experiment(
        prevalence=0.40,
        sensitivity=0.84,
        specificity=0.91,
        deployment_n=1500,
        repetitions=1200,
        delta=0.05,
        seed=20260919,
    )
    assert coverage >= 0.95


def test_v15_independent_pilot_gate_has_nontrivial_release_and_conservative_coverage() -> None:
    result = independent_pilot_gate_experiment(
        prevalence=0.40,
        sensitivity=0.84,
        specificity=0.91,
        pilot_calibration_n_per_class=120,
        confirm_deployment_n=900,
        confirm_calibration_n_per_class=2500,
        maximum_width=0.12,
        repetitions=1600,
        delta=0.05,
        seed=20260919,
    )
    assert 0.15 < result["release_rate"] < 0.85
    assert result["confirm_identified_rate"] > 0.10
    assert result["conditional_coverage_given_release_and_identification"] >= 0.95
