import pandas as pd

# --- Load data ---
membership_1984_2024 = pd.read_csv("data/raw/membership_1984-2024_website.csv", index_col=0)
membership_2025 = pd.read_csv("data/raw/membership_2025_raw.csv", index_col=0)

# --- Transform 1984-2024 from wide to long ---
membership_long = membership_1984_2024.melt(ignore_index=False, var_name="year", value_name="membership").reset_index()
membership_long.columns = ["club", "year", "membership"]
membership_long["year"] = membership_long["year"].astype(int)

# --- Transform 2025 to long format ---
membership_2025_long = membership_2025.reset_index()
membership_2025_long.columns = ["club", "membership"]
membership_2025_long["year"] = 2025
membership_2025_long = membership_2025_long[["club", "year", "membership"]]
membership_2025_long["membership"] = membership_2025_long["membership"].astype(int)

# --- Combine all data ---
membership_all = pd.concat([membership_long, membership_2025_long], ignore_index=True)

# --- Sort by club and year ---
membership_all = membership_all.sort_values(by=["club", "year"]).reset_index(drop=True)

# --- Save clean membership data ---
membership_all.to_csv("data/clean/membership_clean.csv", index=False)
print("Membership data (1984-2025) merged and saved to data/clean/membership_clean.csv")
print(f"\nShape: {membership_all.shape}")
print(f"\nFirst few rows:")
print(membership_all.head(10))
print(f"\nLast few rows:")
print(membership_all.tail(10))



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


