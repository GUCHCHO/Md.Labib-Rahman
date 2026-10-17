# 12 — Product Brief and Revenue Growth Experiments

## 1. Product concept

**Working name:** Revenue Operations Control Tower  
**Product type:** Modular SaaS workflow and decision-support layer for growing SMEs  
**Problem space:** Businesses can acquire customers and add branches faster than they standardize handoffs among sales, inventory, operations and finance.

This concept builds on the case study's process and data model. It is a product hypothesis—not an existing commercial product or a validated market opportunity.

## 2. Vision and positioning

**Vision:** Help growing businesses convert customer demand into fulfilled orders and traceable cash collection with less operational friction.

**Positioning statement:** For SMEs that operate across multiple teams, branches or sales channels, the Control Tower provides a joined-up view of lead-to-cash workflows, exceptions and performance without requiring an immediate replacement of every existing system.

**Differentiation hypothesis:** Combine practical process templates, integrations and governed operational KPIs—not only dashboards or a standalone CRM.

## 3. Target users and jobs to be done

| Persona | Job to be done | Pain to validate | Value hypothesis |
|---|---|---|---|
| Owner / Managing Director | Identify what is blocking growth and cash conversion | Conflicting reports and delayed exceptions | One consistent management view |
| Sales Manager | Improve follow-up and conversion | Stale opportunities, unclear ownership | Better next-action discipline and funnel visibility |
| Operations Lead | Fulfill commitments reliably | Late stock and handoff surprises | Earlier availability and exception visibility |
| Finance Lead | Know what is billed, collected and outstanding | Unmatched receipts and unclear ownership | Traceable reconciliation and receivables aging |
| Branch Manager | Run local operations using shared standards | Different processes and spreadsheets by location | Configurable workflow with consistent controls |

Personas and pain statements should be confirmed through interviews, observation, process samples and data profiling.

## 4. Product principles

- **Adopt before expanding:** first make one important workflow useful; then add modules.
- **Integrate before replacing:** preserve capable systems and make source-of-truth boundaries explicit.
- **Actionable metrics:** every view should suggest a decision or owner action.
- **Exception-first operations:** surface overdue follow-ups, unavailable stock, sync failures and unmatched payments.
- **Configurable, not infinitely custom:** support common process differences while avoiding one-off forks.
- **Trust and control:** roles, audit trails, reconciliation and data minimization are core product behaviors.

## 5. MVP hypothesis

### Must have
- Account and opportunity ownership, stages and next-action reminders.
- Quote / order references and basic stock availability status.
- Invoice references, receipt matching states and exception queue.
- Role-specific pipeline, order risk and receivables dashboards.
- CSV import/export with validation, change history and operational alerts.

### Should have
- Branch filtering and configurable approval thresholds.
- Integration health and retry status for authorized operators.
- Standardized lead source, loss reason and customer-segment taxonomies.

### Later, subject to discovery
- Self-service integration connectors.
- Cohort and retention analytics.
- AI-assisted summaries or follow-up suggestions with human review.
- Industry templates for distribution, retail, furniture, pharmacies and service businesses.

Not in the proposed MVP: payment custody, lending decisions, credit scoring or autonomous financial actions.

## 6. Packaging and business model hypotheses

Potential commercial components to evaluate—not approved prices or actual current offerings:

1. **Subscription:** recurring fee by business size, modules or active branches.
2. **Implementation / onboarding:** workflow mapping, configuration, data import, role setup and training.
3. **Integration services:** scoped connectors for existing accounting, inventory, payment or CRM systems.
4. **Premium analytics:** advanced reporting, multi-branch rollups and additional governance features.
5. **Support tier:** defined response windows, onboarding support and service review.

### Unit economics to model

- Monthly recurring revenue = active paying accounts × average recurring revenue per account.
- Gross margin = (recognized revenue − direct delivery / service costs) ÷ recognized revenue.
- Customer acquisition cost = attributable sales and marketing spend ÷ new paying customers in the same cohort.
- CAC payback = acquisition cost ÷ monthly gross profit per new customer.
- Net revenue retention = (opening recurring revenue + expansion − contraction − churn) ÷ opening recurring revenue.
- Implementation capacity = available delivery hours ÷ average approved onboarding effort.

Validate each formula against finance definitions. Segment by customer cohort and do not conflate one-time implementation revenue with recurring subscription revenue.

## 7. Growth funnel and metric tree

~~~mermaid
flowchart TD
  A[Target accounts] --> B[Qualified discovery]
  B --> C[Validated problem and product fit]
  C --> D[Proposal / paid pilot]
  D --> E[Contract and onboarding]
  E --> F[Activation: first workflow completed]
  F --> G[Repeated weekly usage]
  G --> H[Renewal and expansion]
  H --> I[Reference / referral]
~~~

North Star candidate: **weekly completed, traceable lead-to-cash workflows per active customer**, provided that workflow completion reflects genuine customer value and can be measured reliably.

Supporting metrics:
- Acquisition: qualified discovery rate and source-level conversion.
- Sales: discovery-to-proposal, proposal-to-win, cycle length and loss reason.
- Activation: time to first successful workflow and onboarding completion.
- Adoption: weekly active operators, completion rate and exception-resolution time.
- Retention: logo churn, revenue churn, renewal rate and net revenue retention.
- Economics: gross margin, support cost, onboarding effort and CAC payback.
- Quality: sync failure rate, unmatched payment items, duplicate records and data freshness.

Guardrails: do not optimize raw activity or lead count at the expense of customer fit, gross margin, data quality, or responsible sales practices.

## 8. Prioritized growth experiments

Experiments are proposed and have not been run. Each needs an owner, baseline, sample / cohort definition, duration and decision rule.

| Experiment | Hypothesis | Measurement | Decision rule |
|---|---|---|---|
| Workflow diagnostic before demo | A structured discovery workshop increases qualified proposal rate | Discovery-to-proposal conversion by comparable cohort | Continue only if lift persists without longer unproductive cycle time |
| Industry-specific onboarding checklist | A relevant template shortens activation time | Median days to first completed workflow | Adopt if time falls without increasing rework or support |
| Integration-readiness assessment | Early connector validation reduces late-stage scope changes | Integration-related change requests and delivery variance | Standardize if risk falls across several pilots |
| Exception inbox | Clear ownership improves overdue-item resolution | Median time to resolve and proportion overdue | Roll out if the metric improves and false alerts remain acceptable |
| Manager weekly review pack | Consistent KPIs increase action completion | Number of assigned actions completed by due date | Keep metrics used in recurring decisions; remove vanity metrics |
| Branch rollout playbook | Standard rollout steps reduce onboarding variance | Time and rework per additional branch | Expand if repeatability is demonstrated across branches |

Use holdouts or before/after comparison carefully; control for seasonality, deal mix, pricing changes and sample size. A correlation is not proof that the feature caused revenue lift.

## 9. 90-day learning roadmap

**Days 1–30 — Validate the problem**
- Interview business owners and frontline users.
- Observe one current lead-to-cash process.
- Review a minimized, authorized sample of pipeline and receivables data.
- Agree baseline definitions, target segment and top process bottlenecks.
- Decide which existing system remains the authority for each data domain.

**Days 31–60 — Prototype and test**
- Prototype opportunity follow-up and exception handling.
- Test role-specific dashboards with representative users.
- Validate integration feasibility and security assumptions.
- Define onboarding, support and implementation-cost assumptions.
- Run usability sessions before expanding scope.

**Days 61–90 — Pilot and evaluate**
- Pilot with a controlled user group using a signed-off scope.
- Track adoption, process time, data quality and exception resolution.
- Compare results with the measured baseline and note confounding factors.
- Decide whether to continue, change segment / scope or stop.
- Prepare a scale plan only if user value and operational readiness are demonstrated.

## 10. Go-to-scale gates

Scale only when:
- Repeated usage confirms the workflow solves a material problem.
- A customer can onboard with a repeatable process and support effort.
- Integration and data controls work reliably under the observed load.
- Gross margin and support burden are understood well enough for pricing decisions.
- KPI definitions reconcile to source systems.
- Security, privacy, contractual and regulatory reviews are complete for actual data and service boundaries.

**Product strategy conclusion:** durable growth should come from repeatable customer value, controlled delivery economics, reliable integrations and measurable adoption—not feature volume alone.
