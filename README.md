# Banking Data Platform - Company Simulation

## Purpose
This repository simulates an existing BFSI company's data platform for a 3-year Data Analyst / Data Engineering practice environment.

You are NOT expected to build everything from scratch. Treat this as an existing company repository:
1. Clone/pull the repository.
2. Read the documentation.
3. Run the existing pipeline.
4. Receive Jira tickets.
5. Investigate existing SQL/Python.
6. Make a focused change.
7. Test and validate.
8. Commit and push a feature branch.
9. Open a pull request.

## Business domain
Customer, account, transaction, loan and interest-rate data.

## Main technologies
- Python / Pandas
- SQL
- Relational database concepts
- ETL / data quality
- Dimensional modeling
- Git / GitHub
- Forecasting (practice layer)

## Important
This is a simulated company repository. It contains synthetic data and original practice code. It is not a real company's production repository.

## First setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python python/ingestion/01_profile_sources.py
python python/validation/02_data_quality.py
```

## Practice workflow
See `docs/REAL_TIME_WORKFLOW.md` and `docs/JIRA_TICKETS.md`.
