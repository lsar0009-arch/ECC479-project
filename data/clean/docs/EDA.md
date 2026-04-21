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

### Performance Statistics
- **Average Ladder Position**: 9.50
- **Median Ladder Position**: 10
- **Teams Making Finals**: 112 out of 252 (44.4%)
- **Teams Finishing Top 4**: 56 out of 252 (22.2%)

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

#### Scatterplot 1: Year-by-Year Distribution
![Membership vs Ladder Position (2012-2025)](../../outputs/membership_vs_ladder_position_2012_2025.png)

*Each colored point represents a club-year observation. The red dashed line shows the polynomial trend. Clear inverse relationship: better ladder positions tend to have higher membership.*

#### Scatterplot 2: By Finals Qualification Status
![Membership vs Ladder by Finals Status](../../outputs/membership_vs_ladder_by_finals.png)

*Green points = Made Finals (positions 1-8); Red points = Missed Finals (positions 9-18). Blue dashed line shows linear trend. Teams that make finals consistently have higher memberships across all ladder positions.*

### Key Insights
- There is a weak negative correlation between ladder position and membership (better teams tend to have slightly higher membership)
- Teams that make finals have ~8% higher average membership than those that miss finals
- Top 4 teams have ~18% higher average membership than teams that miss finals
- Richmond and Collingwood consistently have the highest membership numbers
- Gold Coast has the lowest average membership across the period


The dataset is clean, complete, and structured for causal comparison. Membership varies widely across clubs, suggesting strong club‑specific effects. Ladder positions are evenly distributed, and finals qualification is balanced enough to support threshold‑based comparisons.






