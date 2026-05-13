import pandas as pd
import statsmodels.formula.api as smf

# Load data
df = pd.read_csv("data/clean/merged_data_2012_2025.csv")

# Create treatment variable for Top 4 cutoff
df["top4"] = (df.ladder_position <= 4).astype(int)

# Create running variable for Top 4 cutoff
df["running_top4"] = df.ladder_position - 4.5

# Narrow bandwidth: positions 3–6
df_narrow = df[(df.ladder_position >= 3) & (df.ladder_position <= 6)]

# Run model
model = smf.ols(
    "membership ~ top4 + running_top4 + top4:running_top4",
    data=df_narrow
).fit()

print(model.summary())