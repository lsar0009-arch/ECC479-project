# ECC3479-project
Research Question: Does crossing the AFL finals qualification threshold — comparing clubs finishing 6th–8th versus 9th–10th — generate a measurably different impact on club membership tallies?

Economic Relevance

Membership is one of the main sources, if not the main source of revenue for AFL clubs.
Revenue for AFL teams directly contributes to;
- Financial stability
- Club operations
- Investment in facilities, staP, and players
If found to be true, it demonstrates how on-field performance translates to an economic payoff.




Empirical Strategy

This project estimates whether crossing the AFL finals qualification threshold causes a measurable change in club membership numbers by comparing teams that finish just inside the cutoff (6th–8th) with those that finish just outside it (9th–10th). 
Because clubs near the threshold are typically similar in underlying quality, resources, and supporter engagement, their relative position around the cutoff can be treated as quasi‑random. This creates a natural experiment:
- Treatment: qualifying for finals
- control: narrowly missing finals
 By analysing differences in subsequent membership tallies—using simple comparisons and regression‑based adjustments—we aim to isolate the causal impact of finals participation on fan behaviour and club revenue.




Key Variables:

1. Team
- Type: string (text)
- Description: Name of AFL club
- Values: 18 AFL clubs (Adeleaide, Brisbane, ...)
- Source: Manually transcribed from AFL.com.au ladder pages
- Notes: Team names match membership dataset exactly for merging

2. Year
- Type: integer
- Description: Season year corresponding to the ladder position
- Values: 2012–2025
- Source: AFL.com.au ladder pages
- Notes: No missing years in this range

Type: integer

3. Ladder Position
- Description: Final ladder position for the team in that year
- Values: 1–18
- Units: Rank (1 = highest, 18 = lowest)
- Source: AFL.com.au
- Notes: Lower number = better performance




REPOSITORY STRUCTURE

ECC3479-PROJECT/

.venv/                         

data/
- raw/                       
  - ladder_raw.csv
  - membership_1984-2024_website.csv
  - membership_2025_raw.csv

- clean/
  - docs
    - codebook.md
    - EDA.md
    - primary_econometric_analysis.md    
    - robustness_check.md                 
  - membership_clean.csv
  - merged_data_2012_2025.csv

                         
outputs/
- 5_8_vs_9_10_rdd.png
- 5_8_vs_9_10_summary.txt       
- finals_5_8_regression_plot.png
- finals_5_8_regression_summary.txt  
- full_regression_plot.png         
- full_regression_summary.txt
- membership_growth_rate_by_position.png
- membership_growth_rate_trend.png
- positions_9_10_regression_plot.png
- positions_9_10_regression_summary.txt
- positions_11_18_regression_plot.png
- positions_11_18_regression_summary.txt
- top4_regression_plot.png
- top4_regression_summary.txt
- top4_vs_5_8_rdd.png
- top4_vs_5_8_summary.txt


src/                           
- 01_import_afl_members.py
- 02_clean_memberships.py
- 03_merge_ladder_membership.py
- 04_EDA.md_analysis.py
- 05_regressions_visuals.py
README.md


## Software Requirements

This project uses Python and several scientific computing libraries.

**Python version**
- Python 3.14.3

**Required packages**
The full list of dependencies is stored in `requirements.txt`.  
Install them with:

pip install -r requirements.txt




How to Run the Project From Scratch

1. Place the raw data files into data/raw/:

- membership_r1984-2024_website.csv
- membership_2025_raw
- ladder_raw.csv

2. Install required Python packages.

3. Run the scripts in order.

- 01_import_afl_members.py
- 01_clean_memberships.py
- 03_merge_ladder_membership.py
- 04_EDA.md_analysis.py
- 05_regressions_visuals.py
- 06_discontinuous_1.py
- 07_discontinuous_2.py
- 08_robustness_check_clean.py

- Cleaned datasets will appear in data/clean/.

4. Final outputs

- cleaned datasets -> data/clean/
- Figures, tables, regression results -> outputs/




Scripts Descriptions

All scripts are located in the src/ folder.

01_import_afl_members.py
Imports historical membership data from https://footyindustry.com/html/AFL_Members.htm

02_clean_memberships.py
Cleans the raw membership data from years 2012 to 2025  and outputs a cleaned CSV to data/clean/.

03_merge_ladder_membership.py  
Merges the cleaned membership and ladder datasets into a single analysis‑ready file.

04_EDA.md_analysis.py
This script loads the merged dataset, computes summary statistics, checks distributions and correlations, and produces Markdown‑ready outputs for inclusion in the EDA report. It ensures that all descriptive analysis is fully reproducible and not done manually.

05_regressions_visuals.py
Runs all regression specifications and generates the associated visualisations.
This script loads the cleaned/merged data, estimates the OLS models for each ladder‑position band saves regression summaries to the outputs/ directory, and produces scatterplots and fitted‑line visuals for each specification.


06_discontinuous_1.py

Performs regression discontinuity design (RDD) analysis to estimate the causal effect of qualifying for the Top 4 (vs. 5-8) on club membership. It filters data to ladder positions 1-8, creates a treatment indicator for Top 4, centers the running variable at the cutoff (4.5), runs an OLS regression with interaction terms, prints the model summary and estimated discontinuity, and generates a scatter plot with fitted regression lines on both sides of the cutoff.


07_discontinuous_2.py

Conducts RDD analysis to assess the impact of qualifying for finals (5-8 vs. 9-10 positions) on membership. It filters data to positions 5-10, defines treatment for 5-8, centers the running variable at 8.5, fits an OLS model with interactions, outputs the regression summary and discontinuity estimate, and creates a plot showing the data scatter with fitted lines for each group.


08_robustness_check_clean.py

Runs robustness checks for the RDD analyses on Top 4 and finals cutoffs. It defines treatment and running variables, tests different bandwidths (main, narrow, wide) around each cutoff, includes a placebo test at position 6.5, fits multiple OLS models, and prints the estimated coefficients and standard errors for each specification to validate the main findings.


Raw Data Sources

Ladder data: manually transcribed from AFL.com.au into Excel, then exported to CSV (ladder_raw.csv) and placed in data/raw/

Membership data for 2012–2024 was manually copied from FootyIndustry.com (1984–2025 historical membership tables). Membership data for 2025 was taken directly from AFL.com.au due to more up‑to‑date reporting.These values were combined into a single raw CSV (membership_raw.csv) stored in data/raw/


