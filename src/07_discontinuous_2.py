import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv("data/clean/merged_data_2012_2025.csv")

# Keep only positions 5–10
df = df[(df["ladder_position"] >= 5) & (df["ladder_position"] <= 10)]

# Treatment indicator: 1 if 5–8, 0 if 9–10
df["five_to_eight"] = (df["ladder_position"] <= 8).astype(int)

# Running variable centered at cutoff (8.5)
df["running"] = df["ladder_position"] - 8.5

# RDD model
model = smf.ols("membership ~ five_to_eight + running + five_to_eight:running", data=df).fit()

print(model.summary())

# Estimated discontinuity
jump = model.params["five_to_eight"]
print(f"\nEstimated discontinuity at cutoff (5–8 vs 9–10): {jump:.0f} members")

# ---- Plot ----
plt.figure(figsize=(10, 6))

# Scatter
plt.scatter(df["ladder_position"], df["membership"], alpha=0.6, label="Clubs")

# Fit lines
x_left = np.linspace(5, 8, 100)
x_right = np.linspace(9, 10, 100)

pred_left = (
    model.params["Intercept"]
    + model.params["five_to_eight"] * 1
    + model.params["running"] * (x_left - 8.5)
    + model.params["five_to_eight:running"] * (x_left - 8.5)
)

pred_right = (
    model.params["Intercept"]
    + model.params["running"] * (x_right - 8.5)
)

plt.plot(x_left, pred_left, color="blue", label="5–8 fit")
plt.plot(x_right, pred_right, color="red", label="9–10 fit")

plt.axvline(8.5, color="black", linestyle="--", linewidth=1)

plt.title("Regression Discontinuity: 5–8 vs 9–10")
plt.xlabel("Ladder Position")
plt.ylabel("Membership")
plt.legend()
plt.tight_layout()

plt.savefig("outputs/rdd_5_8_vs_9_10.png", dpi=300)
plt.show()
