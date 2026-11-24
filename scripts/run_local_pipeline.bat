@echo off
python python/ingestion/01_profile_sources.py
python python/validation/02_data_quality.py
python python/transformation/03_prepare_transactions.py
python python/validation/04_reconciliation.py
