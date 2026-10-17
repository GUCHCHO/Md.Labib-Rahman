# Synthetic Pipeline Data Dictionary

| Column | Type | Definition | Validation |
|---|---|---|---|
| opportunity_id | String | Stable synthetic opportunity key | Required and unique in the sample |
| segment | String | Illustrative customer / business segment | Controlled value for the sample |
| source | String | Lead acquisition source | Controlled value for the sample |
| stage | String | Current opportunity stage | Must match a documented stage |
| deal_value_bdt | Decimal-like integer | Illustrative opportunity amount, BDT | Non-negative |
| probability_pct | Integer | Illustrative stage / opportunity probability | 0–100 |
| days_in_stage | Integer | Synthetic age in current stage | Non-negative |
| owner | String | Neutral sales owner identifier | No real employee identity |
| next_action_date | ISO date | Illustrative follow-up date | Date format YYYY-MM-DD |

## Definitions and limits
- Every row is synthetic, and IDs do not identify real customers or deals.
- Opportunity amount is not recognized revenue, margin, an invoice balance or cash receipt.
- Probability values are teaching inputs, not calibrated model outputs.
- Stage history, creation date, close date, cancellations, partial wins and cohort definitions are not represented in this small sample.
- The dataset is suitable for a portfolio demonstration only, not for business forecasting.
