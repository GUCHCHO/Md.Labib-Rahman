# 07 — Revenue KPI Model and Scenario Analysis

## 1. Purpose

Turn pipeline data into consistent, decision-useful measures. A dashboard should distinguish pipeline expectation, booked business, billed revenue and collected cash. These are different concepts and must not be added together as if they were the same measure.

All records in this project are synthetic. The model is for demonstration and is not a forecast or a claim about Quickly Services, Fronture Technology, or a real client.

## 2. KPI definitions

| KPI | Formula | Decision it supports |
|---|---|---|
| Qualified pipeline value | Sum of open opportunity amounts for qualified stages | Coverage and prioritization |
| Weighted pipeline | Sum of open opportunity amount × current probability | Scenario planning; not guaranteed revenue |
| Win rate | Closed-won opportunities ÷ all closed opportunities | Sales effectiveness by period and segment |
| Stage conversion | Opportunities entering next stage ÷ opportunities entering prior stage, cohort-aligned | Identify friction in funnel |
| Average deal size | Closed-won value ÷ number of won opportunities | Segment and packaging strategy |
| Sales-cycle days | Average days from qualified date to close date for closed opportunities | Forecast and process bottleneck |
| Follow-up compliance | Qualified opportunities with a future-dated next action ÷ qualified open opportunities | Execution discipline |
| Invoice collection rate | Cash allocated to invoices ÷ amount due for same defined cohort and window | Cash collection performance |
| Receivables aging | Outstanding invoice amount grouped by days overdue | Collections prioritization |
| Product adoption | Active weekly users completing the target workflow ÷ enabled users | Training and product-fit feedback |

Each KPI must specify owner, source, refresh timing, filters, treatment of reopened deals, timezone and historical restatement policy.

## 3. Synthetic pipeline scenario

The CSV includes sample accounts represented only by neutral opportunity IDs. The values and probabilities exist solely to exercise the analysis script.

The Python utility calculates:
- total opportunity count and closed count;
- win rate among closed opportunities;
- closed-won bookings in the sample;
- open weighted pipeline value;
- open pipeline amount by stage;
- an explicitly illustrative sensitivity applying user-selected conversion uplift to the open weighted pipeline.

Weighted pipeline uses each open opportunity's probability field. It does not imply accounting revenue recognition or cash collection.

## 4. Revenue growth levers

Use the funnel as a diagnosis framework rather than assuming "more leads" is always the answer.

1. **Lead quality:** compare lead source, segment and qualification rate.
2. **Speed to lead:** measure time from capture to first meaningful response.
3. **Discovery quality:** capture problem, decision process, budget range, urgency and fit.
4. **Proposal effectiveness:** measure proposal-to-negotiation and proposal-to-win conversion.
5. **Offer design:** evaluate packaging, onboarding friction, value proof and pricing sensitivity.
6. **Retention / expansion:** define activation, adoption, renewal and cross-sell metrics.
7. **Delivery capacity:** prevent selling commitments that stock, service or implementation teams cannot fulfill.
8. **Collections:** link billed amounts to verified receipts and age unresolved balances.

## 5. Sensitivity model

For scenario planning, calculate a range instead of reporting a single promised outcome:

- **Conservative case:** no conversion improvement; validate data and follow-up quality first.
- **Base case:** small change in conversion based on tested workflow improvement.
- **Stretch case:** larger improvement only after experiments and cohort evidence support it.

Any sensitivity must state the formula and baseline period, avoid double-counting, and be compared with actual results after implementation. Incremental gross profit is more decision-useful than gross bookings alone; subtract delivery cost, support burden, discounts and acquisition cost where data is available.

## 6. Dashboard layout proposal

- **Executive:** bookings, invoiced revenue, cash collected, margin, open receivables and forecast range.
- **Sales manager:** pipeline coverage, stage aging, next-action compliance, win/loss reasons and source conversion.
- **Operations:** confirmed orders, at-risk orders, stock exceptions, fulfillment cycle time and returns.
- **Finance:** invoice aging, receipts awaiting allocation, reconciliation completion and overdue balances.
- **Product / adoption:** activation, workflow completion, support requests and feature adoption.

## 7. Governance

Every reported metric should carry: metric ID, definition, business owner, data steward, system of record, refresh time, validation rule and known limitation. Report data quality alongside outcome metrics so leaders can tell whether a change reflects performance or a change in data capture.
