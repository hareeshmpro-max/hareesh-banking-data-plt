from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data" / "sample"

FILES = [
    "customers.csv",
    "accounts.csv",
    "transactions.csv",
    "loans.csv",
    "interest_rates.csv",
]

def main():
    for file_name in FILES:
        path = DATA / file_name
        df = pd.read_csv(path)
        print(f"\n=== {file_name} ===")
        print("shape:", df.shape)
        print("columns:", list(df.columns))
        print("nulls:")
        print(df.isna().sum())
        print("duplicates:", df.duplicated().sum())

if __name__ == "__main__":
    main()
