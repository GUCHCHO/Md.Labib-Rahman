# 09 — UAT and Acceptance Test Plan

## 1. Objective

Confirm that the MVP supports approved business workflows, controls, exceptions and reporting before users depend on it. UAT is performed by business representatives; technical tests alone do not establish business acceptance.

## 2. Test entry criteria

- Approved requirements and process maps.
- Test environment and representative synthetic / authorized test data.
- User roles and access matrix configured.
- Known system interfaces and failure responses documented.
- KPI definitions and expected calculations signed off.
- Test users and business decision-maker assigned.

## 3. Representative test scenarios

| Test ID | Scenario | Expected result |
|---|---|---|
| UAT-01 | Create a lead from a valid source | Unique ID, source and owner recorded |
| UAT-02 | Create a duplicate account / contact | Configured duplicate warning or controlled merge path appears |
| UAT-03 | Move qualified opportunity without next action | Save is blocked with actionable validation |
| UAT-04 | Change stage outside allowed progression | Change is blocked or authorized override is audited |
| UAT-05 | Prepare quote exceeding discount threshold | Approval workflow is triggered |
| UAT-06 | Confirm order when stock is partial | Partial / backorder state is visible; no false full-availability claim |
| UAT-07 | Integration provider retries the same event | Idempotency prevents duplicate order / receipt records |
| UAT-08 | Receive payment with valid invoice reference | Receipt is stored and allocation follows approved rules |
| UAT-09 | Receive unmatched payment | Exception queue and finance owner are populated |
| UAT-10 | User without finance role opens finance data | Access is denied and relevant security event is available |
| UAT-11 | Dashboard compares closed-won value with cash received | Measures remain separate and match test calculations |
| UAT-12 | Simulate integration outage | Failure is visible, retries are controlled, and recovery path is documented |
| UAT-13 | Export data as restricted user | Output respects role and branch permissions |
| UAT-14 | Restore a backed-up test dataset | Recovery steps are documented and data integrity is validated |

## 4. Defect severity

- **Critical:** unauthorized access, duplicate financial transaction, corrupted financial state, or no safe recovery. Blocks release.
- **High:** core workflow cannot complete or data integrity is materially wrong. Blocks release unless formally waived by the accountable owner with a safe workaround.
- **Medium:** partial functional issue with a documented workaround. Must be prioritized and accepted by the business owner.
- **Low:** cosmetic or low-impact usability issue. May be scheduled after release.

## 5. Exit criteria

- All critical and high defects resolved or explicitly rejected with evidence.
- All Must requirements have passing tests.
- Role and branch access tests pass.
- KPI calculations reconcile against the approved synthetic sample.
- Integration retries, duplicate events and exception cases tested.
- Business owners approve workflow and reporting behavior.
- Training notes, support owner, monitoring and rollback plan are available.

## 6. Test evidence record

For each test, keep: test ID, requirement ID, environment, test data ID, preconditions, steps, expected result, actual result, pass/fail, defect link, tester and date.

Never include real customer or payment credentials in screenshots, logs or sample fixtures.
