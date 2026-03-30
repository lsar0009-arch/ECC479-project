import pandas as pd

# --- Load full membership data ---
membership_all = pd.read_csv("data/clean/membership_clean.csv")

# --- Filter to 2012-2025 ---
membership_filtered = membership_all[(membership_all['year'] >= 2012) & (membership_all['year'] <= 2025)]

# --- Save filtered membership data ---
membership_filtered.to_csv("data/clean/membership_clean.csv", index=False)
print("Membership data filtered to 2012-2025 and saved to data/clean/membership_clean.csv")
print(f"\nShape: {membership_filtered.shape}")
print(f"\nFirst few rows:")
print(membership_filtered.head(10))
print(f"\nLast few rows:")
print(membership_filtered.tail(10))
