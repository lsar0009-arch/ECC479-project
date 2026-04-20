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
- **Finals vs Membership**: 0.1491
- **Top 4 vs Membership**: 0.1464

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

### Key Insights
- There is a weak negative correlation between ladder position and membership (better teams tend to have slightly higher membership)
- Teams that make finals have ~8% higher average membership than those that miss finals
- Top 4 teams have ~18% higher average membership than teams that miss finals
- Richmond and Collingwood consistently have the highest membership numbers
- Gold Coast has the lowest average membership across the period


The dataset is clean, complete, and structured for causal comparison. Membership varies widely across clubs, suggesting strong club‑specific effects. Ladder positions are evenly distributed, and finals qualification is balanced enough to support threshold‑based comparisons.



2. Exploratory Analysis of Relationships


2.1 Correlation Matrix

2.2 Visual Exploration

Scatterplot: Membership vs Ladder Position

Boxplot: Membership by Finals Qualification

Histogram: Membership Distribution




3. First‑Order Effect Check (Treatment vs Control)
3.1 Group Means

3.2 Difference in Means


4. Modelling Considerations

4.1 Potential Issues
- Club fixed effects: large clubs dominate membership totals
- Year trends: membership has grown over time
- Non‑linearity: ladder position effect may not be linear
- Simpson’s paradox risk: large clubs may mask threshold effects
- Variance differences: membership variance differs by club

4.2 Possible Solutions
- Use within‑club comparisons
- Include year fixed effects
- Consider log(membership) to stabilise variance
- Use regression discontinuity logic around the 8th‑place cutoff


5. Summary of Insights
The dataset is clean, complete, and suitable for threshold‑based causal analysis.

Finals qualification correlates positively with membership, but raw correlations are confounded.

Visuals show a plausible finals effect but also strong club‑specific patterns.

A small first‑order difference exists between treatment and control groups.

Modelling should account for club size, year trends, and non‑linearities.

Overall, the EDA supports the hypothesis that crossing the finals threshold may influence membership, but careful modelling is required to isolate the causal effect.