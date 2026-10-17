# 02 — Discovery Plan and Stakeholder Map

## 1. Discovery outcome

Create an evidence-based view of the business process, validate business goals, distinguish symptoms from root causes, and make scope and architecture decisions traceable to stakeholder needs.

## 2. Interview plan

| Session | Participants | Focus | Evidence to capture |
|---|---|---|---|
| Business goals | Managing director / business owner | Growth priorities, branch strategy, margin and cash constraints | Goals, constraints, decision criteria |
| Sales process | Sales lead, account executives | Lead sources, qualification, follow-ups, quotation and win/loss | Pipeline stages, aging, exceptions |
| Operations | Warehouse, procurement, delivery | Stock checks, reservations, replenishment and fulfillment | Order handoffs, bottlenecks, stock rules |
| Finance | Accountant, finance lead | Invoice creation, receipt posting, aging and reconciliation | Control points, reconciliation sources |
| Technology | IT / product / vendors | Systems, APIs, identities, hosting, support model | System inventory, interface constraints |
| Frontline users | Representative users from each role | Daily tasks, workarounds, usability | Task frequency, pain points, adoption barriers |

## 3. High-value discovery questions

### Commercial
- How are leads sourced, assigned, deduplicated and qualified?
- What qualifies an opportunity to move to the next stage?
- What are the top loss reasons and how are they recorded?
- Which segments, products and channels have the strongest margin and repeat purchase?

### Operational
- At what point is stock availability confirmed?
- What prevents an accepted quotation from becoming a fulfilled order?
- Which handoffs require re-entering data?
- How are partial deliveries, returns and cancellations handled?

### Finance and controls
- Which record is authoritative for invoices, receipts and balances?
- How are bank transfers, mobile financial service receipts and cash entries matched?
- Who approves discounts, credit terms, refunds and write-offs?
- What audit and segregation-of-duties controls are mandatory?

### Technology and data
- Which applications currently hold customer, product, stock, order and finance data?
- Are APIs, webhooks, scheduled exports or database views available?
- What are the identity, retention, backup, recovery and access requirements?
- Which data must not be sent to third-party AI systems?

## 4. Stakeholder map

| Stakeholder | Primary concern | Role in decisions |
|---|---|---|
| Executive sponsor | Revenue, margin, cash and scale | Accountable for outcomes and funding |
| Sales lead | Pipeline quality, follow-up, forecast | Owns commercial workflow |
| Operations lead | Stock accuracy, fulfillment, service levels | Owns order execution process |
| Finance lead | Invoices, payments, receivables, controls | Owns finance definitions and reconciliation |
| Product / BA | Requirements, prioritization, traceability | Facilitates discovery and backlog |
| Architect / engineering | Integration, security, reliability | Validates feasibility and design |
| IT / data owner | Access, data quality, support, retention | Approves system and data controls |
| End users | Efficient everyday work | Validate usability and UAT |

## 5. Decision rights and cadence

- **Weekly discovery review:** open questions, evidence gaps, scope changes and decisions.
- **Weekly product triage:** priority, dependencies, risks and acceptance criteria.
- **Architecture checkpoint:** interface contract, source of truth, identity, security and operational readiness.
- **Stage-gate approval:** sponsor, process owner and technical lead accept the MVP scope before build begins.
- **Change control:** every material requirement change records rationale, impact, approver and updated acceptance criteria.

## 6. Discovery outputs

1. Current-state process map and exception list.
2. Stakeholder map, RACI and decision log.
3. System/context inventory and data-owner matrix.
4. Prioritized problem statements with evidence and frequency.
5. Validated functional and non-functional requirements.
6. Data-quality sample, baseline KPI definitions and measurement plan.
7. Initial solution options, risks, assumptions, dependencies and ROM estimate.

## 7. Evidence quality

For each finding, record whether it is:
- **Observed:** directly seen in the process or data.
- **Reported:** stated by a stakeholder but not independently checked.
- **Assumed:** introduced for planning and awaiting validation.
- **Decided:** formally agreed by the relevant owner.

This distinction protects the solution from being designed around untested assumptions.
