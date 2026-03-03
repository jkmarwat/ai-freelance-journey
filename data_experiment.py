import pandas as pd

data = {
    "month": ["Jan", "Feb", "Mar", "Apr"],
    "sales": [120, 150, 90, 200]
}

df = pd.DataFrame(data)

print(df)
print("\nStatistics\n")
print(df.describe())