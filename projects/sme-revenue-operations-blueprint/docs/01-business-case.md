# 01 — Business Case and Scope

## 1. Executive summary

This case study considers a fictional Bangladeshi SME that has grown from one sales team into a multi-branch business. Sales, inventory, finance and management currently rely on partially disconnected tools and spreadsheet handoffs. Leadership cannot consistently answer: Which opportunities are likely to convert? Can stock fulfill the order? Which invoices remain unpaid? Which channels and products contribute margin?

The proposed initiative is a phased revenue-operations platform and operating model that connects customer engagement to order fulfillment and cash collection. It combines process standardization, role clarity, integrations, KPI governance and an incremental software roadmap.

> **Portfolio note:** The organization, baseline, targets and financial examples are fictional and illustrative. They must not be represented as client results.

## 2. Problem statement

- Opportunity and follow-up records are inconsistent across teams.
- Quotations, availability checks and order confirmation can involve rekeying.
- Operations may discover stock or delivery constraints late in the sales process.
- Invoices, payments and receivables are not always reconciled into one management view.
- KPI definitions differ between departments, reducing confidence in reports.
- Adding new branches or product lines increases coordination overhead.

## 3. Business objectives

| ID | Objective | How success will be evaluated |
|---|---|---|
| BO-01 | Improve sales follow-up discipline | Percentage of qualified opportunities with a dated next action |
| BO-02 | Increase visibility of conversion | Stage conversion, win rate and sales-cycle trend |
| BO-03 | Improve order feasibility | Percentage of accepted orders with stock / fulfillment status confirmed |
| BO-04 | Strengthen cash visibility | Invoice aging, unapplied receipts and reconciliation completion |
| BO-05 | Reduce manual work | Count of duplicate-entry steps and time per handoff |
| BO-06 | Enable controlled expansion | Branch onboarding time, data completeness and role/access compliance |

## 4. Value hypothesis

If the business standardizes stages, ownership and handoffs—and connects its operational systems through governed interfaces—then managers should make faster decisions, sales teams should have clearer follow-up priorities, and finance should gain a more reliable view of outstanding receivables.

This is a hypothesis to validate. It does not guarantee a specific revenue increase. Revenue impact depends on demand, pricing, product availability, sales execution, margin and collections.

## 5. Scope

### In scope — minimum viable release

- Customer, contact and opportunity management.
- Defined pipeline stages, mandatory fields and next-action reminders.
- Quotation and order status linked to customer and opportunity records.
- Product availability and inventory reservation status.
- Invoice and receipt references, payment status and receivables aging.
- Role-based dashboards for sales, operations, finance and management.
- Audit events, exception queues and standard KPI definitions.

### Out of scope for the first release

- Replacing a bank, payment service provider or accounting ledger.
- Credit underwriting, micro-lending decisions or handling loan disbursements.
- Full payroll and HR transformation.
- Custom AI scoring that makes autonomous decisions.
- Real-time integration with every legacy system before interface discovery.
- Any claim of regulatory compliance before legal and security review.

## 6. Assumptions and constraints

- The business can identify data owners and process owners.
- Existing CRM, ERP/POS or finance tools expose an API, export or controlled integration path.
- Customer, product, order, invoice and payment references can be standardized.
- Business users are available for discovery, UAT and training.
- Initial scope is limited to one business unit or a small pilot group.
- Budget, data quality, integration capability and security requirements require validation before estimation.

## 7. Illustrative success criteria

Pilot targets should be agreed after a baseline measurement. Example directional targets for planning only:

- At least 95% of active qualified opportunities have an owner and next action.
- At least 98% of invoices and receipts in the pilot are linked by unique reference or placed in a visible exception queue.
- At least 90% of pilot users complete the primary workflow within the agreed process.
- A weekly management dashboard is generated from defined, reconcilable metrics.
- No critical access-control or financial-reconciliation defect remains open at go-live.

## 8. Options considered

| Option | Benefits | Trade-offs |
|---|---|---|
| Continue spreadsheets | Lowest immediate change cost | Weak ownership, auditability and scale |
| Replace all systems at once | Potentially unified platform | High migration, change and delivery risk |
| Integrate and standardize incrementally | Lower blast radius, measurable learning | Requires clear system ownership and interface governance |

**Recommendation:** phased integration and process standardization, subject to discovery and a feasibility assessment.

## 9. Decision requested

Approve a time-boxed discovery and solution-design phase—not a full implementation commitment—to establish the baseline, map processes, confirm data ownership, assess integration feasibility, estimate effort and prepare a prioritized MVP backlog.
