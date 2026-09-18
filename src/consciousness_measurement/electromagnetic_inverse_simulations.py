"""Deterministic forward/inverse EM experiments for Research III V21-V25."""

from __future__ import annotations

import numpy as np

from .electromagnetic_inverse import (
    common_reference_invariance_error,
    forward_model_mismatch,
    forward_model_perturbation_bound,
    rank_nullity,
    stacked_rank_nullity,
    tikhonov_source_estimate,
)


def v21_reference_invariance_grid() -> list[dict[str, float]]:
    """V21 pairwise voltage-difference invariance under common rereferencing."""
    sample_rate = 128.0
    time = np.arange(512) / sample_rate
    signals = np.asarray(
        [
            np.sin(2.0 * np.pi * 10.0 * time + phase)
            for phase in (0.0, 0.3, 0.7, 1.2)
        ]
    )
    reference_shape = (
        np.sin(2.0 * np.pi * 1.3 * time)
        + 0.2 * np.cos(2.0 * np.pi * 7.0 * time)
    )
    return [
        {
            "reference_scale": scale,
            "max_pairwise_difference_error": common_reference_invariance_error(
                signals,
                scale * reference_shape,
            ),
        }
        for scale in (0.0, 0.1, 1.0, 10.0, 100.0)
    ]


def v22_lead_field_nonidentifiability() -> dict[str, float]:
    """V22 exact alternative source under an underdetermined lead field."""
    lead_field = np.asarray(
        [
            [1.0, 0.0, 0.0, 1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0, 0.0, 0.0, 1.0],
        ]
    )
    source = np.asarray([1.0, 2.0, 3.0, 0.0, 0.0, 0.0])
    direction = np.asarray([1.0, 0.0, 0.0, -1.0, 0.0, 0.0])
    direction = direction / np.linalg.norm(direction)
    alternative = source + direction
    geometry = rank_nullity(lead_field)
    return {
        "n_sensors": float(lead_field.shape[0]),
        "n_sources": float(lead_field.shape[1]),
        "rank": float(geometry.rank),
        "nullity": float(geometry.nullity),
        "sensor_residual": float(
            np.linalg.norm(lead_field @ alternative - lead_field @ source)
        ),
        "source_separation": float(np.linalg.norm(alternative - source)),
    }


def v23_regularization_path() -> list[dict[str, float]]:
    """V23 source estimates from one measurement under different L2 priors."""
    lead_field = np.asarray(
        [
            [1.0, 0.0, 0.0, 0.9, 0.0, 0.0],
            [0.0, 0.3, 0.0, 0.0, 0.25, 0.0],
            [0.0, 0.0, 0.05, 0.0, 0.0, 0.04],
        ]
    )
    source = np.asarray([1.0, 1.0, 1.0, 0.2, 0.2, 0.2])
    measurement = lead_field @ source
    rows: list[dict[str, float]] = []
    for regularization in (1e-6, 1e-4, 1e-2, 1e-1, 1.0):
        estimate = tikhonov_source_estimate(
            lead_field,
            measurement,
            regularization=regularization,
        )
        rows.append(
            {
                "regularization": regularization,
                "estimate_norm": float(np.linalg.norm(estimate)),
                "measurement_residual": float(
                    np.linalg.norm(lead_field @ estimate - measurement)
                ),
                "source_error_to_declared_generator": float(
                    np.linalg.norm(estimate - source)
                ),
            }
        )
    return rows


def v24_multimodal_nullity() -> list[dict[str, float]]:
    """V24 constructive EEG/MEG complementarity without claiming uniqueness."""
    eeg = np.asarray(
        [
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
        ]
    )
    meg = np.asarray(
        [
            [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
            [1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        ]
    )
    eeg_geometry = rank_nullity(eeg)
    meg_geometry = rank_nullity(meg)
    combined = stacked_rank_nullity(eeg, meg)
    return [
        {
            "modality_code": 1.0,
            "rank": float(eeg_geometry.rank),
            "nullity": float(eeg_geometry.nullity),
        },
        {
            "modality_code": 2.0,
            "rank": float(meg_geometry.rank),
            "nullity": float(meg_geometry.nullity),
        },
        {
            "modality_code": 3.0,
            "rank": float(combined.rank),
            "nullity": float(combined.nullity),
        },
    ]


def v25_forward_model_perturbation_grid() -> list[dict[str, float]]:
    """V25 verify the operator-norm forward-model mismatch bound."""
    lead_field = np.asarray(
        [
            [1.0, 0.2, 0.0, 0.1, 0.0, 0.1],
            [0.0, 0.8, 0.1, 0.0, 0.2, 0.0],
            [0.1, 0.0, 0.6, 0.2, 0.0, 0.1],
            [0.0, 0.1, 0.0, 0.7, 0.2, 0.2],
        ]
    )
    direction = np.asarray(
        [
            [0.5, -0.2, 0.1, 0.0, 0.3, -0.1],
            [-0.1, 0.4, 0.0, 0.2, -0.2, 0.1],
            [0.2, 0.1, -0.3, 0.4, 0.0, 0.2],
            [0.0, -0.2, 0.2, -0.1, 0.5, 0.3],
        ]
    )
    direction = direction / np.linalg.norm(direction, 2)
    source = np.asarray([1.0, -0.5, 0.8, 0.2, -0.3, 0.4])
    rows: list[dict[str, float]] = []
    for scale in (0.0, 0.001, 0.01, 0.05, 0.1):
        perturbation = scale * direction
        mismatch = forward_model_mismatch(lead_field, perturbation, source)
        bound = forward_model_perturbation_bound(perturbation, source)
        rows.append(
            {
                "perturbation_operator_norm": float(np.linalg.norm(perturbation, 2)),
                "sensor_mismatch": mismatch,
                "upper_bound": bound,
                "bound_ratio": 0.0 if bound == 0.0 else mismatch / bound,
            }
        )
    return rows
