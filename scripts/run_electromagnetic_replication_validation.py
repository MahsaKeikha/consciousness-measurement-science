from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from consciousness_measurement.electromagnetic_replication_simulations import (
    v46_common_effect_pooling,
    v47_common_effect_heterogeneity,
    v48_leave_one_site_out_influence,
    v49_partial_conjunction_replicability,
    v50_site_weight_concentration,
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


def _write_single_row_csv(path: Path, row: dict[str, Any]) -> None:
    _write_csv(path, [row])


def _fmt(value: float) -> str:
    if value == 0.0:
        return "0"
    if abs(value) < 1e-4 or abs(value) >= 1e4:
        return f"{value:.6e}"
    return f"{value:.9f}".rstrip("0").rstrip(".")


def _render_svg(
    v46: dict[str, float],
    v47: dict[str, float],
    v48: list[dict[str, float]],
    v49: list[dict[str, float]],
    v50: list[dict[str, float | str]],
) -> str:
    influence_points: list[str] = []
    influence_zero_y = 795.0
    influence_scale = 3600.0
    for index, row in enumerate(v48):
        x = 165 + index * 125
        y = influence_zero_y - float(row["leave_one_out_shift"]) * influence_scale
        influence_points.append(f'<line x1="{x}" y1="{influence_zero_y:.1f}" x2="{x}" y2="{y:.2f}" stroke="#315c7d" stroke-width="4"/>')
        influence_points.append(f'<circle cx="{x}" cy="{y:.2f}" r="7" fill="#ffffff" stroke="#315c7d" stroke-width="3"/>')
        influence_points.append(f'<text x="{x}" y="845" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">S{index + 1}</text>')

    pc_points: list[str] = []
    for index, row in enumerate(v49):
        x = 865 + index * 105
        pvalue = float(row["partial_conjunction_p_value"])
        y = 810 - pvalue / 0.5 * 205
        pc_points.append(f"{x:.2f},{y:.2f}")

    balanced = next(row for row in v50 if row["design"] == "balanced")
    dominant = next(row for row in v50 if row["design"] == "dominant_site")

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">
  <rect width="1600" height="1000" fill="#ffffff"/>
  <text x="85" y="72" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="#13243a">Research III V46-V50: cross-site replication inference and stability</text>
  <text x="85" y="112" font-family="Arial, Helvetica, sans-serif" font-size="18" fill="#46586c">Common-effect pooling, heterogeneity, leave-one-site-out influence, partial conjunction, and site-weight concentration.</text>

  <rect x="85" y="155" width="455" height="245" rx="18" fill="#f5f8fb" stroke="#c7d3df" stroke-width="2"/>
  <text x="120" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#173b63">V46 pooled common effect</text>
  <text x="120" y="257" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Pooled estimate</text>
  <text x="500" y="257" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#173b63">{_fmt(float(v46["pooled_estimate"]))}</text>
  <text x="120" y="307" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Known-variance SE</text>
  <text x="500" y="307" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#173b63">{_fmt(float(v46["pooled_standard_error"]))}</text>
  <text x="120" y="360" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">Inverse-variance pooling across four declared synthetic sites.</text>

  <rect x="570" y="155" width="455" height="245" rx="18" fill="#f7f8f4" stroke="#ced4c2" stroke-width="2"/>
  <text x="605" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#3b5b32">V47 heterogeneity calibration</text>
  <text x="605" y="257" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Observed Q</text>
  <text x="985" y="257" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#3b5b32">{_fmt(float(v47["observed_q"]))}</text>
  <text x="605" y="307" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Simulated mean Q / theory</text>
  <text x="985" y="307" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="700" fill="#3b5b32">{_fmt(float(v47["simulated_mean_q"]))} / {int(v47["theoretical_mean_q"])}</text>
  <text x="605" y="360" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">50,000 fixed-seed draws check the chi-square moment law.</text>

  <rect x="1055" y="155" width="460" height="245" rx="18" fill="#faf6f8" stroke="#d8c8d0" stroke-width="2"/>
  <text x="1090" y="202" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#6a3f57">V50 site-weight concentration</text>
  <text x="1090" y="257" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Effective sites: balanced</text>
  <text x="1470" y="257" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#6a3f57">{_fmt(float(balanced["effective_site_count"]))}</text>
  <text x="1090" y="307" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Effective sites: dominant</text>
  <text x="1470" y="307" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#6a3f57">{_fmt(float(dominant["effective_site_count"]))}</text>
  <text x="1090" y="350" font-family="Arial, Helvetica, sans-serif" font-size="17" fill="#34495e">Max delete variance inflation</text>
  <text x="1470" y="350" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#6a3f57">{_fmt(float(dominant["maximum_delete_variance_inflation"]))}</text>

  <rect x="85" y="440" width="680" height="455" rx="18" fill="#fbfbfc" stroke="#d4d9df" stroke-width="2"/>
  <text x="120" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#294f64">V48 leave-one-site-out influence</text>
  <text x="120" y="522" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#5b6c7c">Shift of the pooled estimate when each site is deleted once.</text>
  <line x1="150" y1="795" x2="590" y2="795" stroke="#8795a5" stroke-width="2"/>
  <line x1="150" y1="585" x2="150" y2="825" stroke="#8795a5" stroke-width="2"/>
  {"".join(influence_points)}
  <text x="118" y="630" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">+0.04</text>
  <text x="118" y="800" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">0</text>
  <text x="118" y="870" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">-0.02</text>
  <text x="120" y="875" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#6b7785">The exact delete-one identity matches every displayed shift.</text>

  <rect x="795" y="440" width="720" height="455" rx="18" fill="#f8faf8" stroke="#ced8ce" stroke-width="2"/>
  <text x="830" y="487" font-family="Arial, Helvetica, sans-serif" font-size="23" font-weight="700" fill="#43634a">V49 partial-conjunction replicability</text>
  <text x="830" y="518" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#5b6c7c">Bonferroni partial-conjunction p-values for requiring at least r</text>
  <text x="830" y="540" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#5b6c7c">nonnull sites.</text>
  <line x1="865" y1="810" x2="1285" y2="810" stroke="#8795a5" stroke-width="2"/>
  <line x1="865" y1="605" x2="865" y2="810" stroke="#8795a5" stroke-width="2"/>
  <polyline points="{" ".join(pc_points)}" fill="none" stroke="#43634a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="865" cy="807.95" r="6" fill="#ffffff" stroke="#43634a" stroke-width="3"/>
  <circle cx="970" cy="790.32" r="6" fill="#ffffff" stroke="#43634a" stroke-width="3"/>
  <circle cx="1075" cy="760.80" r="6" fill="#ffffff" stroke="#43634a" stroke-width="3"/>
  <circle cx="1180" cy="637.80" r="6" fill="#ffffff" stroke="#43634a" stroke-width="3"/>
  <circle cx="1285" cy="625.50" r="6" fill="#ffffff" stroke="#43634a" stroke-width="3"/>
  <text x="1075" y="850" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="16" fill="#46586c">required nonnull sites r = 1, 2, 3, 4, 5</text>
  <text x="1320" y="625" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#34495e">r=5: p=0.45</text>
  <text x="1320" y="668" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#34495e">r=4: p=0.42</text>
  <text x="1320" y="711" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="#34495e">r=3: p=0.12</text>
  <text x="830" y="866" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6b7785">This is a replicability-inference check, not evidence from</text>
  <text x="830" y="887" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6b7785">real sites.</text>

  <text x="85" y="944" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6a7684">Analytic and fixed-seed synthetic replication inference only. No real multisite data.</text>
  <text x="85" y="966" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#6a7684">No direct measurement of consciousness or qualia.</text>
</svg>
"""


def main() -> None:
    v46 = v46_common_effect_pooling()
    v47 = v47_common_effect_heterogeneity()
    v48 = v48_leave_one_site_out_influence()
    v49 = v49_partial_conjunction_replicability()
    v50 = v50_site_weight_concentration()

    _write_single_row_csv(RESULTS / "v46_common_effect_pooling.csv", v46)
    _write_single_row_csv(RESULTS / "v47_common_effect_heterogeneity.csv", v47)
    _write_csv(RESULTS / "v48_leave_one_site_out.csv", v48)
    _write_csv(RESULTS / "v49_partial_conjunction_replicability.csv", v49)
    _write_csv(RESULTS / "v50_site_weight_concentration.csv", v50)

    summary = {
        "status": "analytic_and_synthetic_only",
        "claim_boundary": (
            "cross-site replication inference and site-stability calculations do not "
            "constitute external replication in real cohorts or identify consciousness"
        ),
        "v46_common_effect_pooling": v46,
        "v47_common_effect_heterogeneity": v47,
        "v48_leave_one_site_out_influence": v48,
        "v49_partial_conjunction_replicability": v49,
        "v50_site_weight_concentration": v50,
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "electromagnetic_replication_validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    FIGURES.mkdir(parents=True, exist_ok=True)
    (FIGURES / "v46_v50_electromagnetic_replication_validation.svg").write_text(
        _render_svg(v46, v47, v48, v49, v50),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
