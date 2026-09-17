"""Run Research III formal validation stages V11-V15.

The outputs are analytic and synthetic measurement-design validation records.
They are not human empirical consciousness measurements.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from consciousness_measurement.identification_design_simulations import (
    independent_pilot_gate_experiment,
    missingness_information_design_grid,
    multisite_heterogeneity_design_grid,
    resolution_sample_size_design_grid,
)

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "docs" / "figures"
SEED = 20260919


def write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def svg_line_plot(
    path: Path,
    *,
    title: str,
    subtitle: str,
    x_values: list[float],
    series: list[tuple[str, list[float], str]],
    x_label: str,
    y_label: str,
    y_min: float,
    y_max: float,
    x_log: bool = False,
) -> None:
    import math

    left, right, top, bottom = 110, 55, 105, 105
    width, height = 1200 - left - right, 720 - top - bottom
    tx = [math.log10(x) if x_log else x for x in x_values]
    xmin, xmax = min(tx), max(tx)

    def sx(value: float) -> float:
        transformed = math.log10(value) if x_log else value
        return left + (transformed - xmin) / (xmax - xmin) * width

    def sy(value: float) -> float:
        return top + (y_max - value) / (y_max - y_min) * height

    palette = ("#0f5f78", "#9a4e0d", "#6b4fa3", "#3f6f45")
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720" role="img">',
        f"<title>{title}</title>",
        f"<desc>{subtitle}</desc>",
        '<rect width="1200" height="720" fill="#fff"/>',
        f'<text x="{left}" y="42" font-family="Arial" font-size="24" font-weight="700" fill="#0f172a">{title}</text>',
        f'<text x="{left}" y="68" font-family="Arial" font-size="14" fill="#475569">{subtitle}</text>',
        f'<rect x="{left}" y="{top}" width="{width}" height="{height}" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>',
    ]
    for index in range(6):
        y = y_min + index * (y_max - y_min) / 5
        py = sy(y)
        out.append(f'<line x1="{left}" y1="{py:.1f}" x2="{left+width}" y2="{py:.1f}" stroke="#e2e8f0"/>')
        out.append(f'<text x="{left-14}" y="{py+4:.1f}" text-anchor="end" font-family="Arial" font-size="13" fill="#475569">{y:.3g}</text>')
    for value in x_values:
        px = sx(value)
        out.append(f'<line x1="{px:.1f}" y1="{top}" x2="{px:.1f}" y2="{top+height}" stroke="#e2e8f0"/>')
        label = f"{value:g}"
        out.append(f'<text x="{px:.1f}" y="{top+height+27}" text-anchor="middle" font-family="Arial" font-size="13" fill="#475569">{label}</text>')
    out.append(f'<line x1="{left}" y1="{top+height}" x2="{left+width}" y2="{top+height}" stroke="#334155" stroke-width="1.4"/>')
    out.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+height}" stroke="#334155" stroke-width="1.4"/>')
    out.append(f'<text x="{left+width/2}" y="690" text-anchor="middle" font-family="Arial" font-size="15" font-weight="600" fill="#1e293b">{x_label}</text>')
    out.append(f'<text transform="translate(31 {top+height/2}) rotate(-90)" text-anchor="middle" font-family="Arial" font-size="15" font-weight="600" fill="#1e293b">{y_label}</text>')
    for index, (name, values, marker) in enumerate(series):
        color = palette[index % len(palette)]
        points = [(sx(x), sy(y)) for x, y in zip(x_values, values, strict=True)]
        coords = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        out.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="3"/>')
        for x, y in points:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="{color}"/>')
        ly = 91 + index * 22
        out.append(f'<line x1="650" y1="{ly}" x2="682" y2="{ly}" stroke="{color}" stroke-width="3"/>')
        out.append(f'<text x="692" y="{ly+4}" font-family="Arial" font-size="13" fill="#475569">{name}</text>')
        _ = marker
    out.append("</svg>")
    path.write_text("\n".join(out), encoding="utf-8")


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    missingness = missingness_information_design_grid(
        missing_fractions=(0.0, 0.05, 0.10, 0.15, 0.20),
        youden_values=(0.30, 0.50, 0.75, 0.90),
    )
    multisite = multisite_heterogeneity_design_grid(
        spreads=(0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30),
    )
    resolution = resolution_sample_size_design_grid(
        youden_values=(0.30, 0.50, 0.75, 0.90),
        maximum_widths=(0.25, 0.20, 0.15, 0.10, 0.075),
        delta=0.05,
    )

    pilot_rows: list[dict[str, float]] = []
    for planned_n in (600, 800, 900, 1000, 1200, 1600):
        result = independent_pilot_gate_experiment(
            prevalence=0.40,
            sensitivity=0.84,
            specificity=0.91,
            pilot_calibration_n_per_class=120,
            confirm_deployment_n=planned_n,
            confirm_calibration_n_per_class=2500,
            maximum_width=0.12,
            repetitions=1600,
            delta=0.05,
            seed=SEED + planned_n,
        )
        pilot_rows.append({"planned_confirmatory_n": float(planned_n), **result})

    write_csv(RESULTS / "v11_missingness_information_law.csv", missingness)
    write_csv(RESULTS / "v12_v13_multisite_identification.csv", multisite)
    write_csv(RESULTS / "v14_resolution_sample_size.csv", resolution)
    write_csv(RESULTS / "v15_independent_pilot_gate.csv", pilot_rows)

    summary = {
        "status": "analytic_and_synthetic_validation_only",
        "seed": SEED,
        "v11": {
            "width_10_percent_missing_youden_0_75": next(
                row["interior_latent_width"]
                for row in missingness
                if row["missing_fraction"] == 0.10 and row["youden"] == 0.75
            )
        },
        "v12_v13": {
            "equal_information_width": multisite[0]["identified_width"],
            "width_at_spread_0_30": multisite[-1]["identified_width"],
        },
        "v14": {
            "required_n_youden_0_75_width_0_10": next(
                row["required_n"]
                for row in resolution
                if row["youden"] == 0.75 and row["maximum_width"] == 0.10
            )
        },
        "v15": {
            "release_rate_n900": next(
                row["release_rate"]
                for row in pilot_rows
                if row["planned_confirmatory_n"] == 900.0
            ),
            "minimum_conditional_coverage": min(
                row["conditional_coverage_given_release_and_identification"]
                for row in pilot_rows
                if row["identified_confirmatory_runs"] > 0.0
            ),
        },
    }
    (RESULTS / "identification_design_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    by_j: dict[float, list[dict[str, float]]] = {}
    for row in missingness:
        by_j.setdefault(row["youden"], []).append(row)
    x_missing = [row["missing_fraction"] for row in by_j[0.75]]
    svg_line_plot(
        FIGURES / "v11_missingness_information_law.svg",
        title="Missingness loss is amplified by the inverse information margin",
        subtitle="Exact interior identified-set width equals missing fraction divided by the Youden information margin.",
        x_values=x_missing,
        series=[
            (f"J = {j:g}", [row["interior_latent_width"] for row in by_j[j]], "circle")
            for j in (0.30, 0.50, 0.75, 0.90)
        ],
        x_label="fraction of outcomes missing",
        y_label="exact interior latent identified-set width",
        y_min=0.0,
        y_max=0.70,
    )

    svg_line_plot(
        FIGURES / "v12_v13_multisite_heterogeneity.svg",
        title="Unequal site information margins create partial identification",
        subtitle="The population-average latent prevalence is point-identified at equal site slopes and becomes set-identified as slope heterogeneity grows.",
        x_values=[row["youden_spread"] for row in multisite],
        series=[
            ("sharp identified-set width", [row["identified_width"] for row in multisite], "circle")
        ],
        x_label="site Youden-margin spread",
        y_label="sharp average-prevalence identified-set width",
        y_min=0.0,
        y_max=0.36,
    )

    rows_width_010 = [row for row in resolution if row["maximum_width"] == 0.10]
    svg_line_plot(
        FIGURES / "v14_resolution_sample_size.svg",
        title="Target resolution has a quadratic sample-size cost",
        subtitle="Sufficient deployment sample size for a 95% Hoeffding interval with latent width at most 0.10.",
        x_values=[row["youden"] for row in rows_width_010],
        series=[("required deployment n", [row["required_n"] for row in rows_width_010], "circle")],
        x_label="Youden information margin J",
        y_label="sufficient deployment sample size",
        y_min=0.0,
        y_max=8500.0,
    )

    svg_line_plot(
        FIGURES / "v15_independent_pilot_gate.svg",
        title="Independent pilot gating preserves confirmatory validity",
        subtitle="Pilot data decide whether to proceed; an independent confirmatory interval retains its coverage among released designs.",
        x_values=[row["planned_confirmatory_n"] for row in pilot_rows],
        series=[
            ("release rate", [row["release_rate"] for row in pilot_rows], "circle"),
            (
                "conditional coverage",
                [
                    row["conditional_coverage_given_release_and_identification"]
                    if row["identified_confirmatory_runs"] > 0.0
                    else 0.0
                    for row in pilot_rows
                ],
                "circle",
            ),
        ],
        x_label="planned confirmatory deployment sample size",
        y_label="fraction",
        y_min=0.0,
        y_max=1.02,
    )

    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
