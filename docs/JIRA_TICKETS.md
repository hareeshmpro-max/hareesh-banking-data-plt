# Jira Practice Backlog

## JIRA-2451 - Transaction reconciliation mismatch
Priority: High

Business reports that March 2026 transaction totals in the analytics layer do not match the source.

Acceptance criteria:
- Identify the cause.
- Correct the transformation logic.
- Re-run the affected dataset.
- Source and target transaction counts must reconcile for valid records.
- Source and target successful transaction amount totals must reconcile.
- Add/update a validation test.

## JIRA-2480 - Add customer segment KPI
Priority: Medium

Add monthly transaction amount by customer segment to the analytics layer.

Acceptance criteria:
- Use only successful transactions.
- Include Premium, Standard and any future segment values.
- Preserve existing monthly metrics.
- Add SQL test coverage.

## JIRA-2510 - Python validation enhancement
Priority: Medium

The ingestion validation script currently checks nulls but does not report duplicate IDs.

Acceptance criteria:
- Add duplicate-key checks.
- Produce a readable validation summary.
- Return a non-zero exit code when critical quality rules fail.

## JIRA-2550 - Loan portfolio forecast dataset
Priority: Medium

Prepare a monthly loan portfolio dataset for forecasting.

Acceptance criteria:
- Monthly active loan amount.
- Monthly average interest rate.
- No duplicate month records.
- Output CSV under `data/output/`.
