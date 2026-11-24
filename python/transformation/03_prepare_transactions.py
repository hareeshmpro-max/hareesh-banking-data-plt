from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data" / "sample"
OUT = BASE / "data" / "output"
OUT.mkdir(parents=True, exist_ok=True)

def main():
    transactions = pd.read_csv(DATA / "transactions.csv")
    accounts = pd.read_csv(DATA / "accounts.csv")

    valid = transactions[
        transactions["status"].eq("SUCCESS")
        & transactions["amount"].notna()
        & transactions["amount"].gt(0)
    ].copy()

    valid = valid.merge(
        accounts[["account_id", "customer_id", "account_type"]],
        on="account_id",
        how="inner",
        validate="many_to_one",
    )

    valid["transaction_date"] = pd.to_datetime(valid["transaction_date"])
    valid["month"] = valid["transaction_date"].dt.to_period("M").astype(str)

    output = (
        valid.groupby(["month", "customer_id"], as_index=False)
        .agg(
            transaction_count=("transaction_id", "count"),
            transaction_amount=("amount", "sum"),
        )
    )

    output.to_csv(OUT / "monthly_customer_transactions.csv", index=False)
    print(output.head(10))
    print(f"Written: {OUT / 'monthly_customer_transactions.csv'}")

if __name__ == "__main__":
    main()
