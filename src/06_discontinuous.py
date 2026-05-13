import pandas as pd
import numpy as np

import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# Load your merged dataset
df = pd.read_csv("data/clean/merged_data_2012_2025.csv")

# Keep only positions 1–8
df = df[(df["ladder_position"] >= 1) & (df["ladder_position"] <= 8)]

# Create treatment indicator: 1 if Top 4, 0 if 5–8
df["top4"] = (df["ladder_position"] <= 4).astype(int)

# Running variable centered at cutoff (4.5)
df["running"] = df["ladder_position"] - 4.5

# RDD model: membership ~ treatment + running + interaction
model = smf.ols("membership ~ top4 + running + top4:running", data=df).fit()

print(model.summary())

# Extract discontinuity (coefficient on top4)
jump = model.params["top4"]
print(f"\nEstimated discontinuity at cutoff (Top 4 vs 5–8): {jump:.0f} members")

# ---- Plot ----
plt.figure(figsize=(10, 6))

# Scatter
plt.scatter(df["ladder_position"], df["membership"], alpha=0.6, label="Clubs")

# Fit lines on each side
x_left = np.linspace(1, 4, 100)
x_right = np.linspace(5, 8, 100)

# Predictions
pred_left = model.params["Intercept"] \
             + model.params["top4"]*1 \
             + model.params["running"]*(x_left - 4.5) \
             + model.params["top4:running"]*(x_left - 4.5)

pred_right = model.params["Intercept"] \
             + model.params["running"]*(x_right - 4.5)

plt.plot(x_left, pred_left, color="blue", label="Top 4 fit")
plt.plot(x_right, pred_right, color="red", label="5–8 fit")

# Cutoff line
plt.axvline(4.5, color="black", linestyle="--", linewidth=1)

plt.title("Regression Discontinuity: Top 4 vs 5–8")
plt.xlabel("Ladder Position")
plt.ylabel("Membership")
plt.legend()
plt.tight_layout()

plt.savefig("outputs/top4_vs_5_8_rdd.png", dpi=300)
plt.show()


