-- Portfolio simulation only. Assumes a PostgreSQL-style opportunities table.
-- All sample data is synthetic. Validate definitions with Finance and Sales owners.

-- 1. Open pipeline by stage, including probability-weighted value.
SELECT
    stage,
    COUNT(*) AS opportunity_count,
    SUM(deal_value_bdt) AS open_pipeline_bdt,
    SUM(deal_value_bdt * probability_pct / 100.0) AS weighted_pipeline_bdt,
    AVG(days_in_stage) AS avg_days_in_stage
FROM opportunities
WHERE stage NOT IN ('Closed Won', 'Closed Lost')
GROUP BY stage
ORDER BY weighted_pipeline_bdt DESC;

-- 2. Closed win rate for the selected cohort.
-- Closed opportunities only; open opportunities are excluded.
SELECT
    COUNT(*) FILTER (WHERE stage = 'Closed Won') AS closed_won_count,
    COUNT(*) FILTER (WHERE stage = 'Closed Lost') AS closed_lost_count,
    COUNT(*) FILTER (WHERE stage IN ('Closed Won', 'Closed Lost')) AS closed_count,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE stage = 'Closed Won')
        / NULLIF(COUNT(*) FILTER (WHERE stage IN ('Closed Won', 'Closed Lost')), 0),
        2
    ) AS win_rate_pct
FROM opportunities;

-- 3. Pipeline quality by acquisition source.
SELECT
    source,
    COUNT(*) AS opportunity_count,
    SUM(deal_value_bdt) FILTER (
        WHERE stage NOT IN ('Closed Won', 'Closed Lost')
    ) AS open_pipeline_bdt,
    AVG(probability_pct) FILTER (
        WHERE stage NOT IN ('Closed Won', 'Closed Lost')
    ) AS avg_open_probability_pct,
    COUNT(*) FILTER (WHERE stage = 'Closed Won') AS won_count,
    COUNT(*) FILTER (WHERE stage = 'Closed Lost') AS lost_count
FROM opportunities
GROUP BY source
ORDER BY open_pipeline_bdt DESC NULLS LAST;

-- 4. Follow-up hygiene for active qualified-or-later opportunities.
-- Apply the reporting date / timezone agreed by the business.
SELECT
    COUNT(*) AS active_qualified_count,
    COUNT(*) FILTER (
        WHERE next_action_date IS NOT NULL
          AND next_action_date >= CURRENT_DATE
    ) AS with_future_action,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE next_action_date IS NOT NULL
              AND next_action_date >= CURRENT_DATE
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS follow_up_compliance_pct
FROM opportunities
WHERE stage IN ('Qualified', 'Discovery', 'Proposal', 'Negotiation');

-- Important: pipeline values are not equivalent to booked revenue, invoices or cash.
-- Define calendar windows, ownership, stage history and restatement rules before production use.
