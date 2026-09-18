"""Forward and inverse electromagnetic measurement utilities for Research III V21-V25.

The functions in this module formalize properties of multichannel EEG/MEG-style
measurement operators. They address reference invariance, source
non-identifiability, regularized inversion, multimodal complementarity, and
forward-model perturbation.

These are measurement-science utilities. They do not identify consciousness
with an electromagnetic field or with a reconstructed neural source.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class RankNullity:
    """Rank and right-nullity of a linear measurement operator."""

    rank: int
    nullity: int


@dataclass(frozen=True)
class NullspaceAlternative:
    """Two source vectors that produce the same ideal sensor measurement."""

    source: np.ndarray
    alternative: np.ndarray
    sensor_residual: float
    source_separation: float


def pairwise_sensor_differences(signals: np.ndarray) -> np.ndarray:
    """Return all unordered pairwise sensor differences.

    If every sensor is shifted by the same arbitrary reference waveform r(t),
    pairwise differences remain unchanged exactly.
    """
    x = _validate_signals(signals)
    return np.asarray(
        [
            x[i] - x[j]
            for i in range(x.shape[0] - 1)
            for j in range(i + 1, x.shape[0])
        ]
    )


def common_reference_invariance_error(
    signals: np.ndarray,
    reference_waveform: np.ndarray,
) -> float:
    """Return the maximum pairwise-difference error after common rereferencing."""
    x = _validate_signals(signals)
    reference = np.asarray(reference_waveform, dtype=float)
    if reference.ndim != 1 or reference.shape[0] != x.shape[1]:
        raise ValueError("reference_waveform must have one value per sample")
    if not np.all(np.isfinite(reference)):
        raise ValueError("reference_waveform must contain only finite values")
    original = pairwise_sensor_differences(x)
    rereferenced = pairwise_sensor_differences(x + reference[None, :])
    return float(np.max(np.abs(original - rereferenced)))


def rank_nullity(matrix: np.ndarray, *, tolerance: float | None = None) -> RankNullity:
    """Return numerical matrix rank and right-nullity."""
    operator = _validate_matrix(matrix)
    singular_values = np.linalg.svd(operator, compute_uv=False)
    tol = _svd_tolerance(operator, singular_values, tolerance)
    rank = int(np.count_nonzero(singular_values > tol))
    return RankNullity(rank=rank, nullity=operator.shape[1] - rank)


def right_nullspace(matrix: np.ndarray, *, tolerance: float | None = None) -> np.ndarray:
    """Return an orthonormal basis for the right null space as columns."""
    operator = _validate_matrix(matrix)
    _, singular_values, vh = np.linalg.svd(operator, full_matrices=True)
    tol = _svd_tolerance(operator, singular_values, tolerance)
    rank = int(np.count_nonzero(singular_values > tol))
    return vh[rank:].T.copy()


def nullspace_alternative(
    lead_field: np.ndarray,
    source: np.ndarray,
    *,
    scale: float = 1.0,
    tolerance: float | None = None,
) -> NullspaceAlternative:
    """Construct an alternative source with the same ideal sensor measurement.

    If L has a nontrivial right null space and v is any unit null vector, then
    L(j + scale*v) = L j. This is the core V22 non-identifiability result.
    """
    operator = _validate_matrix(lead_field)
    source_vector = _validate_source(source, operator.shape[1])
    if scale == 0.0 or not np.isfinite(scale):
        raise ValueError("scale must be finite and nonzero")
    basis = right_nullspace(operator, tolerance=tolerance)
    if basis.shape[1] == 0:
        raise ValueError("lead_field has trivial right null space")
    direction = basis[:, 0]
    alternative = source_vector + scale * direction
    residual = float(np.linalg.norm(operator @ alternative - operator @ source_vector))
    separation = float(np.linalg.norm(alternative - source_vector))
    return NullspaceAlternative(
        source=source_vector.copy(),
        alternative=alternative,
        sensor_residual=residual,
        source_separation=separation,
    )


def tikhonov_source_estimate(
    lead_field: np.ndarray,
    measurement: np.ndarray,
    *,
    regularization: float,
) -> np.ndarray:
    """Return the L2-regularized source estimate.

    The estimate minimizes ||L j - y||_2^2 + regularization*||j||_2^2.
    """
    operator = _validate_matrix(lead_field)
    y = np.asarray(measurement, dtype=float)
    if y.ndim != 1 or y.shape[0] != operator.shape[0]:
        raise ValueError("measurement length must equal the number of sensors")
    if not np.all(np.isfinite(y)):
        raise ValueError("measurement must contain only finite values")
    if regularization <= 0.0 or not np.isfinite(regularization):
        raise ValueError("regularization must be finite and positive")
    gram = operator.T @ operator
    rhs = operator.T @ y
    return np.linalg.solve(
        gram + regularization * np.eye(operator.shape[1]),
        rhs,
    )


def tikhonov_filter_factors(
    lead_field: np.ndarray,
    *,
    regularization: float,
) -> np.ndarray:
    """Return singular-direction Tikhonov gains s/(s^2+lambda)."""
    operator = _validate_matrix(lead_field)
    if regularization <= 0.0 or not np.isfinite(regularization):
        raise ValueError("regularization must be finite and positive")
    singular_values = np.linalg.svd(operator, compute_uv=False)
    return singular_values / (singular_values**2 + regularization)


def stacked_rank_nullity(*lead_fields: np.ndarray) -> RankNullity:
    """Return rank/nullity after stacking two or more measurement operators."""
    if len(lead_fields) < 2:
        raise ValueError("at least two lead fields are required")
    operators = [_validate_matrix(field) for field in lead_fields]
    n_sources = operators[0].shape[1]
    if any(operator.shape[1] != n_sources for operator in operators):
        raise ValueError("all lead fields must act on the same source dimension")
    return rank_nullity(np.vstack(operators))


def forward_model_perturbation_bound(
    perturbation: np.ndarray,
    source: np.ndarray,
) -> float:
    """Return ||Delta L||_2 ||j||_2, an upper bound on ||Delta L j||_2."""
    delta = _validate_matrix(perturbation)
    source_vector = _validate_source(source, delta.shape[1])
    return float(np.linalg.norm(delta, 2) * np.linalg.norm(source_vector))


def forward_model_mismatch(
    lead_field: np.ndarray,
    perturbation: np.ndarray,
    source: np.ndarray,
) -> float:
    """Return the sensor-space change caused by a lead-field perturbation."""
    operator = _validate_matrix(lead_field)
    delta = _validate_matrix(perturbation)
    if delta.shape != operator.shape:
        raise ValueError("lead_field and perturbation must have identical shape")
    source_vector = _validate_source(source, operator.shape[1])
    baseline = operator @ source_vector
    perturbed = (operator + delta) @ source_vector
    return float(np.linalg.norm(perturbed - baseline))


def _validate_signals(signals: np.ndarray) -> np.ndarray:
    x = np.asarray(signals, dtype=float)
    if x.ndim != 2 or x.shape[0] < 2 or x.shape[1] < 2:
        raise ValueError("signals must have shape (at least 2 sensors, at least 2 samples)")
    if not np.all(np.isfinite(x)):
        raise ValueError("signals must contain only finite values")
    return x


def _validate_matrix(matrix: np.ndarray) -> np.ndarray:
    operator = np.asarray(matrix, dtype=float)
    if operator.ndim != 2 or min(operator.shape) < 1:
        raise ValueError("matrix must be a nonempty two-dimensional array")
    if not np.all(np.isfinite(operator)):
        raise ValueError("matrix must contain only finite values")
    return operator


def _validate_source(source: np.ndarray, n_sources: int) -> np.ndarray:
    source_vector = np.asarray(source, dtype=float)
    if source_vector.ndim != 1 or source_vector.shape[0] != n_sources:
        raise ValueError("source length must match the operator source dimension")
    if not np.all(np.isfinite(source_vector)):
        raise ValueError("source must contain only finite values")
    return source_vector


def _svd_tolerance(
    matrix: np.ndarray,
    singular_values: np.ndarray,
    tolerance: float | None,
) -> float:
    if tolerance is not None:
        if tolerance < 0.0 or not np.isfinite(tolerance):
            raise ValueError("tolerance must be finite and nonnegative")
        return tolerance
    if singular_values.size == 0:
        return 0.0
    return float(
        np.finfo(float).eps
        * max(matrix.shape)
        * singular_values[0]
    )
