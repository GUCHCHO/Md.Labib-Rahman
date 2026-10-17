# 03 — Requirements and User Stories

## 1. Requirement conventions

Each requirement has a stable ID, priority, owner and testable acceptance condition. Priority uses MoSCoW: Must, Should, Could, Won't (this release). Final priorities require stakeholder approval.

## 2. Functional requirements

| ID | Requirement | Priority | Acceptance evidence |
|---|---|---|---|
| FR-01 | Create and update account/contact records with duplicate checks | Must | Duplicate warning is shown using configured matching rules |
| FR-02 | Record lead source, segment, owner, status and next action | Must | Required fields prevent incomplete qualified records |
| FR-03 | Manage opportunity stages using an approved stage model | Must | Invalid stage transitions are blocked or require authorized override |
| FR-04 | Link quotation, order and invoice references to the opportunity/account | Must | Authorized users can navigate between linked records |
| FR-05 | Check product availability before confirming fulfillment | Must | Order shows available, partial, backorder or exception status |
| FR-06 | Record receipt references and reconcile them to invoices | Must | Matched and unmatched receipts appear in separate states |
| FR-07 | Provide role-specific pipeline, aging and operational dashboards | Must | KPI calculations match approved definitions and sample checks |
| FR-08 | Notify owners about overdue follow-up actions | Should | Reminder is generated from the configured due-date rule |
| FR-09 | Maintain an audit history of material changes | Must | Actor, timestamp, action and reference are available to authorized reviewers |
| FR-10 | Export role-filtered reports for review | Should | Export respects permissions and records the export event where required |

## 3. Non-functional requirements

| ID | Quality attribute | Requirement / validation approach |
|---|---|---|
| NFR-01 | Security | Role-based access, least privilege, MFA for privileged users, secrets outside source control |
| NFR-02 | Data integrity | Stable IDs, foreign-key rules, idempotent integration events and reconciliation checks |
| NFR-03 | Availability | Agree service objective after business impact and hosting review |
| NFR-04 | Performance | Define response-time SLO using pilot workload; measure p95 at representative load |
| NFR-05 | Scalability | Support additional branches through configuration, tenant / branch scoping and indexed queries |
| NFR-06 | Observability | Structured logs, correlation IDs, queue health, failed sync and reconciliation alerts |
| NFR-07 | Recovery | Approved backup schedule and tested recovery objectives before production |
| NFR-08 | Usability | Primary sales and finance tasks validated with representative users |
| NFR-09 | Privacy | Collect minimum necessary data; define purpose, access, retention and deletion policy |
| NFR-10 | Maintainability | Versioned APIs, automated checks, deployment notes and operational runbooks |

## 4. User stories and acceptance criteria

### US-01 — Qualified opportunity follow-up
**As a** sales representative, **I want** each qualified opportunity to have an owner and next action, **so that** active deals do not silently stall.

Acceptance criteria:
- Given an opportunity is moved to Qualified, when the user saves it, then owner, value range, source and next action are required.
- Given the next-action date has passed, when the daily reminder process runs, then the owner sees the overdue item.
- Given an opportunity is closed, then further reminders stop.

### US-02 — Order feasibility
**As an** operations coordinator, **I want** an order linked to a confirmed stock / fulfillment status, **so that** sales commitments reflect operational reality.

Acceptance criteria:
- Given an order is submitted, when availability is checked, then the system returns available, partial, backorder or exception.
- Given inventory data is stale or the stock service is unavailable, then the system does not silently assume availability.
- Given an order changes after reservation, then the reservation change is recorded.

### US-03 — Invoice and payment visibility
**As a** finance user, **I want** receipts reconciled against invoice references, **so that** balances and exceptions are visible.

Acceptance criteria:
- A receipt can be matched to one or more invoices according to approved allocation rules.
- Unmatched or partially matched receipts remain in an exception queue.
- The system records the source reference, date, amount, match decision and responsible user.
- A reconciliation report shows opening items, matched items, exceptions and closing balance.

### US-04 — Executive revenue view
**As an** executive, **I want** a consistent view of pipeline, win rate, billed revenue and collections, **so that** I can prioritize commercial and operational action.

Acceptance criteria:
- Every KPI has a defined formula, time window and data owner.
- Closed-won bookings are distinguished from invoices issued and cash collected.
- The report exposes the last refresh time and incomplete data warnings.

## 5. Business rules

- BR-01: An opportunity has one accountable owner at any point in time.
- BR-02: Stage progression follows the approved lifecycle; exceptions are audited.
- BR-03: Deal value is not the same as recognized revenue or cash received.
- BR-04: Order confirmation requires a documented fulfillment status.
- BR-05: Payment status is not marked reconciled without a match to source evidence.
- BR-06: Discount, credit and refund approvals follow configurable authority limits.
- BR-07: Users see only data allowed by role, branch and assigned business scope.
- BR-08: KPI definitions are version-controlled and owned by the business.

## 6. Traceability model

Problem statement → business objective → requirement → user story → process step → test case → KPI.

This traceability chain makes it possible to explain why a feature exists and which evidence shows that it works.
