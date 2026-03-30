import pandas as pd

# --- Load raw data ---
ladder = pd.read_csv("data/raw/ladder_raw.csv", header=0, index_col=0)
membership = pd.read_csv("data/raw/membership_raw.csv", header=0, index_col=0)

# --- Melt wide to long ---
ladder_long = ladder.melt(ignore_index=False, var_name="year", value_name="ladder_position").reset_index()
ladder_long.columns = ["club", "year", "ladder_position"]

membership_long = membership.melt(ignore_index=False, var_name="year", value_name="membership").reset_index()
membership_long.columns = ["club", "year", "membership"]

# --- Clean types ---
ladder_long["year"] = ladder_long["year"].astype(int)
membership_long["year"] = membership_long["year"].astype(int)
membership_long["membership"] = membership_long["membership"].str.replace(",", "").astype(int)

# --- Merge ---
merged = pd.merge(ladder_long, membership_long, on=["club", "year"], how="inner")

# --- Add threshold indicators ---
merged["finals"] = (merged["ladder_position"] <= 8).astype(int)
merged["top4"] = (merged["ladder_position"] <= 4).astype(int)

# --- Save ---
merged.to_csv("data/clean/merged_data.csv", index=False)
print(merged.head())
print(f"Shape: {merged.shape}")
