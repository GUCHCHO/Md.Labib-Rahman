"""Unit tests for the synthetic revenue pipeline model."""
import csv
import tempfile
import unittest
from pathlib import Path

import revenue_model


ANALYTICS_DIR = Path(__file__).resolve().parent
SAMPLE_CSV = ANALYTICS_DIR / "sample_pipeline.csv"


class RevenueModelTests(unittest.TestCase):
    def test_sample_dataset_totals(self):
        rows = revenue_model.load_rows(SAMPLE_CSV)
        summary = revenue_model.analyze(rows)

        self.assertEqual(summary["rows"], 12)
        self.assertEqual(summary["closed_count"], 3)
        self.assertEqual(summary["won_count"], 2)
        self.assertEqual(summary["lost_count"], 1)
        self.assertEqual(str(summary["win_rate"].quantize(__import__("decimal").Decimal("0.01"))), "66.67")
        self.assertEqual(summary["won_value"], __import__("decimal").Decimal("1640000"))
        self.assertEqual(summary["open_value"], __import__("decimal").Decimal("8460000"))
        self.assertEqual(summary["weighted"], __import__("decimal").Decimal("3964000"))

    def test_invalid_probability_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad.csv"
            path.write_text(
                "opportunity_id,segment,source,stage,deal_value_bdt,probability_pct,days_in_stage\n"
                "OPP-X,Retail,Inbound,Qualified,1000,120,2\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "between 0 and 100"):
                revenue_model.load_rows(path)

    def test_negative_value_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad.csv"
            path.write_text(
                "opportunity_id,segment,source,stage,deal_value_bdt,probability_pct,days_in_stage\n"
                "OPP-X,Retail,Inbound,Qualified,-100,20,2\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "cannot be negative"):
                revenue_model.load_rows(path)

    def test_empty_closed_cohort_has_zero_win_rate(self):
        rows = revenue_model.load_rows(SAMPLE_CSV)
        open_rows = [row for row in rows if row["stage"] not in revenue_model.CLOSED_STAGES]
        summary = revenue_model.analyze(open_rows)
        self.assertEqual(summary["win_rate"], __import__("decimal").Decimal("0"))


if __name__ == "__main__":
    unittest.main()
