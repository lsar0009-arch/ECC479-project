import pandas as pd

# --- Load merged data ---
merged = pd.read_csv("data/clean/merged_data_2012_2025.csv")

# --- Convert membership to integer ---
merged["membership"] = merged["membership"].fillna(0).astype(int)

# --- Save ---
merged.to_csv("data/clean/merged_data_2012_2025.csv", index=False)
print("Membership column converted to integer format")
print(f"\nFirst few rows:")
print(merged.head(10))
