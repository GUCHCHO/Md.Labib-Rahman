# 05 — Solution Architecture

## 1. Architectural intent

Use a modular, API-first design that preserves existing systems where sensible, avoids uncontrolled point-to-point dependencies, and makes business rules and financial control points explicit.

The design is conceptual. Technology selection, hosting, capacity, service-level objectives and cost require discovery and a technical proof of concept.

## 2. Context diagram

~~~mermaid
flowchart TB
  U[Sales, Operations, Finance, Management] --> UI[Web Application / Role-Based Views]
  UI --> APP[Business Services]
  CRM[Existing CRM or Lead Module] <--> INT[Integration Layer]
  ERP[ERP / Inventory / Orders] <--> INT
  FIN[Accounting / Invoicing] <--> INT
  PAY[Bank / MFS / Payment Provider] --> INT
  APP <--> INT
  APP --> DB[(Operational Database)]
  INT --> LOG[Audit, Monitoring and Exception Queue]
  DB --> BI[Analytics / KPI Layer]
  BI --> M[Management Dashboard]
~~~

## 3. Logical layers

1. **Experience layer:** web views for sales, operations, finance and executives.
2. **Application layer:** account, opportunity, quotation, order, invoice and reconciliation workflows.
3. **Domain layer:** business rules, stage transitions, approval limits, ownership and validation.
4. **Integration layer:** versioned REST APIs, event/webhook intake, scheduled imports and idempotent retry.
5. **Data layer:** operational relational database, event/audit history and analytical reporting model.
6. **Control layer:** identity, role-based access, secrets, audit, monitoring, backups, alerts and runbooks.

## 4. System-of-record proposal

| Data domain | Candidate authority | Integration approach |
|---|---|---|
| Account / contact | CRM or master data service | Stable account ID; duplicate-resolution policy |
| Opportunity / activity | CRM | Stage and activity events |
| Product / price list | ERP or product master | Versioned snapshots for quotes |
| Available stock | Inventory / ERP | Availability query; do not trust stale client-side cache |
| Order / fulfillment | ERP or order service | Unique order ID and status events |
| Invoice / receivable | Accounting system | Invoice ID, amount, currency and balance snapshot |
| Payment source record | Bank, MFS or PSP source | Verified source reference and amount |
| Reconciliation decision | Finance control service / accounting workflow | Matcher result, exception and approver audit |
| Analytics definitions | Governed KPI layer | Versioned formula and refresh timestamp |

Final authority must be agreed with data owners. No two systems should be treated as authoritative for the same field without an explicit conflict-resolution rule.

## 5. Integration rules

- Use stable IDs and correlation IDs across workflow steps.
- Design event handlers to be idempotent; a duplicate webhook must not create duplicate orders or receipts.
- Validate signatures and timestamps for provider callbacks where supported.
- Retry transient errors with backoff and a maximum-attempt policy.
- Send exhausted failures to a dead-letter / exception queue with owner and replay controls.
- Never treat a redirect page or client-side success message alone as proof of payment.
- Reconcile provider / bank source records against internal transactions.
- Separate synchronous decisions, such as a stock check, from asynchronous updates, such as a report refresh.

## 6. Security and resilience

- Enforce least privilege and role / branch-based access.
- Require MFA for privileged access and use managed secrets.
- Encrypt transport; assess encryption at rest and key management for selected hosting.
- Log sensitive actions without copying unnecessary personal or payment data into logs.
- Define retention, deletion, backup, restore and disaster-recovery policies before production.
- Monitor API latency/errors, queue age, sync lag, failed reconciliation and unusual admin activity.
- Review threat model and privacy impact based on actual data categories.

## 7. Scalability path

**MVP:** modular application + relational database + scheduled / API integrations.  
**Growth:** separate worker processes for integration, notifications and reconciliation; add queueing and reporting read models when justified.  
**Scale:** partition by business/tenant and branch where appropriate; add caching, read replicas, service boundaries and stronger SLOs based on measured bottlenecks.

Do not start with microservices solely for appearance. Introduce distributed components when independent scaling, team ownership or fault isolation justifies their operational cost.

## 8. Future domain extension

A later, separately governed phase could evaluate payment orchestration or education-finance / micro-credit workflows. That would require explicit consent, privacy and security design, ledger and reconciliation controls, eligibility policy, affordability / risk review, auditability, legal review and regulated-partner validation. This portfolio project does **not** implement lending or payment processing and should not be represented as a compliant financial product.
