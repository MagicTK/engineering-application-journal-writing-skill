#!/usr/bin/env python3
"""Render the bundled fictional fixture, not a general experiment evaluator."""

import argparse
import csv
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
from statistics import mean, stdev


METRICS = ("accuracy", "macro_f1", "weighted_f1")


def divide(numerator, denominator):
    return Fraction(numerator, denominator) if denominator else Fraction(0)


def metrics(matrix):
    n = len(matrix)
    if not n or any(len(row) != n for row in matrix):
        raise ValueError("A confusion matrix must be nonempty and square.")
    if any(type(x) is not int or x < 0 for row in matrix for x in row):
        raise ValueError("Counts must be nonnegative integers, not percentages.")
    support = [sum(row) for row in matrix]
    total = sum(support)
    if total == 0:
        raise ValueError("An empty outcome table is not a zero-scoring run.")
    class_f1 = []
    for i in range(n):
        tp = matrix[i][i]
        fp = sum(row[i] for row in matrix) - tp
        fn = support[i] - tp
        class_f1.append(divide(2 * tp, 2 * tp + fp + fn))
    return {
        "accuracy": divide(sum(matrix[i][i] for i in range(n)), total),
        "macro_f1": sum(class_f1) / n,
        "weighted_f1": sum(v * s for v, s in zip(class_f1, support)) / total,
    }


def summarize(fixture):
    if fixture.get("fictional") is not True or fixture.get("zero_division") != 0:
        raise ValueError("This demo requires a fictional fixture with zero_division=0.")
    if (fixture.get("matrix_rows") != "reference classes"
            or fixture.get("matrix_columns") != "predicted classes"):
        raise ValueError("Declare reference rows and prediction columns.")
    labels, support = fixture["class_labels"], fixture["class_support"]
    if (len(labels) != len(set(labels)) or len(labels) != len(support)
            or any(type(v) is not int or v <= 0 for v in support)
            or sum(support) != fixture["unique_test_examples"]):
        raise ValueError("Class labels, supports and declared sample count disagree.")
    methods = fixture["methods"]
    n = fixture["expected_repetitions_per_method"]
    if not methods or len(methods) != len(set(methods)) or type(n) is not int or n < 2:
        raise ValueError("Declare unique methods and at least two constructed tables.")
    runs = fixture["runs"]
    if len({r["run_id"] for r in runs}) != len(runs):
        raise ValueError("Duplicate outcome-table ID.")
    if set(r["method"] for r in runs) != set(methods):
        raise ValueError("Observed methods differ from the fixture manifest.")
    result = {}
    for method in methods:
        selected = [r for r in runs if r["method"] == method]
        if (len(selected) != n
                or any(type(r["repetition"]) is not int for r in selected)
                or {r["repetition"] for r in selected} != set(range(1, n + 1))):
            raise ValueError("Missing or duplicated constructed table for " + method)
        selected.sort(key=lambda r: r["repetition"])
        values = []
        for run in selected:
            value = metrics(run["matrix"])
            if [sum(row) for row in run["matrix"]] != support:
                raise ValueError("Class supports disagree with the fixture manifest.")
            values.append(value)
        result[method] = {
            "outcome_table_ids": [r["run_id"] for r in selected],
            "table_metrics": [{k: float(v[k]) for k in METRICS} for v in values],
            "summary": {
                k: {"mean": float(mean(v[k] for v in values)),
                    "sample_sd": stdev(float(v[k]) for v in values)}
                for k in METRICS
            },
        }
    return result


def markdown_table(result):
    lines = [
        "Fictional teaching example: mean +/- sample SD (ddof=1).",
        "Scores are percentages; SD is in percentage points.", "",
        "| Fictional method | Accuracy (%) | Macro-F1 (%) | Weighted-F1 (%) |",
        "|---|---:|---:|---:|",
    ]
    for name, value in result.items():
        cells = ["{:.2f} +/- {:.2f}".format(
            100 * value["summary"][k]["mean"],
            100 * value["summary"][k]["sample_sd"]) for k in METRICS]
        lines.append("| " + name + " | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def draw(result, destination, plt):
    with plt.rc_context({"font.family": "DejaVu Sans", "font.size": 11}):
        fig, ax = plt.subplots(figsize=(6.2, 4.4))
        fig.subplots_adjust(left=0.14, right=0.96, bottom=0.25, top=0.80)
        colors, markers = ("#007A70", "#AC385F"), ("o", "s")
        for i, (name, value) in enumerate(result.items()):
            color, marker = colors[i % 2], markers[i % 2]
            scores = [100 * v["macro_f1"] for v in value["table_metrics"]]
            # Horizontal offsets separate marks, not time points or paired seeds.
            xs = [i - 0.16 + 0.08 * j / max(1, len(scores) - 1)
                  for j in range(len(scores))]
            ax.scatter(xs, scores, s=36, facecolors="white", edgecolors=color,
                       marker=marker, linewidths=1.2, zorder=3)
            summary = value["summary"]["macro_f1"]
            ax.errorbar(i + 0.10, 100 * summary["mean"],
                        yerr=100 * summary["sample_sd"], fmt=marker, color=color,
                        markersize=7, capsize=5, linewidth=1.5, zorder=4)
        ax.set_xlim(-0.45, len(result) - 0.55)
        ax.set_ylim(75, 90)
        ax.set_yticks([75, 80, 85, 90])
        ax.set_xticks(list(range(len(result))))
        ax.set_xticklabels(list(result))
        ax.set_ylabel("Macro-F1 (%)")
        ax.grid(axis="y", color="#dddddd", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        fig.suptitle("Fictional teaching example", fontsize=14, y=0.95)
        fig.text(0.5, 0.87, "Constructed outcome tables, not training runs",
                 ha="center", fontsize=10)
        fig.text(0.5, 0.11, "Open marks: individual tables    Filled marks: mean",
                 ha="center", fontsize=10)
        fig.text(0.5, 0.06, "Error bars: one sample SD (ddof=1); three tables per method",
                 ha="center", fontsize=9)
        fig.savefig(destination, dpi=180, facecolor="white")
        plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True,
                        help="New output directory; existing paths are never overwritten")
    args = parser.parse_args()
    target = args.output.expanduser()
    if target.exists() or target.is_symlink():
        parser.error("Output path already exists; choose a new directory.")
    source = Path(__file__).with_name("fixture.json")
    fixture = json.loads(source.read_text(encoding="utf-8"))
    result = summarize(fixture)
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        parser.error("Plotting needs matplotlib; see this example's README. Nothing written.")
    target.mkdir(parents=True, exist_ok=False)
    (target / "table.md").write_text(markdown_table(result), encoding="utf-8")
    with (target / "summary.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["fictional_method", "metric", "mean", "sample_sd", "scale"])
        for name, value in result.items():
            for metric in METRICS:
                row = value["summary"][metric]
                writer.writerow([name, metric, row["mean"], row["sample_sd"], "0-1"])
    draw(result, target / "macro-f1.png", plt)
    record = {
        "fictional": True, "purpose": fixture["purpose"],
        "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "builder_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(), "matplotlib": matplotlib.__version__,
        "unique_test_examples_stipulated": fixture["unique_test_examples"],
        "repetition_unit": fixture["repetition_unit"], "sd_ddof": 1,
        "metric_scale": "0-1; table and figure display percentages",
        "methods": result,
        "artifacts_sha256": {
            name: hashlib.sha256((target / name).read_bytes()).hexdigest()
            for name in ("table.md", "summary.csv", "macro-f1.png")
        },
    }
    (target / "evidence.json").write_text(json.dumps(record, indent=2) + "\n",
                                        encoding="utf-8")
    print("Built fictional teaching artifacts: " + str(target))


if __name__ == "__main__":
    main()
