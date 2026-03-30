import pandas as pd

# --- Load membership clean data ---
membership_clean = pd.read_csv("data/clean/membership_clean.csv")

# --- Convert membership to integer ---
membership_clean["membership"] = membership_clean["membership"].fillna(0).astype(int)

# --- Save ---
membership_clean.to_csv("data/clean/membership_clean.csv", index=False)
print("Membership column converted to integer format in membership_clean.csv")
print(f"\nFirst few rows:")
print(membership_clean.head(10))
print(f"\nLast few rows:")
print(membership_clean.tail(10))
