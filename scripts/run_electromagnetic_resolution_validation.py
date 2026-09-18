from __future__ import annotations

import csv
import json
from pathlib import Path

from consciousness_measurement.electromagnetic_resolution_simulations import (
    v26_correlated_noise_whitening,
    v27_resolution_leakage_path,
    v28_correlated_noise_fisher_information,
    v29_temporal_aliasing,
    v30_inverse_noise_amplification,
)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "docs" / "figures"


def _write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: float) -> str:
    if value == 0.0:
        return "0"
    if abs(value) >= 1000 or abs(value) < 1e-3:
        return f"{value:.6e}"
    return f"{value:.9f}".rstrip("0").rstrip(".")


def _svg(
    *,
    v26: dict[str, float],
    v27: list[dict[str, float]],
    v28: list[dict[str, float]],
    v29: dict[str, float],
    v30: list[dict[str, float]],
) -> str:
    x27 = [220 + 120 * i for i in range(len(v27))]
    y27 = [
        730 - 300 * row["identity_error"]
        for row in v27
    ]
    points27 = " ".join(
        f"{x},{y:.2f}" for x, y in zip(x27, y27, strict=True)
    )

    x28 = [760 + 115 * i for i in range(len(v28))]
    y28 = [
        735 - 70 * row["fisher_information"]
        for row in v28
    ]
    points28 = " ".join(
        f"{x},{y:.2f}" for x, y in zip(x28, y28, strict=True)
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
  <rect width="1600" height="1000" fill="#ffffff"/>
  <text x="85" y="72" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#13243a">Research III V26-V30: electromagnetic resolution and information limits</text>
  <text x="85" y="112" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#46586c">Correlated noise, inverse leakage, Fisher information, temporal aliasing, and singular-direction noise amplification.</text>

  <rect x="85" y="155" width="455" height="245" rx="20" fill="#f5f8fb" stroke="#c7d3df" stroke-width="2"/>
  <text x="120" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#173b63">V26 correlated-noise whitening</text>
  <text x="120" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Weighted residual energy</text>
  <text x="500" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(v26["weighted_residual_energy"])}</text>
  <text x="120" y="296" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Whitened residual energy</text>
  <text x="500" y="296" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(v26["whitened_residual_energy"])}</text>
  <text x="120" y="342" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Absolute identity error</text>
  <text x="500" y="342" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#173b63">{_fmt(v26["absolute_identity_error"])}</text>
  <text x="120" y="375" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Whitening converts Mahalanobis geometry to Euclidean geometry.</text>

  <rect x="570" y="155" width="455" height="245" rx="20" fill="#f7f8f4" stroke="#ced4c2" stroke-width="2"/>
  <text x="605" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#3b5b32">V29 temporal aliasing</text>
  <text x="605" y="250" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Sample rate</text>
  <text x="985" y="250" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(v29["sample_rate_hz"])} Hz</text>
  <text x="605" y="296" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Continuous frequencies</text>
  <text x="985" y="296" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(v29["frequency_hz"])} / {_fmt(v29["alias_frequency_hz"])} Hz</text>
  <text x="605" y="342" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Max sample difference</text>
  <text x="985" y="342" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(v29["max_sample_difference"])}</text>
  <text x="605" y="375" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Distinct continuous frequencies can be observationally identical after sampling.</text>

  <rect x="1055" y="155" width="460" height="245" rx="20" fill="#faf6f8" stroke="#d8c8d0" stroke-width="2"/>
  <text x="1090" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#6a3f57">V30 inverse noise amplification</text>
  <text x="1090" y="252" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Smallest singular value</text>
  <text x="1470" y="252" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{_fmt(v30[-1]["smallest_singular_value"])}</text>
  <text x="1090" y="300" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Pseudoinverse norm</text>
  <text x="1470" y="300" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{_fmt(v30[-1]["pseudoinverse_norm"])}</text>
  <text x="1090" y="348" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Realized amplification</text>
  <text x="1470" y="348" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#6a3f57">{_fmt(v30[-1]["realized_noise_amplification"])}</text>
  <text x="1090" y="378" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Noise aligned with the weakest singular direction reaches the inverse bound.</text>

  <rect x="85" y="440" width="680" height="455" rx="20" fill="#fbfbfc" stroke="#d4d9df" stroke-width="2"/>
  <text x="120" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#294f64">V27 inverse resolution leakage</text>
  <text x="120" y="522" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">The normalized distance from ideal identity resolution remains nonzero.</text>
  <line x1="220" y1="760" x2="580" y2="760" stroke="#8795a5" stroke-width="2"/>
  <line x1="220" y1="450" x2="220" y2="760" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{points27}" fill="none" stroke="#294f64" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="400" y="810" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">increasing regularization</text>
  <text x="150" y="610" transform="rotate(-90 150 610)" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">identity error</text>
  <text x="120" y="850" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Rank-only normalized error floor: {_fmt(v27[0]["rank_lower_bound"])}</text>
  <text x="120" y="875" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Off-diagonal resolution energy records source leakage and cross-talk.</text>

  <rect x="795" y="440" width="720" height="455" rx="20" fill="#f8faf8" stroke="#ced8ce" stroke-width="2"/>
  <text x="830" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#43634a">V28 Fisher information under common sensor noise</text>
  <text x="830" y="522" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Information falls as correlated noise grows along the measured topography.</text>
  <line x1="760" y1="760" x2="1105" y2="760" stroke="#8795a5" stroke-width="2"/>
  <line x1="760" y1="450" x2="760" y2="760" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{points28}" fill="none" stroke="#43634a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="935" y="810" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">common-noise correlation</text>
  <text x="690" y="610" transform="rotate(-90 690 610)" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">Fisher information</text>
  <text x="1160" y="590" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#34495e">rho = 0: I = {_fmt(v28[0]["fisher_information"])}</text>
  <text x="1160" y="630" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#34495e">rho = 0.9: I = {_fmt(v28[-1]["fisher_information"])}</text>
  <text x="1160" y="685" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">The CRLB variance therefore rises from</text>
  <text x="1160" y="713" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">{_fmt(v28[0]["crlb_variance"])} to {_fmt(v28[-1]["crlb_variance"])}.</text>

  <text x="85" y="955" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6a7684">Deterministic synthetic measurement validation. No human empirical data and no direct measurement of consciousness or qualia.</text>
</svg>
"""


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    v26 = v26_correlated_noise_whitening()
    v27 = v27_resolution_leakage_path()
    v28 = v28_correlated_noise_fisher_information()
    v29 = v29_temporal_aliasing()
    v30 = v30_inverse_noise_amplification()

    _write_csv(RESULTS / "v26_correlated_noise_whitening.csv", [v26])
    _write_csv(RESULTS / "v27_resolution_leakage.csv", v27)
    _write_csv(RESULTS / "v28_fisher_information.csv", v28)
    _write_csv(RESULTS / "v29_temporal_aliasing.csv", [v29])
    _write_csv(RESULTS / "v30_inverse_noise_amplification.csv", v30)
    (RESULTS / "electromagnetic_resolution_validation_summary.json").write_text(
        json.dumps(
            {
                "status": "analytic_and_synthetic_only",
                "claim_boundary": (
                    "resolution and information limits do not identify "
                    "consciousness or remove electromagnetic inverse ambiguity"
                ),
                "v26_correlated_noise_whitening": v26,
                "v27_resolution_leakage": v27,
                "v28_fisher_information": v28,
                "v29_temporal_aliasing": v29,
                "v30_inverse_noise_amplification": v30,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    (FIGURES / "v26_v30_electromagnetic_resolution_validation.svg").write_text(
        _svg(v26=v26, v27=v27, v28=v28, v29=v29, v30=v30),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
