from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data" / "sample"

def test_customer_ids_are_not_null():
    df = pd.read_csv(DATA / "customers.csv")
    assert df["customer_id"].notna().all()

def test_valid_transaction_statuses_exist_in_source():
    df = pd.read_csv(DATA / "transactions.csv")
    assert set(df["status"].dropna()).issubset({"SUCCESS", "FAILED", "UNKNOWN"})
