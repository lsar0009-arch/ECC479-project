1. Data Overview

1.1 Dataset Description

The merged dataset contains AFL club-year observations from 2012-2025, combining:
- ladder data (final finishing position)
- membership data (annual club membership totals)
- derived variables (finals qualification, treatment/control groups)
each row represents a club in a given season


1.2 Data Dimensions
Rows: 18 Clubs x 14 seasons 
Columns: 


1.3: Variables included

Key variables (full definitions in data/clean/docs/codebook.md):

- team — AFL club name
- year — season year
- ladder_position — final ladder rank (1 = best, 18 = worst)
- membership_total — total club membership
- finals_qualified — 1 if ladder_position ≤ 8
- treatment_group — 1 if finishing 6th–8th
- control_group — 1 if finishing 9th–10th
- membership_change — year‑to‑year change
- membership_growth_rate — percentage change


1.4 Summary of Statistics

import pandas as pd

# Load your merged analysis-ready dataset
df = pd.read_csv("../data/clean/merged_data_2012_2025.csv")

df.head()
# Summary statistics for all numeric variables
df.describe()

# Check for missing values
df.isna().sum()

# Summary statistics for membership specifically
df['membership_total'].describe()


# Optional: histogram of membership totals
import matplotlib.pyplot as plt

df['membership_total'].hist(bins=20)
plt.xlabel("Membership Total")
plt.ylabel("Frequency")
plt.title("Distribution of AFL Club Membership Totals")
plt.show()
