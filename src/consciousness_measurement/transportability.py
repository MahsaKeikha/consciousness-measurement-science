from __future__ import annotations

import numpy as np


def _vector(values: np.ndarray | list[float], *, name: str) -> np.ndarray:
    vector = np.asarray(values, dtype=float)
    if vector.ndim != 1 or vector.size == 0:
        raise ValueError(f"{name} must be a nonempty one-dimensional vector")
    if not np.all(np.isfinite(vector)):
        raise ValueError(f"{name} must contain only finite values")
    return vector


def _matrix(values: np.ndarray | list[list[float]], *, name: str) -> np.ndarray:
    matrix = np.asarray(values, dtype=float)
    if matrix.ndim != 2 or matrix.size == 0:
        raise ValueError(f"{name} must be a nonempty two-dimensional matrix")
    if not np.all(np.isfinite(matrix)):
        raise ValueError(f"{name} must contain only finite values")
    return matrix


def _positive_definite_covariance(
    values: np.ndarray | list[list[float]],
    *,
    name: str,
) -> np.ndarray:
    covariance = _matrix(values, name=name)
    if covariance.shape[0] != covariance.shape[1]:
        raise ValueError(f"{name} must be square")
    if not np.allclose(covariance, covariance.T, rtol=1e-10, atol=1e-12):
        raise ValueError(f"{name} must be symmetric")
    try:
        np.linalg.cholesky(covariance)
    except np.linalg.LinAlgError as exc:
        raise ValueError(f"{name} must be positive definite") from exc
    return covariance


def _probability_vector(
    values: np.ndarray | list[float],
    *,
    name: str,
) -> np.ndarray:
    probabilities = _vector(values, name=name)
    if np.any(probabilities < 0.0):
        raise ValueError(f"{name} must be nonnegative")
    total = float(np.sum(probabilities))
    if not np.isclose(total, 1.0, rtol=1e-10, atol=1e-12):
        raise ValueError(f"{name} must sum to one")
    return probabilities


def scalar_amplitude_information(
    topography: np.ndarray | list[float],
    covariance: np.ndarray | list[list[float]],
) -> float:
    """Fisher information for a scalar amplitude in a Gaussian linear sensor model."""
    topography = _vector(topography, name="topography")
    covariance = _positive_definite_covariance(covariance, name="covariance")
    if covariance.shape[0] != topography.size:
        raise ValueError("topography and covariance dimensions must match")
    solved = np.linalg.solve(covariance, topography)
    return float(np.dot(topography, solved))


def gls_scalar_amplitude_estimate(
    observation: np.ndarray | list[float],
    topography: np.ndarray | list[float],
    covariance: np.ndarray | list[list[float]],
) -> float:
    """Generalized least-squares estimate of one scalar source amplitude."""
    observation = _vector(observation, name="observation")
    topography = _vector(topography, name="topography")
    covariance = _positive_definite_covariance(covariance, name="covariance")
    if observation.shape != topography.shape:
        raise ValueError("observation and topography must have matching shapes")
    if covariance.shape[0] != topography.size:
        raise ValueError("topography and covariance dimensions must match")
    solved_topography = np.linalg.solve(covariance, topography)
    solved_observation = np.linalg.solve(covariance, observation)
    denominator = float(np.dot(topography, solved_topography))
    return float(np.dot(topography, solved_observation) / denominator)


def transformed_sensor_model(
    observation: np.ndarray | list[float],
    topography: np.ndarray | list[float],
    covariance: np.ndarray | list[list[float]],
    transform: np.ndarray | list[list[float]],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Apply a declared linear sensor-coordinate transform to the full Gaussian model."""
    observation = _vector(observation, name="observation")
    topography = _vector(topography, name="topography")
    covariance = _positive_definite_covariance(covariance, name="covariance")
    transform = _matrix(transform, name="transform")
    if observation.shape != topography.shape:
        raise ValueError("observation and topography must have matching shapes")
    if covariance.shape[0] != topography.size:
        raise ValueError("topography and covariance dimensions must match")
    if transform.shape[1] != topography.size:
        raise ValueError("transform input dimension must match the sensor dimension")
    return (
        transform @ observation,
        transform @ topography,
        transform @ covariance @ transform.T,
    )


def projected_scalar_information(
    topography: np.ndarray | list[float],
    covariance: np.ndarray | list[list[float]],
    projection: np.ndarray | list[list[float]],
) -> float:
    """Fisher information retained after a full-row-rank linear sensor projection."""
    topography = _vector(topography, name="topography")
    covariance = _positive_definite_covariance(covariance, name="covariance")
    projection = _matrix(projection, name="projection")
    if covariance.shape[0] != topography.size:
        raise ValueError("topography and covariance dimensions must match")
    if projection.shape[1] != topography.size:
        raise ValueError("projection input dimension must match the sensor dimension")
    projected_topography = projection @ topography
    projected_covariance = projection @ covariance @ projection.T
    projected_covariance = _positive_definite_covariance(
        projected_covariance,
        name="projected_covariance",
    )
    return scalar_amplitude_information(projected_topography, projected_covariance)


def mismatched_topography_gain(
    nominal_topography: np.ndarray | list[float],
    true_topography: np.ndarray | list[float],
    weight_matrix: np.ndarray | list[list[float]],
) -> float:
    """Expected amplitude gain when a nominal topography is used for a different true one."""
    nominal = _vector(nominal_topography, name="nominal_topography")
    true = _vector(true_topography, name="true_topography")
    weight = _positive_definite_covariance(weight_matrix, name="weight_matrix")
    if nominal.shape != true.shape:
        raise ValueError("nominal_topography and true_topography must match")
    if weight.shape[0] != nominal.size:
        raise ValueError("topographies and weight_matrix dimensions must match")
    denominator = float(nominal @ weight @ nominal)
    return float((nominal @ weight @ true) / denominator)


def mismatched_topography_relative_bias_bound(
    nominal_topography: np.ndarray | list[float],
    true_topography: np.ndarray | list[float],
    weight_matrix: np.ndarray | list[list[float]],
) -> float:
    """Cauchy-Schwarz bound on absolute relative amplitude bias from topography mismatch."""
    nominal = _vector(nominal_topography, name="nominal_topography")
    true = _vector(true_topography, name="true_topography")
    weight = _positive_definite_covariance(weight_matrix, name="weight_matrix")
    if nominal.shape != true.shape:
        raise ValueError("nominal_topography and true_topography must match")
    if weight.shape[0] != nominal.size:
        raise ValueError("topographies and weight_matrix dimensions must match")
    mismatch = true - nominal
    nominal_norm = float(np.sqrt(nominal @ weight @ nominal))
    mismatch_norm = float(np.sqrt(mismatch @ weight @ mismatch))
    return mismatch_norm / nominal_norm


def importance_weights(
    source_probabilities: np.ndarray | list[float],
    target_probabilities: np.ndarray | list[float],
) -> np.ndarray:
    """Exact discrete density-ratio weights for a target distribution over source support."""
    source = _probability_vector(source_probabilities, name="source_probabilities")
    target = _probability_vector(target_probabilities, name="target_probabilities")
    if source.shape != target.shape:
        raise ValueError("source_probabilities and target_probabilities must match")
    if np.any((source == 0.0) & (target > 0.0)):
        raise ValueError("target support must be contained in source support")
    weights = np.zeros_like(source)
    positive = source > 0.0
    weights[positive] = target[positive] / source[positive]
    return weights


def importance_weighted_expectation(
    values: np.ndarray | list[float],
    source_probabilities: np.ndarray | list[float],
    target_probabilities: np.ndarray | list[float],
) -> float:
    """Target expectation written exactly as a source expectation with density-ratio weights."""
    values = _vector(values, name="values")
    source = _probability_vector(source_probabilities, name="source_probabilities")
    target = _probability_vector(target_probabilities, name="target_probabilities")
    if not (values.shape == source.shape == target.shape):
        raise ValueError("values and probability vectors must have matching shapes")
    weights = importance_weights(source, target)
    return float(np.dot(source, weights * values))


def population_effective_sample_fraction(
    source_probabilities: np.ndarray | list[float],
    target_probabilities: np.ndarray | list[float],
) -> float:
    """Population analogue of normalized importance-weight effective sample size."""
    source = _probability_vector(source_probabilities, name="source_probabilities")
    target = _probability_vector(target_probabilities, name="target_probabilities")
    if source.shape != target.shape:
        raise ValueError("source_probabilities and target_probabilities must match")
    weights = importance_weights(source, target)
    second_moment = float(np.dot(source, np.square(weights)))
    return 1.0 / second_moment


def total_variation_distance(
    first_probabilities: np.ndarray | list[float],
    second_probabilities: np.ndarray | list[float],
) -> float:
    """Total variation distance between two discrete distributions."""
    first = _probability_vector(first_probabilities, name="first_probabilities")
    second = _probability_vector(second_probabilities, name="second_probabilities")
    if first.shape != second.shape:
        raise ValueError("probability vectors must have matching shapes")
    return 0.5 * float(np.sum(np.abs(first - second)))


def bounded_expectation_shift_bound(
    lower: float,
    upper: float,
    first_probabilities: np.ndarray | list[float],
    second_probabilities: np.ndarray | list[float],
) -> float:
    """Sharp total-variation bound for expectations of a variable in [lower, upper]."""
    lower = float(lower)
    upper = float(upper)
    if not np.isfinite(lower) or not np.isfinite(upper) or upper < lower:
        raise ValueError("lower and upper must be finite with upper >= lower")
    tv = total_variation_distance(first_probabilities, second_probabilities)
    return (upper - lower) * tv
