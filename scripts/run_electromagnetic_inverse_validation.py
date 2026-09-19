from __future__ import annotations

import csv
import json
from pathlib import Path

from consciousness_measurement.electromagnetic_inverse_simulations import (
    v21_reference_invariance_grid,
    v22_lead_field_nonidentifiability,
    v23_regularization_path,
    v24_multimodal_nullity,
    v25_forward_model_perturbation_grid,
)
from consciousness_measurement.figure_svg import (
    circle as svg_circle,
    line as svg_line,
    metric_card,
    polyline as svg_polyline,
    rect as svg_rect,
    text as svg_text,
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
    v21: list[dict[str, float]],
    v22: dict[str, float],
    v23: list[dict[str, float]],
    v24: list[dict[str, float]],
    v25: list[dict[str, float]],
) -> str:
    width, height = 1400, 900
    v24_map = {int(row["modality_code"]): row for row in v24}
    max_reference_error = max(row["max_pairwise_difference_error"] for row in v21)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        svg_rect(0, 0, width, height, fill="#ffffff", stroke="none", stroke_width=0),
        svg_text(60, 56, "Research III V21-V25", size=13, weight=700, fill="#3156a3"),
        svg_text(
            60,
            92,
            "Electromagnetic forward and inverse limits",
            size=31,
            weight=700,
            fill="#172236",
        ),
        svg_text(
            60,
            120,
            "Reference invariance, source ambiguity, regularization sensitivity, multimodal complementarity, and forward-model error.",
            size=15,
            fill="#657286",
        ),
        svg_line(60, 145, 1340, 145, stroke="#d6dde7", width=1.2),
        metric_card(
            60,
            172,
            400,
            150,
            kicker="V21",
            title="Reference invariance",
            value=f"{max_reference_error:.2e}",
            note="max pairwise-difference error",
            accent="#315b78",
        ),
        metric_card(
            500,
            172,
            400,
            150,
            kicker="V22",
            title="Source non-identifiability",
            value=f'rank {int(v22["rank"])} / nullity {int(v22["nullity"])}',
            note=f'zero sensor residual; source separation {_fmt(v22["source_separation"])}',
            accent="#51683f",
        ),
        metric_card(
            940,
            172,
            400,
            150,
            kicker="V24",
            title="Multimodal complementarity",
            value=f'nullity {int(v24_map[1]["nullity"])} + {int(v24_map[2]["nullity"])} to {int(v24_map[3]["nullity"])}',
            note="ambiguity reduced, not eliminated",
            accent="#7a425c",
        ),
    ]

    plot_y = 365
    panel_height = 430

    # V23: regularization sensitivity
    x0, panel_width = 60, 610
    parts.extend(
        [
            svg_rect(
                x0,
                plot_y,
                panel_width,
                panel_height,
                fill="#fbfcfe",
                stroke="#d6dde7",
                stroke_width=1.2,
                radius=12,
            ),
            svg_text(
                x0 + 26,
                plot_y + 36,
                "V23  Regularization sensitivity",
                size=18,
                weight=700,
                fill="#244c64",
            ),
            svg_text(
                x0 + 26,
                plot_y + 61,
                "Sensor residual rises as the inverse prior is strengthened",
                size=13,
                fill="#687588",
            ),
        ]
    )
    ax_left, ax_right = x0 + 78, x0 + panel_width - 28
    ax_top, ax_bottom = plot_y + 96, plot_y + 335
    y_min, y_max = 0.0, 0.55
    for value in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5):
        y = ax_bottom - (value - y_min) / (y_max - y_min) * (ax_bottom - ax_top)
        parts.append(svg_line(ax_left, y, ax_right, y, stroke="#e3e8ef"))
        parts.append(
            svg_text(
                ax_left - 12,
                y + 5,
                f"{value:.1f}",
                size=11,
                fill="#657286",
                anchor="end",
            )
        )
    parts.extend(
        [
            svg_line(ax_left, ax_top, ax_left, ax_bottom, stroke="#8f9cad", width=1.4),
            svg_line(ax_left, ax_bottom, ax_right, ax_bottom, stroke="#8f9cad", width=1.4),
        ]
    )
    x_values = [
        ax_left + i * (ax_right - ax_left) / (len(v23) - 1)
        for i in range(len(v23))
    ]
    points = [
        (
            x,
            ax_bottom
            - (row["measurement_residual"] - y_min)
            / (y_max - y_min)
            * (ax_bottom - ax_top),
        )
        for x, row in zip(x_values, v23, strict=True)
    ]
    parts.append(svg_polyline(points, stroke="#1f6078", width=4))
    for x, y in points:
        parts.append(svg_circle(x, y, 5.5, fill="#1f6078"))
    for x, label in zip(x_values, ("1e-6", "1e-4", "1e-2", "0.1", "1"), strict=True):
        parts.append(
            svg_text(x, ax_bottom + 24, label, size=11, fill="#657286", anchor="middle")
        )
    parts.extend(
        [
            svg_text(
                (ax_left + ax_right) / 2,
                ax_bottom + 52,
                "regularization",
                size=12,
                weight=600,
                fill="#4f5e72",
                anchor="middle",
            ),
            svg_text(
                x0 + 26,
                plot_y + 397,
                "Result: stronger regularization trades fit for stronger prior influence.",
                size=12,
                weight=600,
                fill="#4f5e72",
            ),
        ]
    )

    # V25: forward-model perturbation
    x0, panel_width = 730, 610
    parts.extend(
        [
            svg_rect(
                x0,
                plot_y,
                panel_width,
                panel_height,
                fill="#fbfcfe",
                stroke="#d6dde7",
                stroke_width=1.2,
                radius=12,
            ),
            svg_text(
                x0 + 26,
                plot_y + 36,
                "V25  Forward-model perturbation",
                size=18,
                weight=700,
                fill="#415f46",
            ),
            svg_text(
                x0 + 26,
                plot_y + 61,
                "Observed mismatch remains below the declared perturbation bound",
                size=13,
                fill="#687588",
            ),
        ]
    )
    ax_left, ax_right = x0 + 78, x0 + panel_width - 28
    ax_top, ax_bottom = plot_y + 96, plot_y + 335
    y_min, y_max = 0.0, 0.16
    for value in (0.0, 0.04, 0.08, 0.12, 0.16):
        y = ax_bottom - (value - y_min) / (y_max - y_min) * (ax_bottom - ax_top)
        parts.append(svg_line(ax_left, y, ax_right, y, stroke="#e3e8ef"))
        parts.append(
            svg_text(
                ax_left - 12,
                y + 5,
                f"{value:.2f}",
                size=11,
                fill="#657286",
                anchor="end",
            )
        )
    parts.extend(
        [
            svg_line(ax_left, ax_top, ax_left, ax_bottom, stroke="#8f9cad", width=1.4),
            svg_line(ax_left, ax_bottom, ax_right, ax_bottom, stroke="#8f9cad", width=1.4),
        ]
    )
    x_values = [
        ax_left + i * (ax_right - ax_left) / (len(v25) - 1)
        for i in range(len(v25))
    ]
    mismatch_points = []
    bound_points = []
    for x, row in zip(x_values, v25, strict=True):
        mismatch_points.append(
            (
                x,
                ax_bottom
                - (row["sensor_mismatch"] - y_min)
                / (y_max - y_min)
                * (ax_bottom - ax_top),
            )
        )
        bound_points.append(
            (
                x,
                ax_bottom
                - (row["upper_bound"] - y_min)
                / (y_max - y_min)
                * (ax_bottom - ax_top),
            )
        )
    parts.extend(
        [
            svg_polyline(bound_points, stroke="#9aa7b5", width=3, dash="7 5"),
            svg_polyline(mismatch_points, stroke="#456848", width=4),
        ]
    )
    for x, y in mismatch_points:
        parts.append(svg_circle(x, y, 5.2, fill="#456848"))
    for x, label in zip(
        x_values,
        ("0", "0.001", "0.01", "0.05", "0.1"),
        strict=True,
    ):
        parts.append(
            svg_text(x, ax_bottom + 24, label, size=11, fill="#657286", anchor="middle")
        )
    parts.extend(
        [
            svg_text(
                (ax_left + ax_right) / 2,
                ax_bottom + 52,
                "perturbation operator norm",
                size=12,
                weight=600,
                fill="#4f5e72",
                anchor="middle",
            ),
            svg_line(x0 + 326, plot_y + 390, x0 + 350, plot_y + 390, stroke="#456848", width=4),
            svg_text(x0 + 360, plot_y + 395, "sensor mismatch", size=11, weight=600, fill="#4f5e72"),
            svg_line(
                x0 + 465,
                plot_y + 390,
                x0 + 489,
                plot_y + 390,
                stroke="#9aa7b5",
                width=3,
                dash="7 5",
            ),
            svg_text(x0 + 499, plot_y + 395, "upper bound", size=11, weight=600, fill="#4f5e72"),
            svg_line(60, 840, 1340, 840, stroke="#d6dde7"),
            svg_text(
                60,
                868,
                "Deterministic synthetic validation. Forward/inverse checks do not uniquely identify neural sources or consciousness.",
                size=12,
                fill="#697587",
            ),
            "</svg>",
        ]
    )
    return "\n".join(parts)


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    v21 = v21_reference_invariance_grid()
    v22 = v22_lead_field_nonidentifiability()
    v23 = v23_regularization_path()
    v24 = v24_multimodal_nullity()
    v25 = v25_forward_model_perturbation_grid()

    _write_csv(RESULTS / "v21_reference_invariance.csv", v21)
    _write_csv(RESULTS / "v23_regularization_path.csv", v23)
    _write_csv(RESULTS / "v24_multimodal_nullity.csv", v24)
    _write_csv(RESULTS / "v25_forward_model_perturbation.csv", v25)
    (RESULTS / "electromagnetic_inverse_validation_summary.json").write_text(
        json.dumps(
            {
                "status": "analytic_and_synthetic_only",
                "claim_boundary": (
                    "forward and inverse electromagnetic validation does not "
                    "identify consciousness or uniquely identify neural sources"
                ),
                "v22_lead_field_nonidentifiability": v22,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    (FIGURES / "v21_v25_electromagnetic_inverse_validation.svg").write_text(
        _svg(v21=v21, v22=v22, v23=v23, v24=v24, v25=v25),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
