from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from consciousness_measurement.electromagnetic_sparse_simulations import (
    v36_coherence_and_welch_bound,
    v37_sparse_uniqueness_guarantee,
    v38_restricted_gram_conditioning,
    v39_nuisance_adjusted_fisher_information,
    v40_sequential_sensor_information_gain,
)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "docs" / "figures"


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _fmt(value: float) -> str:
    if value == 0.0:
        return "0"
    if abs(value) < 1e-4 or abs(value) >= 1e4:
        return f"{value:.6e}"
    return f"{value:.9f}".rstrip("0").rstrip(".")


def _bar(
    x: float,
    y: float,
    width: float,
    height: float,
    fraction: float,
    label: str,
    value: str,
) -> str:
    fill_width = max(min(fraction, 1.0), 0.0) * width
    return (
        f'<text x="{x:.1f}" y="{y - 10:.1f}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="15" fill="#435466">{label}</text>'
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{height:.1f}" '
        'rx="7" fill="#edf1f5"/>'
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{fill_width:.1f}" height="{height:.1f}" '
        'rx="7" fill="#486b84"/>'
        f'<text x="{x + width + 18:.1f}" y="{y + height - 5:.1f}" '
        'font-family="Arial, Helvetica, sans-serif" font-size="16" '
        f'font-weight="700" fill="#21364a">{value}</text>'
    )


def _render_svg(
    v36: list[dict[str, float | str]],
    v37: list[dict[str, float | str]],
    v38: list[dict[str, float]],
    v39: list[dict[str, float | str]],
    v40: list[dict[str, float | str]],
) -> str:
    coherence = {str(row["dictionary"]): row for row in v36}
    uniqueness = {str(row["dictionary"]): row for row in v37}
    nuisance = {str(row["nuisance_case"]): row for row in v39}
    gains = {str(row["candidate"]): row for row in v40}
    restricted = {int(float(row["sparsity"])): row for row in v38}

    nuisance_bars = "".join(
        (
            _bar(
                110.0,
                650.0 + index * 82.0,
                410.0,
                24.0,
                float(nuisance[name]["nuisance_adjusted_information"]),
                label,
                _fmt(float(nuisance[name]["nuisance_adjusted_information"])),
            )
        )
        for index, (name, label) in enumerate(
            (
                ("orthogonal", "Orthogonal nuisance"),
                ("partial_30deg", "30 degree target-nuisance angle"),
                ("contains_target", "Nuisance contains target"),
            )
        )
    )

    max_gain = max(float(row["determinant_lemma_gain"]) for row in v40)
    gain_bars = "".join(
        (
            _bar(
                920.0,
                650.0 + index * 82.0,
                410.0,
                24.0,
                float(gains[name]["determinant_lemma_gain"]) / max_gain,
                label,
                _fmt(float(gains[name]["determinant_lemma_gain"])),
            )
        )
        for index, (name, label) in enumerate(
            (
                ("strong_direction", "Already-strong direction"),
                ("mixed_direction", "Mixed direction"),
                ("weak_direction", "Weak-information direction"),
            )
        )
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
  <rect width="1600" height="1000" fill="#ffffff"/>
  <text x="80" y="68" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#13243a">Research III V36-V40: sparse identifiability and nuisance-aware information</text>
  <text x="80" y="108" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#526273">Coherence limits, sparse uniqueness guarantees, restricted conditioning, nuisance-adjusted Fisher information, and sequential sensor value.</text>

  <rect x="80" y="155" width="455" height="330" rx="20" fill="#f6f8fa" stroke="#cbd5df" stroke-width="2"/>
  <text x="115" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#274e6b">V36-V37 coherence and sparse uniqueness</text>
  <text x="115" y="252" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">Regular-simplex coherence</text>
  <text x="495" y="252" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#274e6b">{_fmt(float(coherence["regular_simplex"]["mutual_coherence"]))}</text>
  <text x="115" y="296" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">Welch lower bound</text>
  <text x="495" y="296" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#274e6b">{_fmt(float(coherence["regular_simplex"]["welch_lower_bound"]))}</text>
  <text x="115" y="340" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">Simplex strict k threshold</text>
  <text x="495" y="340" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#274e6b">{_fmt(float(uniqueness["regular_simplex"]["strict_sparsity_threshold"]))}</text>
  <text x="115" y="384" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">Coherent strict k threshold</text>
  <text x="495" y="384" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#274e6b">{_fmt(float(uniqueness["coherent"]["strict_sparsity_threshold"]))}</text>
  <text x="115" y="438" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#667687">The coherence bound is sufficient, not necessary, and depends on the declared sparse linear model.</text>

  <rect x="570" y="155" width="455" height="330" rx="20" fill="#f8f8f5" stroke="#d1d6c8" stroke-width="2"/>
  <text x="605" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#4f6640">V38 restricted Gram conditioning</text>
  <text x="605" y="252" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">k = 2 lower bound / observed</text>
  <text x="985" y="252" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#4f6640">{_fmt(float(restricted[2]["gershgorin_lower_bound"]))} / {_fmt(float(restricted[2]["observed_minimum_eigenvalue"]))}</text>
  <text x="605" y="298" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">k = 2 upper bound / observed</text>
  <text x="985" y="298" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#4f6640">{_fmt(float(restricted[2]["gershgorin_upper_bound"]))} / {_fmt(float(restricted[2]["observed_maximum_eigenvalue"]))}</text>
  <text x="605" y="344" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">k = 3 lower bound / observed</text>
  <text x="985" y="344" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#4f6640">{_fmt(float(restricted[3]["gershgorin_lower_bound"]))} / {_fmt(float(restricted[3]["observed_minimum_eigenvalue"]))}</text>
  <text x="605" y="390" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">k = 3 upper bound / observed</text>
  <text x="985" y="390" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#4f6640">{_fmt(float(restricted[3]["gershgorin_upper_bound"]))} / {_fmt(float(restricted[3]["observed_maximum_eigenvalue"]))}</text>
  <text x="605" y="438" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#667687">Restricted support conditioning is bounded by coherence but is not summarized by coherence alone.</text>

  <rect x="1060" y="155" width="460" height="330" rx="20" fill="#faf7f8" stroke="#dacdd2" stroke-width="2"/>
  <text x="1095" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#725064">Design interpretation</text>
  <text x="1095" y="252" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">Low coherence</text>
  <text x="1095" y="282" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#667687">reduces worst pairwise source-column similarity</text>
  <text x="1095" y="330" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">Nuisance adjustment</text>
  <text x="1095" y="360" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#667687">removes information explainable by nuisance parameters</text>
  <text x="1095" y="408" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#425466">Sequential logdet gain</text>
  <text x="1095" y="438" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#667687">prioritizes measurements that fill weak information directions</text>

  <rect x="80" y="530" width="710" height="375" rx="20" fill="#fbfcfd" stroke="#d5dde5" stroke-width="2"/>
  <text x="115" y="580" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#31566f">V39 nuisance-adjusted Fisher information</text>
  <text x="115" y="610" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#667687">Efficient target information after the nuisance block is removed by its Fisher Schur complement.</text>
  {nuisance_bars}

  <rect x="830" y="530" width="690" height="375" rx="20" fill="#f9fbf8" stroke="#d3ddd0" stroke-width="2"/>
  <text x="865" y="580" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#49664d">V40 sequential sensor information gain</text>
  <text x="865" y="610" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#667687">Exact log determinant gain from the matrix determinant lemma, normalized visually to the best candidate.</text>
  {gain_bars}

  <text x="80" y="960" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#687785">Deterministic analytic and synthetic measurement-design validation. Sparse guarantees do not establish biological sparsity, unique neural truth, or direct measurement of consciousness or qualia.</text>
</svg>
"""


def main() -> None:
    v36 = v36_coherence_and_welch_bound()
    v37 = v37_sparse_uniqueness_guarantee()
    v38 = v38_restricted_gram_conditioning()
    v39 = v39_nuisance_adjusted_fisher_information()
    v40 = v40_sequential_sensor_information_gain()

    _write_csv(RESULTS / "v36_coherence_welch.csv", v36)
    _write_csv(RESULTS / "v37_sparse_uniqueness.csv", v37)
    _write_csv(RESULTS / "v38_restricted_conditioning.csv", v38)
    _write_csv(RESULTS / "v39_nuisance_adjusted_information.csv", v39)
    _write_csv(RESULTS / "v40_sequential_sensor_information.csv", v40)

    summary = {
        "status": "analytic_and_synthetic_only",
        "claim_boundary": (
            "coherence and sparsity guarantees are sufficient model-conditional results; "
            "they do not establish biological sparsity, uniquely true neural sources, "
            "or direct measurement of consciousness or qualia"
        ),
        "v36_coherence_and_welch_bound": v36,
        "v37_sparse_uniqueness_guarantee": v37,
        "v38_restricted_gram_conditioning": v38,
        "v39_nuisance_adjusted_fisher_information": v39,
        "v40_sequential_sensor_information_gain": v40,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "electromagnetic_sparse_validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    FIGURES.mkdir(parents=True, exist_ok=True)
    (
        FIGURES / "v36_v40_electromagnetic_sparse_validation.svg"
    ).write_text(
        _render_svg(v36, v37, v38, v39, v40),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
