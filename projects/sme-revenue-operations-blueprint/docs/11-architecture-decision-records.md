# Architecture Decision Records

## ADR-001 — Start with a modular application, not microservices
**Status:** Proposed for the fictional MVP  
**Context:** The case study needs clear domain boundaries and integrations, but has no measured scale, team topology or production SLOs yet.  
**Decision:** Begin with a modular application, relational data store, explicit service/domain boundaries and a dedicated integration worker where needed.  
**Rationale:** This is simpler to deploy, test, observe and support while preserving separation of concerns.  
**Consequences:** Module boundaries and interfaces must be enforced; later service extraction should require a measured need such as independent scaling, release cadence or fault isolation.  
**Revisit when:** Workload, availability, team ownership or bottleneck measurements justify distributed deployment.

## ADR-002 — Treat finance-source records and internal allocations separately
**Status:** Proposed  
**Context:** A single payment event may be duplicated, delayed, partially allocated or lack a trustworthy invoice reference.  
**Decision:** Preserve the source payment event separately from the internal reconciliation/allocation decision. Use stable source references, idempotency and an exception queue.  
**Rationale:** This supports auditability and prevents an unverified browser redirect or duplicate callback from becoming the sole financial proof.  
**Consequences:** Finance needs exception ownership, reconciliation reports, adjustment controls and explicit system-of-record decisions.  
**Revisit when:** The chosen accounting/PSP interfaces, settlement semantics or legal requirements are confirmed.

## ADR-003 — Govern KPI definitions before dashboard delivery
**Status:** Proposed  
**Context:** Pipeline, bookings, invoiced revenue, gross profit and collected cash can be confused in an ungoverned dashboard.  
**Decision:** Version-control metric definitions with owner, formula, reporting window, source and known limitations. Display refresh time and data-quality warnings.  
**Rationale:** A polished dashboard cannot compensate for ambiguous business definitions.  
**Consequences:** KPI sign-off and data reconciliation are part of delivery acceptance, not post-launch cleanup.  
**Revisit when:** Business models, finance policy or reporting requirements change.
