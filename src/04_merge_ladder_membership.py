import pandas as pd

# --- Load data ---
ladder_raw = pd.read_csv("data/raw/ladder_raw.csv", index_col=0)
membership_clean = pd.read_csv("data/clean/membership_clean.csv")

# --- Transform ladder_raw from wide to long ---
ladder_long = ladder_raw.melt(ignore_index=False, var_name="year", value_name="ladder_position").reset_index()
ladder_long.columns = ["club", "year", "ladder_position"]
ladder_long["year"] = ladder_long["year"].astype(int)

# --- Merge ladder and membership data ---
merged = pd.merge(ladder_long, membership_clean, on=["club", "year"], how="inner")

# --- Add threshold indicators (numeric) ---
merged["finals"] = (merged["ladder_position"] <= 8).astype(int)
merged["top4"] = (merged["ladder_position"] <= 4).astype(int)

# --- Sort by year and club ---
merged = merged.sort_values(by=["year", "club"]).reset_index(drop=True)

# --- Save ---
merged.to_csv("data/clean/merged_data_2012_2025.csv", index=False)
print("Ladder and membership data merged and saved to data/clean/merged_data_2012_2025.csv")
print(f"\nShape: {merged.shape}")
print(f"\nFirst few rows:")
print(merged.head(10))
print(f"\nLast few rows:")
print(merged.tail(10))
print(f"\nColumns: {merged.columns.tolist()}")
