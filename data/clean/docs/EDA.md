1. Data Overview
1.1 Dataset Description

The merged dataset contains AFL club‑year observations from 2012–2025, combining:
- Ladder data (final finishing positions)
- Membership data (annual club membership totals)
- Derived variables (finals qualification, treatment/control groups)
Each row represents a club in a given season.


1.2 Dimensions

- Rows: 18 clubs × 14 seasons = 252 observations (minus any missing years)
- Columns: depends on your final merged dataset, typically 6–10 variables

1.3 Variables Included
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

# Exploratory Data Analysis (EDA)
## Merged Dataset Summary Statistics

### Dataset Overview
- **Total Records**: 252
- **Columns**: 6
- **Teams**: 18
- **Time Period**: 2012 - 2025
- **Missing Values**: 0 (None detected)

### Data Structure
| Column | Type | Description |
|--------|------|-------------|
| club | string | Team name |
| year | int64 | Season year |
| ladder_position | int64 | Final ladder position (1=best) |
| membership | int64 | Club membership numbers |
| finals | int64 | Made finals (1=yes, 0=no) |
| top4 | int64 | Finished top 4 (1=yes, 0=no) |

The dataset is clean, complete, and structured for causal comparison. Membership varies widely across clubs, suggesting strong club‑specific effects. Ladder positions are evenly distributed, and finals qualification is balanced enough to support threshold‑based comparisons.

### Descriptive Statistics

#### Numeric Variables
| Statistic | membership |
|-----------|------------|
| count | 252 |
| mean | 56,532 |
| std | 23,679 |
| min | 10,241 |
| 25% | 40,268 |
| 50% | 54,872 |
| 75% | 72,674 |
| max | 112,491 |

### Membership Statistics
- **Average Membership**: 56,532
- **Median Membership**: 54,872
- **Standard Deviation**: 23,679
- **Minimum**: 10,241
- **Maximum**: 112,491

Membership varies widely across clubs, with a spread of over 100k between smallest and largest clubs. This indicates strong club‑specific effects that must be accounted for in modelling (e.g., fixed effects or differencing).

### Performance Statistics
- **Average Ladder Position**: 9.50
- **Median Ladder Position**: 10
- **Teams Making Finals**: 112 out of 252 (44.4%)
- **Teams Finishing Top 4**: 56 out of 252 (22.2%)

Performance is evenly distributed across the ladder, with a natural split between finals and non‑finals teams. This supports threshold‑based comparisons (e.g., regression discontinuity around 8th place).

### Performance vs Membership Analysis

#### Correlations
- **Ladder Position vs Membership**: -0.2104 (negative = better position correlates with higher membership)
- **Finals vs Membership**: 0.1491 (This is a weak positive correlation indicating that clubs which make finals (positions 1-8) tend to have slightly higher membership than those that miss finals. However, the correlation is small (around 0.15), so it's not a strong relationship. Essentially, making finals is weakly associated with having more members, but many other factors influence membership.)
- **Top 4 vs Membership**: 0.1464 (Similar weak positive correlation for teams finishing in the top 4. These clubs have modestly higher membership on average, but again, it's a weak effect)

#### Average Membership by Performance Group
| Performance Group | Count | Average Membership | Median Membership |
|-------------------|-------|-------------------|-------------------|
| Top 4 Finish | 56 | 63,002 | 62,097 |
| Finals (5-8) | 56 | 57,938 | 55,206 |
| Missed Finals (9+) | 140 | 53,381 | 51,920 |

### Team-Level Statistics

#### Average Membership by Team (Sorted by Average)
| Team | Average | Min | Max | Std Dev |
|------|---------|-----|-----|----------|
| Richmond | 86,627 | 53,027 | 107,331 | 19,392 |
| Collingwood | 86,151 | 72,688 | 112,491 | 14,599 |
| West Coast | 82,779 | 57,377 | 106,422 | 20,968 |
| Hawthorn | 76,067 | 60,841 | 87,204 | 7,543 |
| Essendon | 71,714 | 47,708 | 86,274 | 13,494 |
| Carlton | 67,929 | 45,440 | 106,345 | 22,097 |
| Geelong | 62,367 | 40,205 | 92,379 | 17,556 |
| Adelaide | 60,198 | 46,005 | 81,067 | 10,137 |
| Fremantle | 54,695 | 42,918 | 86,179 | 10,618 |
| Sydney | 54,683 | 29,873 | 78,671 | 13,657 |
| Port Adelaide | 53,952 | 35,543 | 72,656 | 9,795 |
| Melbourne | 48,118 | 33,177 | 70,785 | 12,929 |
| St Kilda | 46,558 | 30,007 | 65,509 | 10,033 |
| Western Bulldogs | 45,234 | 30,007 | 76,584 | 13,190 |
| North Melbourne | 43,527 | 30,007 | 67,731 | 11,033 |
| Brisbane | 35,546 | 20,762 | 75,138 | 17,383 |
| G.Western Sydney | 24,436 | 10,241 | 43,527 | 9,033 |
| Gold Coast | 16,989 | 11,204 | 30,107 | 6,080 |

### Membership Growth Rate by Ladder Position (2012-2025)
| Ladder Position | Avg Growth Rate (%) | Median Growth Rate (%) | Std Dev (%) | Observations | Avg Membership |
|---|---|---|---|---|---|
| 1 | 10.07 | 6.06 | 12.68 | 13 | 66,718 |
| 2 | 12.18 | 8.47 | 9.02 | 13 | 57,758 |
| 3 | 6.22 | 3.33 | 6.73 | 13 | 72,624 |
| 4 | 14.97 | 12.87 | 12.91 | 13 | 58,185 |
| 5 | 9.97 | 11.42 | 7.26 | 13 | 63,152 |
| 6 | 10.82 | 8.25 | 9.73 | 13 | 55,261 |
| 7 | 5.56 | 3.87 | 9.68 | 13 | 49,773 |
| 8 | 8.66 | 9.62 | 8.14 | 13 | 68,014 |
| 9 | 6.45 | 7.89 | 11.11 | 13 | 65,406 |
| 10 | 6.34 | 4.33 | 7.39 | 13 | 53,628 |
| 11 | 3.06 | 1.17 | 6.12 | 13 | 62,376 |
| 12 | 5.66 | 4.64 | 6.60 | 13 | 58,151 |
| 13 | 0.90 | 1.66 | 10.59 | 13 | 62,647 |
| 14 | 4.45 | 5.29 | 8.82 | 14 | 46,010 |
| 15 | 1.37 | 1.14 | 6.54 | 12 | 53,094 |
| 16 | 3.06 | 1.22 | 10.63 | 13 | 47,192 |
| 17 | 1.48 | 3.72 | 8.47 | 13 | 48,239 |
| 18 | 3.03 | 0.37 | 11.34 | 13 | 53,686 |


### Membership vs Ladder Position Visualizations

#### Regression 1: Membership vs Ladder Position (2012-2025)
- outputs/full_regression_plot.png

#### Regression 2: Membership Growth Rate by Ladder Position (Top 4)
- outputs/top_4_regression_plot.png

#### Regression 3: Membership Growth Rate by Ladder Position (5-8)
- outputs/finals_5_8_regression_plot.png

#### Regression 3: Membership Growth Rate by Ladder Position (9-10)
- outputs/finals_9_10_regression_plot.png

#### Regression 4: Membership Growth Rate by Ladder Position (11-18)
- outputs/finals_11_18_regression_plot.png

#### Bar Chart 1: Membership Growth Rate by Ladder Position
- outputs/membership_growth_rate_by_position.png

### Key Regression Insights

1. Top 4
The regression shows no significant relationship between ladder position and membership within the top 4 teams. The coefficient of -858 indicates that membership decreases by about 858 for each position drop from 1st to 4th, but this effect is not statistically significant (p=0.77).

2. Ladder Positions 5-8
Within positions 5-8, there's virtually no relationship between ladder position and membership. The positive coefficient of 351 suggests membership increases slightly by 351 when moving from 5th to 8th place, but this is not statistically significant (p=0.89).

3. Ladder Positions 9-10 (just missing out on finals)
Teams finishing 9th tend to have higher membership than those finishing 10th. The coefficient of -10,223 indicates membership decreases by about 10,223 when dropping from 9th to 10th place, though this difference is not statistically significant (p=0.19).

4. Ladder Positions 11-18
Among lower-performing teams, membership decreases as ladder position worsens. The coefficient of -2,018 shows membership falls by about 2,018 for each position drop from 11th to 18th, with marginal statistical significance (p=0.08).

5. Full data set 
Across all ladder positions, better performance correlates with higher membership. The coefficient of -959 indicates membership decreases by about 959 for each worse ladder position, representing a statistically significant relationship (p<0.001).

6. Discointinuous Regression (Top 4 to 5-8) - TBC

7. Discointinuous Regression (5-8 to 9-10) - TBC



### Overall Key Insights
- There is a weak negative correlation between ladder position and membership (better teams tend to have slightly higher membership)
- Finals teams have modestly higher membership (~8% higher on average). This is a weak first‑order effect, indicating that making finals matters, but not dramatically.
- Top 4 teams have ~18% higher average membership than teams that miss finals
- A weak negative relationship: better ladder position is associated with slightly higher membership. The effect is small, suggesting performance is not the dominant driver of membership.
- Growth is highest for positions 2, 4, 6 (8–15%) and is lowest for positions 13–17 (0–4%)

Teams differ substantially in scale:
- Richmond, Collingwood, West Coast: 80k–110k
- Brisbane, North Melbourne, St Kilda: 30k–50k
- Gold Coast: consistently lowest

Therefore, club identity is a major determinant of membership levels








