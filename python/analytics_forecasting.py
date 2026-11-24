from pathlib import Path
import pandas as pd
from sklearn.linear_model import LinearRegression

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "sample"

# Starter only: after completing the Jira tasks, build a proper monthly
# forecasting dataset and compare models.
