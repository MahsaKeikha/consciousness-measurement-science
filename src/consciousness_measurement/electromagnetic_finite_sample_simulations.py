from __future__ import annotations

import numpy as np

from .electromagnetic_finite_sample import (
    gaussian_equal_covariance_bayes_error,
    gaussian_two_sided_interval_half_width,
    gls_amplitude_estimate,
    gls_amplitude_information,
    gls_amplitude_variance,
    independent_two_sided_fwer,
    independent_two_sided_fwer_threshold,
    inverse_sample_covariance_bias_factor,
    nominal_weighted_amplitude_variance,
    weighted_amplitude_variance,
)


def v36_gls_amplitude_efficiency(
    *,
    seed: int = 20260918,
    trials: int = 40_000,
) -> dict[str, float]:
    topography = np.asarray([1.0, 0.5, -0.2])
    covariance = np.asarray(
        [
            [1.0, 0.3, 0.1],
            [0.3, 0.8, 0.2],
            [0.1, 0.2, 0.6],
        ]
    )
    true_amplitude = 1.2
    information = gls_amplitude_information(topography, covariance)
    exact_variance = gls_amplitude_variance(topography, covariance)
    half_width = gaussian_two_sided_interval_half_width(exact_variance, 0.95)

    rng = np.random.default_rng(seed)
    noise = rng.multivariate_normal(
        mean=np.zeros(topography.size),
        cov=covariance,
        size=trials,
    )
    measurements = true_amplitude * topography + noise
    precision_topography = np.linalg.solve(covariance, topography)
    estimates = measurements @ precision_topography / information
    empirical_mean = float(np.mean(estimates))
    empirical_variance = float(np.var(estimates, ddof=1))
    empirical_coverage = float(
        np.mean(np.abs(estimates - true_amplitude) <= half_width)
    )

    first_estimate = gls_amplitude_estimate(
        topography,
        measurements[0],
        covariance,
    )
    return {
        "seed": float(seed),
        "trials": float(trials),
        "true_amplitude": true_amplitude,
        "fisher_information": information,
        "exact_variance": exact_variance,
        "crlb_variance": exact_variance,
        "interval_half_width_95": half_width,
        "empirical_mean": empirical_mean,
        "empirical_variance": empirical_variance,
        "empirical_coverage_95": empirical_coverage,
        "first_scalar_estimate": first_estimate,
    }


def v37_inverse_covariance_bias() -> list[dict[str, float]]:
    dimension = 4
    rows: list[dict[str, float]] = []
    for degrees_of_freedom in (6, 10, 20, 50):
        rows.append(
            {
                "dimension": float(dimension),
                "degrees_of_freedom": float(degrees_of_freedom),
                "inverse_covariance_bias_factor": inverse_sample_covariance_bias_factor(
                    dimension,
                    degrees_of_freedom,
                ),
            }
        )
    return rows


def v38_gaussian_source_discrimination() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for mahalanobis_squared in (0.0, 0.25, 1.0, 4.0, 9.0):
        rows.append(
            {
                "mahalanobis_squared": mahalanobis_squared,
                "mahalanobis_distance": float(np.sqrt(mahalanobis_squared)),
                "equal_prior_bayes_error": gaussian_equal_covariance_bayes_error(
                    mahalanobis_squared
                ),
            }
        )
    return rows


def v39_independent_search_fwer(
    *,
    alpha: float = 0.05,
) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for comparisons in (1, 10, 100, 1000):
        threshold = independent_two_sided_fwer_threshold(alpha, comparisons)
        rows.append(
            {
                "comparisons": float(comparisons),
                "target_fwer": alpha,
                "two_sided_z_threshold": threshold,
                "realized_fwer": independent_two_sided_fwer(
                    threshold,
                    comparisons,
                ),
            }
        )
    return rows


def v40_covariance_mismatch_sandwich() -> list[dict[str, float | str]]:
    topography = np.asarray([1.0, 0.4, -0.3])
    true_covariance = np.asarray(
        [
            [1.0, 0.6, 0.0],
            [0.6, 1.0, 0.2],
            [0.0, 0.2, 0.8],
        ]
    )
    weight_matrices = {
        "oracle_precision": np.linalg.inv(true_covariance),
        "identity_weight": np.eye(3),
        "diagonal_precision": np.diag(1.0 / np.diag(true_covariance)),
    }

    rows: list[dict[str, float | str]] = []
    for name, weight in weight_matrices.items():
        exact_variance = weighted_amplitude_variance(
            topography,
            true_covariance,
            weight,
        )
        nominal_variance = nominal_weighted_amplitude_variance(
            topography,
            weight,
        )
        rows.append(
            {
                "weight_model": name,
                "exact_sandwich_variance": exact_variance,
                "nominal_precision_variance": nominal_variance,
                "variance_ratio_exact_over_nominal": exact_variance
                / nominal_variance,
            }
        )
    return rows
