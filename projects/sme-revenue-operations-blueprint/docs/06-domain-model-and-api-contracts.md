# 06 — Domain Model, Data Dictionary and API Contracts

## 1. Domain model

~~~mermaid
erDiagram
  ACCOUNT ||--o{ CONTACT : contains
  ACCOUNT ||--o{ OPPORTUNITY : owns
  OPPORTUNITY ||--o{ ACTIVITY : tracks
  OPPORTUNITY ||--o{ QUOTATION : has
  QUOTATION ||--o| ORDER : converts_to
  ORDER ||--o{ ORDER_LINE : contains
  ORDER ||--o{ INVOICE : billed_by
  INVOICE ||--o{ PAYMENT_ALLOCATION : settled_by
  PAYMENT ||--o{ PAYMENT_ALLOCATION : allocates
  USER ||--o{ ACTIVITY : owns
  USER ||--o{ AUDIT_EVENT : performs
~~~

## 2. Core entities and critical fields

| Entity | Key fields | Rules |
|---|---|---|
| Account | account_id, legal_name, segment, status, branch_id | Stable ID; duplicate checks; controlled merge |
| Contact | contact_id, account_id, name, business_email, phone, consent_status | Store minimum necessary data and consent where applicable |
| Opportunity | opportunity_id, account_id, owner_id, source, stage, amount_bdt, probability_pct, next_action_at, close_date | Stage history and owner required; amount is not realized revenue |
| Activity | activity_id, opportunity_id, owner_id, type, occurred_at, outcome, next_action_at | Track meaningful sales activity and follow-up |
| Quotation | quote_id, opportunity_id, version, valid_until, subtotal, discount, approval_status | Versioned; approval limits apply |
| Order | order_id, quote_id, order_status, fulfillment_status, branch_id | Unique ID; fulfillment state is distinct from payment status |
| Invoice | invoice_id, order_id, issue_date, due_date, amount_bdt, outstanding_bdt, status | Invoice authority and corrections must be explicit |
| Payment | payment_id, source_reference, received_at, amount_bdt, channel, reconciliation_status | Unique source reference where guaranteed by provider |
| Payment allocation | allocation_id, payment_id, invoice_id, allocated_bdt, created_by, created_at | Allocation sum cannot exceed receipt or applicable outstanding amount |
| Audit event | event_id, actor_id, entity_type, entity_id, action, occurred_at, correlation_id | Append-oriented security / business audit trail |

## 3. Data quality rules

- Required IDs are immutable and never based on mutable display names.
- Monetary values use fixed-precision decimal types, not binary floating-point.
- Store currency explicitly; BDT is assumed for this fictional sample.
- Store timestamps with timezone and use a consistent reporting timezone.
- Track source system and last-synchronized timestamp for integrated records.
- Validate stage probabilities against a controlled configuration; never silently rewrite historical forecast assumptions.
- Keep both event history and current state where auditability requires it.
- Define retention and deletion handling for personal data.

## 4. Example API contracts

These are illustrative contracts, not deployed endpoints.

### Create or update opportunity
**POST /api/v1/opportunities**

Request:
~~~json
{
  "account_id": "ACC-1042",
  "source": "partner",
  "stage": "qualified",
  "amount_bdt": "950000.00",
  "owner_id": "USR-008",
  "next_action_at": "2026-11-03T10:00:00+06:00"
}
~~~

Validation:
- Account and owner must exist and be visible to the caller.
- Amount must be a non-negative decimal with agreed precision.
- Source and stage must match the approved dictionaries.
- A qualified opportunity must have a next action.
- The response includes the opportunity ID, version and audit correlation ID.

### Payment reconciliation event
**POST /api/v1/payment-events**

Request:
~~~json
{
  "provider": "illustrative-provider",
  "source_reference": "SYNTH-REC-10021",
  "invoice_reference": "INV-SYNTH-2038",
  "amount_bdt": "25000.00",
  "currency": "BDT",
  "event_type": "receipt_confirmed"
}
~~~

Required control behavior:
- Validate provider authenticity using the agreed method.
- Enforce idempotency using a stable provider/event reference.
- Store the source event separately from the internal allocation decision.
- Return an explicit accepted / rejected / duplicate state.
- Send ambiguous invoice matches to an exception queue.
- Never expose bank credentials, payment tokens or secrets in application logs.

## 5. Open design questions

- Is the business multi-company, multi-tenant or only multi-branch?
- Which source owns product pricing and stock availability?
- Are partial receipts and multi-invoice allocations allowed?
- Which account and invoice identifiers are guaranteed unique by the current systems?
- Which personal data fields are necessary, and what are the approved retention periods?
- How will deleted or merged accounts propagate across systems?
