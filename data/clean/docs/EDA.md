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
| Statistic | year | ladder_position | membership | finals | top4 |
|-----------|------|-----------------|------------|--------|------|
| count | 252.0 | 252.0 | 252 | 252.0 | 252.0 |
| mean | 2018.5 | 9.5 | 56,532 | 0.44 | 0.22 |
| std | 4.04 | 5.19 | 23,679 | 0.5 | 0.42 |
| min | 2012.0 | 1.0 | 10,241 | 0.0 | 0.0 |
| 25% | 2015.0 | 5.0 | 40,268 | 0.0 | 0.0 |
| 50% | 2018.5 | 9.5 | 54,872 | 0.0 | 0.0 |
| 75% | 2022.0 | 14.0 | 72,674 | 1.0 | 0.0 |
| max | 2025.0 | 18.0 | 112,491 | 1.0 | 1.0 |

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
| St Kilda | 46,558 | 30,739 | 65,509 | 12,016 |
| Western Bulldogs | 45,234 | 30,007 | 76,584 | 13,190 |
| North Melbourne | 43,527 | 33,423 | 56,731 | 6,652 |
| Brisbane | 35,546 | 20,762 | 75,138 | 17,383 |
| G.Western Sydney | 24,436 | 10,241 | 37,754 | 9,840 |
| Gold Coast | 16,989 | 11,204 | 30,107 | 6,080 |

### Key Insights
- There is a weak negative correlation between ladder position and membership (better teams tend to have slightly higher membership)
- Teams that make finals have ~11% higher average membership than those that miss finals
- Top 4 teams have ~15% higher average membership than teams that miss finals
- Richmond and Collingwood consistently have the highest membership numbers
- Gold Coast has the lowest average membership across the period
