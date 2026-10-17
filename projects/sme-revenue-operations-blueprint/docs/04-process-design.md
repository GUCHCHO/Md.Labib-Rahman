# 04 — Current-State and Future-State Process

## 1. Current-state hypothesis

The fictional business uses disconnected records and manual handoffs. This map is a discovery hypothesis, not an observed process.

~~~mermaid
flowchart TD
  A[Lead arrives] --> B[Sales logs lead in a spreadsheet or CRM]
  B --> C[Manual qualification and follow-up]
  C --> D[Quotation prepared separately]
  D --> E[Stock checked with operations]
  E --> F{Stock / approval available?}
  F -- No --> G[Manual rework or delayed response]
  F -- Yes --> H[Order created in operations system]
  H --> I[Invoice raised in finance tool]
  I --> J[Receipt checked against bank or payment records]
  J --> K[Management combines reports manually]
~~~

### Candidate pain points to validate
- Missing owner or next action.
- Re-keyed account, product, order or invoice information.
- Stock/price checks after a customer expects confirmation.
- No consistent reason code for lost deals or delayed orders.
- Receipt exceptions identified late.
- KPI calculation differences between spreadsheets.

## 2. Future-state flow

~~~mermaid
flowchart TD
  A[Lead captured] --> B[Deduplicate and assign owner]
  B --> C[Qualify need, fit, value and next action]
  C --> D{Qualified?}
  D -- No --> E[Nurture or close with reason]
  D -- Yes --> F[Discovery and solution / quotation]
  F --> G[Price, discount and availability checks]
  G --> H{Approved and fulfillable?}
  H -- No --> I[Exception queue and owner action]
  I --> G
  H -- Yes --> J[Order confirmation and reservation]
  J --> K[Fulfillment and delivery confirmation]
  K --> L[Invoice issued]
  L --> M[Receipt captured and reconciled]
  M --> N[Closed-loop reporting and follow-up]
~~~

## 3. Process controls

| Control point | Control | Evidence |
|---|---|---|
| Lead intake | Duplicate rule, owner assignment and source capture | Lead audit event |
| Qualification | Required criteria and next action | Stage history |
| Quotation | Price list, discount authority and validity | Versioned quotation and approval |
| Order | Availability status and order reference | Reservation / exception record |
| Fulfillment | Dispatch / delivery evidence | Delivery reference and status |
| Invoice | Unique invoice number and account mapping | Posted invoice reference |
| Payment | Source reference and matching rule | Reconciliation record |
| Reporting | Approved formula, time window and refresh timestamp | KPI definition and refresh log |

## 4. Exceptions and recovery paths

- **Duplicate lead:** preserve the source record, link it to the canonical account and keep an audit trail.
- **No stock:** offer backorder or an approved alternative; do not show a confirmed delivery promise without evidence.
- **Discount override:** route to the designated approver and record the decision.
- **Integration unavailable:** retain the event safely, show processing status, retry idempotently, and alert after threshold.
- **Unmatched payment:** place in finance exception queue; do not silently allocate it.
- **Incorrect invoice / return:** use a controlled correction, credit-note or reversal process rather than destructive edits.
- **Data mismatch:** identify a system-of-record owner and reconcile before overwriting authoritative data.

## 5. Process measures

- Lead-to-first-response time.
- Percentage of qualified opportunities with a future-dated next action.
- Stage aging and conversion.
- Quote-to-order conversion and time.
- Order exception rate.
- Perfect-order / on-time delivery measure, if source data supports it.
- Invoice-to-receipt matching rate.
- Receivables aging and overdue amount.
- Manual touchpoints per transaction.

## 6. Design principle

Automate repeatable, agreed processes only after ownership and exception handling are clear. Automating an undefined process usually makes errors faster, not outcomes better.
