# Real-Time Company Workflow

## 1. Before changing code
- Pull the latest main branch.
- Read the Jira ticket.
- Identify impacted source, SQL, Python, model and tests.
- Reproduce the issue locally.

## 2. Branch
Example:
```bash
git checkout main
git pull origin main
git checkout -b feature/JIRA-2451-transaction-reconciliation
```

## 3. Investigate
Typical order:
1. Source file / source table
2. Staging SQL
3. Transformation SQL
4. Python transformation
5. Target model
6. Validation queries
7. Tests

## 4. Implement
Make the smallest change that satisfies the requirement.

## 5. Validate
Check:
- row counts
- null counts
- duplicate counts
- source-to-target totals
- business-rule results
- regression tests

## 6. Deliver
```bash
git status
git diff
git add .
git commit -m "Fix transaction reconciliation for JIRA-2451"
git push -u origin feature/JIRA-2451-transaction-reconciliation
```

Then open a Pull Request and explain:
- What changed
- Why
- Validation performed
- Any known limitations
