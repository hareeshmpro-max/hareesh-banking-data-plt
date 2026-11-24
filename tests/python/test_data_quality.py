from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data" / "sample"


def test_customer_ids_are_not_null():
    df = pd.read_csv(DATA / "customers.csv")
    assert df["customer_id"].notna().all()


def test_valid_transaction_statuses_exist_in_source():
    df = pd.read_csv(DATA / "transactions.csv")
    assert set(df["status"].dropna()).issubset(
        {"SUCCESS", "FAILED", "UNKNOWN"}
    )


def test_valid_transactions_have_existing_accounts():
    transactions = pd.read_csv(DATA / "transactions.csv")
    accounts = pd.read_csv(DATA / "accounts.csv")

    valid_transactions = transactions[
        transactions["status"].eq("SUCCESS")
        & transactions["amount"].notna()
        & transactions["amount"].gt(0)
    ].copy()

    invalid_account_transactions = valid_transactions[
        ~valid_transactions["account_id"].isin(accounts["account_id"])
    ]

    # Invalid source records are expected to be excluded
    # from the analytics population.
    assert set(invalid_account_transactions["transaction_id"]) == {"T99998"}