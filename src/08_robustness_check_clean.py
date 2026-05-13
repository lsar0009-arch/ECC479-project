import pandas as pd
import statsmodels.formula.api as smf

# Load data
df = pd.read_csv("data/clean/merged_data_2012_2025.csv")

# --- Create treatment variables ---
df["top4"] = (df.ladder_position <= 4).astype(int)
df["five_to_eight"] = ((df.ladder_position >= 5) & (df.ladder_position <= 8)).astype(int)

# --- Create running variables ---
df["running_top4"] = df.ladder_position - 4.5
df["running_finals"] = df.ladder_position - 8.5

# --- Bandwidths ---
df_main_top4 = df[(df.ladder_position >= 1) & (df.ladder_position <= 8)]
df_narrow_top4 = df[(df.ladder_position >= 3) & (df.ladder_position <= 6)]
df_wide_top4 = df[(df.ladder_position >= 1) & (df.ladder_position <= 10)]

df_main_finals = df[(df.ladder_position >= 5) & (df.ladder_position <= 10)]
df_narrow_finals = df[(df.ladder_position >= 7) & (df.ladder_position <= 10)]
df_wide_finals = df[(df.ladder_position >= 5) & (df.ladder_position <= 12)]

# --- Placebo cutoff ---
df["placebo"] = (df.ladder_position <= 6).astype(int)
df["running_placebo"] = df.ladder_position - 6.5

# --- Helper ---
def run(formula, data):
    return smf.ols(formula, data=data).fit()

# --- Run models ---
m_main_top4 = run("membership ~ top4 + running_top4 + top4:running_top4", df_main_top4)
m_narrow_top4 = run("membership ~ top4 + running_top4 + top4:running_top4", df_narrow_top4)
m_wide_top4 = run("membership ~ top4 + running_top4 + top4:running_top4", df_wide_top4)

m_main_finals = run("membership ~ five_to_eight + running_finals + five_to_eight:running_finals", df_main_finals)
m_narrow_finals = run("membership ~ five_to_eight + running_finals + five_to_eight:running_finals", df_narrow_finals)
m_wide_finals = run("membership ~ five_to_eight + running_finals + five_to_eight:running_finals", df_wide_finals)

m_placebo = run("membership ~ placebo + running_placebo + placebo:running_placebo", df)

# --- Print results ---
print("\nTOP 4 CUTOFF")
print(m_main_top4.params["top4"], m_main_top4.bse["top4"])
print(m_narrow_top4.params["top4"], m_narrow_top4.bse["top4"])
print(m_wide_top4.params["top4"], m_wide_top4.bse["top4"])

print("\nFINALS CUTOFF")
print(m_main_finals.params["five_to_eight"], m_main_finals.bse["five_to_eight"])
print(m_narrow_finals.params["five_to_eight"], m_narrow_finals.bse["five_to_eight"])
print(m_wide_finals.params["five_to_eight"], m_wide_finals.bse["five_to_eight"])

print("\nPLACEBO")
print(m_placebo.params["placebo"], m_placebo.bse["placebo"])
