import pandas as pd

df = pd.read_csv("data/acne_data.csv")

print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nSummary:")
print(df.describe())