#!/usr/bin/env python3
"""Analyze a synthetic sales pipeline CSV using only the Python standard library.

This is a portfolio demonstration, not a production forecasting engine.
All values are illustrative and should be validated before business use.
"""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, List


CLOSED_STAGES = {"Closed Won", "Closed Lost"}
REQUIRED_COLUMNS = {
    "opportunity_id", "segment", "source", "stage",
    "deal_value_bdt", "probability_pct", "days_in_stage",
}


def load_rows(path: Path) -> List[dict]:
    with path.open("r", newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None:
            raise ValueError("CSV is empty or has no header.")
        missing = REQUIRED_COLUMNS.difference(reader.fieldnames)
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

        rows = []
        for line_number, row in enumerate(reader, start=2):
            try:
                value = Decimal(row["deal_value_bdt"])
                probability = Decimal(row["probability_pct"])
                days = int(row["days_in_stage"])
            except (InvalidOperation, TypeError, ValueError) as exc:
                raise ValueError(f"Invalid numeric value on CSV line {line_number}.") from exc

            if value < 0:
                raise ValueError(f"deal_value_bdt cannot be negative on line {line_number}.")
            if probability < 0 or probability > 100:
                raise ValueError(f"probability_pct must be between 0 and 100 on line {line_number}.")
            if days < 0:
                raise ValueError(f"days_in_stage cannot be negative on line {line_number}.")
            if not row["opportunity_id"].strip() or not row["stage"].strip():
                raise ValueError(f"opportunity_id and stage are required on line {line_number}.")

            rows.append({
                **row,
                "deal_value": value,
                "probability": probability,
                "days": days,
            })
    return rows


def bdt(value: Decimal) -> str:
    return f"BDT {value:,.2f}"


def analyze(rows: List[dict]) -> Dict[str, object]:
    closed = [row for row in rows if row["stage"] in CLOSED_STAGES]
    won = [row for row in rows if row["stage"] == "Closed Won"]
    lost = [row for row in rows if row["stage"] == "Closed Lost"]
    open_rows = [row for row in rows if row["stage"] not in CLOSED_STAGES]

    total_won = sum((row["deal_value"] for row in won), Decimal("0"))
    open_value = sum((row["deal_value"] for row in open_rows), Decimal("0"))
    weighted = sum(
        (row["deal_value"] * row["probability"] / Decimal("100") for row in open_rows),
        Decimal("0"),
    )
    win_rate = (
        Decimal(len(won)) * Decimal("100") / Decimal(len(closed))
        if closed else Decimal("0")
    )

    stage_summary = defaultdict(lambda: {
        "count": 0, "open_value": Decimal("0"), "weighted": Decimal("0")
    })
    source_summary = defaultdict(lambda: {
        "count": 0, "open_value": Decimal("0"), "weighted": Decimal("0")
    })

    for row in open_rows:
        for summary, key in (
            (stage_summary, row["stage"]),
            (source_summary, row["source"]),
        ):
            summary[key]["count"] += 1
            summary[key]["open_value"] += row["deal_value"]
            summary[key]["weighted"] += (
                row["deal_value"] * row["probability"] / Decimal("100")
            )

    return {
        "rows": len(rows),
        "closed_count": len(closed),
        "won_count": len(won),
        "lost_count": len(lost),
        "win_rate": win_rate,
        "won_value": total_won,
        "open_value": open_value,
        "weighted": weighted,
        "stages": stage_summary,
        "sources": source_summary,
    }


def print_summary(summary: Dict[str, object]) -> None:
    print("SYNTHETIC REVENUE OPERATIONS SNAPSHOT")
    print("=" * 42)
    print(f"Opportunities:              {summary['rows']}")
    print(f"Closed opportunities:       {summary['closed_count']}")
    print(f"Closed won / lost:          {summary['won_count']} / {summary['lost_count']}")
    print(f"Win rate among closed:      {summary['win_rate']:.2f}%")
    print(f"Sample closed-won bookings: {bdt(summary['won_value'])}")
    print(f"Open pipeline value:        {bdt(summary['open_value'])}")
    print(f"Probability-weighted open:  {bdt(summary['weighted'])}")
    print("\nOPEN PIPELINE BY STAGE")
    for stage, metrics in sorted(
        summary["stages"].items(),
        key=lambda item: item[1]["weighted"],
        reverse=True,
    ):
        print(
            f"- {stage}: {metrics['count']} opps | "
            f"{bdt(metrics['open_value'])} open | "
            f"{bdt(metrics['weighted'])} weighted"
        )
    print("\nOPEN PIPELINE BY SOURCE")
    for source, metrics in sorted(
        summary["sources"].items(),
        key=lambda item: item[1]["weighted"],
        reverse=True,
    ):
        print(
            f"- {source}: {metrics['count']} opps | "
            f"{bdt(metrics['open_value'])} open | "
            f"{bdt(metrics['weighted'])} weighted"
        )
    print("\nNote: pipeline expectation is not booked revenue, invoiced revenue, or collected cash.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).with_name("sample_pipeline.csv"),
        help="Path to a CSV with the documented schema.",
    )
    args = parser.parse_args()

    try:
        rows = load_rows(args.input)
        if not rows:
            raise ValueError("No opportunity rows found.")
        print_summary(analyze(rows))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
