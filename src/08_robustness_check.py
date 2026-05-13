import pandas as pd
import statsmodels.formula.api as smf

# ---- Load cleaned data ----
df = pd.read_csv("data/cleaned_afl.csv")

# ---- Helper function ----
def run_rdd(data, treatment, running):
    formula = f"membership ~ {treatment} + {running} + {treatment}:{running}"
    return smf.ols(formula, data=data).fit()

# ---- Baseline windows ----
df_base_top4 = df[(df.ladder_position >= 1) & (df.ladder_position <= 8)]
df_base_finals = df[(df.ladder_position >= 5) & (df.ladder_position <= 10)]

# ---- Narrow bandwidth ----
df_narrow_top4 = df[(df.ladder_position >= 3) & (df.ladder_position <= 6)]
df_narrow_finals = df[(df.ladder_position >= 7) & (df.ladder_position <= 10)]

# ---- Wide bandwidth ----
df_wide_top4 = df[(df.ladder_position >= 1) & (df.ladder_position <= 10)]
df_wide_finals = df[(df.ladder_position >= 5) & (df.ladder_position <= 12)]

# ---- Placebo cutoff ----
df["placebo"] = (df.ladder_position <= 6).astype(int)
df["running_placebo"] = df.ladder_position - 6.5

# ---- Run models ----
model_base_top4 = run_rdd(df_base_top4, "top4", "running")
model_narrow_top4 = run_rdd(df_narrow_top4, "top4", "running")
model_wide_top4 = run_rdd(df_wide_top4, "top4", "running")

model_base_finals = run_rdd(df_base_finals, "five_to_eight", "running")
model_narrow_finals = run_rdd(df_narrow_finals, "five_to_eight", "running")
model_wide_finals = run_rdd(df_wide_finals, "five_to_eight", "running")

model_placebo = smf.ols(
    "membership ~ placebo + running_placebo + placebo:running_placebo",
    data=df
).fit()

# ---- Extract treatment effects ----
def extract_tau(model, varname):
    return model.params[varname], model.bse[varname]

# Top 4 cutoff
tau_base_top4, se_base_top4 = extract_tau(model_base_top4, "top4")
tau_narrow_top4, se_narrow_top4 = extract_tau(model_narrow_top4, "top4")
tau_wide_top4, se_wide_top4 = extract_tau(model_wide_top4, "top4")

# Finals cutoff
tau_base_finals, se_base_finals = extract_tau(model_base_finals, "five_to_eight")
tau_narrow_finals, se_narrow_finals = extract_tau(model_narrow_finals, "five_to_eight")
tau_wide_finals, se_wide_finals = extract_tau(model_wide_finals, "five_to_eight")

# Placebo
tau_placebo, se_placebo = extract_tau(model_placebo, "placebo")

# ---- Print results ----
print("\n--- Robustness Results (Top 4 Cutoff) ---")
print("Main:", tau_base_top4, se_base_top4)
print("Narrow:", tau_narrow_top4, se_narrow_top4)
print("Wide:", tau_wide_top4, se_wide_top4)

print("\n--- Robustness Results (Finals Cutoff) ---")
print("Main:", tau_base_finals, se_base_finals)
print("Narrow:", tau_narrow_finals, se_narrow_finals)
print("Wide:", tau_wide_finals, se_wide_finals)

print("\n--- Placebo Cutoff ---")
print("Placebo:", tau_placebo, se_placebo)
