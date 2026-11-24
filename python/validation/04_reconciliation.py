from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data" / "sample"

def main():
    tx = pd.read_csv(DATA / "transactions.csv")

    source_success = tx[tx["status"].eq("SUCCESS") & tx["amount"].notna() & tx["amount"].gt(0)]
    print("VALID SOURCE TRANSACTION COUNT:", len(source_success))
    print("VALID SOURCE TRANSACTION AMOUNT:", source_success["amount"].sum())

    print("\nThis script is intentionally simple. Extend it when you receive a Jira ticket.")

if __name__ == "__main__":
    main()
