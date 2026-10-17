# 08 — Delivery Roadmap, Risks and Dependencies

## 1. Phased delivery plan

This is an indicative sequence; effort and calendar dates must be estimated after discovery.

| Phase | Work | Exit criteria |
|---|---|---|
| 0. Discover | Interviews, system inventory, current-state map, baseline KPIs, data sample | Sponsor and process owners validate problem and scope |
| 1. Define | BRD / PRD, user stories, architecture options, non-functional requirements, ROM estimate | MVP scope, acceptance criteria and dependencies approved |
| 2. Foundation | Identity, roles, account / opportunity model, audit, integration conventions | Security and data ownership checks pass |
| 3. Commercial MVP | Lead capture, stages, next actions, quote reference, pipeline dashboard | Sales UAT passes and records reconcile to source |
| 4. Order-to-cash | Order, inventory status, invoice references and payment exception workflow | Operations and finance UAT pass; reconciliation tested |
| 5. Pilot and learn | Training, limited rollout, telemetry, feedback, defect correction | Adoption and operational success criteria achieved |
| 6. Scale | Additional branches, automation, richer analytics and future integrations | Performance and support readiness validated |

## 2. Prioritization model

Score candidate features against:
- business value / KPI linkage;
- user frequency and pain severity;
- risk reduction / mandatory control;
- feasibility and dependency;
- effort and ongoing support cost;
- data readiness and evidence confidence.

A simple weighted score can be used to start discussion, but high-risk financial controls should not be deprioritized solely because they produce less visible revenue.

## 3. Risk register

| ID | Risk | Likelihood / impact | Mitigation | Owner |
|---|---|---|---|---|
| R-01 | Poor data quality undermines trust | High / High | Profile sample data; define cleansing and ownership before migration | Data owner |
| R-02 | Unclear source of truth causes conflicts | Medium / High | Domain authority matrix and conflict-resolution rules | Architect / business owners |
| R-03 | Integration provider changes or downtime | Medium / High | Versioned contract, retries, monitoring and exception queue | Engineering |
| R-04 | Users continue using spreadsheets | High / Medium | Co-design workflow, simplify tasks, train champions, measure adoption | Business owner |
| R-05 | Forecast is mistaken for guaranteed revenue | Medium / High | Label weighted pipeline; separate bookings, billed revenue and cash | Sales / finance |
| R-06 | Payment event is duplicated or forged | Medium / Critical | Signature validation, idempotency, reconciliation and audit | Security / finance |
| R-07 | Scope expands before the MVP proves value | High / Medium | Stage-gate, change log, explicit out-of-scope items | Sponsor / product |
| R-08 | Personal or financial data is over-shared | Medium / High | Least privilege, minimization, retention controls and privacy review | Security / data owner |
| R-09 | AI-generated content contains errors or leaks data | Medium / High | Human review, approved tools, synthetic data for demos, no secret uploads | Product / security |
| R-10 | Operational support is not ready for launch | Medium / High | Runbooks, escalation path, monitoring, backup / restore rehearsal | IT / operations |

## 4. Dependencies

- Named business owner and data stewards.
- Access to representative, approved and minimized process/data samples.
- Availability of current-system APIs, exports or integration documentation.
- Identity provider and role model decision.
- Approval matrix for discounts, credit terms, refunds and financial adjustments.
- Finance agreement on invoice, receipt, collection and reconciliation definitions.
- UAT participants and training time.
- Environment, backup and support readiness.

## 5. Governance cadence

- Weekly delivery review: milestones, risks, dependencies, scope and decisions.
- Weekly product review: backlog ordering, acceptance criteria and feedback.
- Architecture review at key interfaces, security assumptions and data migrations.
- UAT review: test evidence, defect severity and business sign-off.
- Go/no-go checklist: controls, monitoring, rollback, user support, owner coverage and data reconciliation.

## 6. Release and rollback principle

Do not launch based on a successful demo alone. Launch only after agreed critical tests, data reconciliation, access-control checks, monitoring, backup/restore evidence and support ownership are complete. Keep a clear rollback / fallback approach for integrations that impact orders, invoices or payment status.
