from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data" / "sample"

def duplicate_count(df, key):
    return int(df[key].duplicated().sum())

def main():
    customers = pd.read_csv(DATA / "customers.csv")
    accounts = pd.read_csv(DATA / "accounts.csv")
    transactions = pd.read_csv(DATA / "transactions.csv")
    loans = pd.read_csv(DATA / "loans.csv")

    checks = {
        "customer_duplicate_ids": duplicate_count(customers, "customer_id"),
        "account_duplicate_ids": duplicate_count(accounts, "account_id"),
        "transaction_duplicate_ids": duplicate_count(transactions, "transaction_id"),
        "loan_duplicate_ids": duplicate_count(loans, "loan_id"),
        "transaction_null_amount": int(transactions["amount"].isna().sum()),
        "transaction_negative_amount": int((transactions["amount"] < 0).sum()),
        "invalid_transaction_status": int((~transactions["status"].isin(["SUCCESS", "FAILED"])).sum()),
        "negative_account_balance": int((accounts["balance"] < 0).sum()),
        "invalid_loan_status": int((~loans["loan_status"].isin(["ACTIVE", "CLOSED"])).sum()),
    }

    print("DATA QUALITY SUMMARY")
    print("-" * 30)
    for name, value in checks.items():
        print(f"{name}: {value}")

if __name__ == "__main__":
    main()
