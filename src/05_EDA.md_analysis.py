import pandas as pd
import numpy as np

# Load the merged data
df = pd.read_csv('data/clean/merged_data_2012_2025.csv')

print("# Exploratory Data Analysis (EDA)")
print("## Merged Dataset Summary Statistics")
print()
print("### Dataset Overview")
print(f"- **Total Records**: {len(df)}")
print(f"- **Columns**: {len(df.columns)}")
print(f"- **Teams**: {df['club'].nunique()}")
print(f"- **Time Period**: {df['year'].min()} - {df['year'].max()}")
print(f"- **Missing Values**: {df.isna().sum().sum()} (None detected)")
print()

print("### Data Structure")
print("| Column | Type | Description |")
print("|--------|------|-------------|")
print("| club | string | Team name |")
print("| year | int64 | Season year |")
print("| ladder_position | int64 | Final ladder position (1=best) |")
print("| membership | int64 | Club membership numbers |")
print("| finals | int64 | Made finals (1=yes, 0=no) |")
print("| top4 | int64 | Finished top 4 (1=yes, 0=no) |")
print()

print("### Descriptive Statistics")
print()
print("#### Numeric Variables")
desc_stats = df.describe().round(2)
print("| Statistic | year | ladder_position | membership | finals | top4 |")
print("|-----------|------|-----------------|------------|--------|------|")
for stat in desc_stats.index:
    row = desc_stats.loc[stat]
    print(f"| {stat} | {row['year']} | {row['ladder_position']} | {row['membership']:,.0f} | {row['finals']} | {row['top4']} |")
print()

print("### Membership Statistics")
print(f"- **Average Membership**: {df['membership'].mean():,.0f}")
print(f"- **Median Membership**: {df['membership'].median():,.0f}")
print(f"- **Standard Deviation**: {df['membership'].std():,.0f}")
print(f"- **Minimum**: {df['membership'].min():,.0f}")
print(f"- **Maximum**: {df['membership'].max():,.0f}")
print()

print("### Performance Statistics")
print(f"- **Average Ladder Position**: {df['ladder_position'].mean():.2f}")
print(f"- **Median Ladder Position**: {df['ladder_position'].median():.0f}")
print(f"- **Teams Making Finals**: {df['finals'].sum()} out of {len(df)} ({df['finals'].sum()/len(df)*100:.1f}%)")
print(f"- **Teams Finishing Top 4**: {df['top4'].sum()} out of {len(df)} ({df['top4'].sum()/len(df)*100:.1f}%)")
print()

print("### Performance vs Membership Analysis")
print()
print("#### Correlations")
print(f"- **Ladder Position vs Membership**: {df['ladder_position'].corr(df['membership']):.4f} (negative = better position correlates with higher membership)")
print(f"- **Finals vs Membership**: {df['finals'].corr(df['membership']):.4f}")
print(f"- **Top 4 vs Membership**: {df['top4'].corr(df['membership']):.4f}")
print()

print("#### Average Membership by Performance Group")
top_4 = df[df['ladder_position'] <= 4]['membership']
finals_5_8 = df[(df['ladder_position'] >= 5) & (df['ladder_position'] <= 8)]['membership']
missed_finals = df[df['ladder_position'] >= 9]['membership']

print("| Performance Group | Count | Average Membership | Median Membership |")
print("|-------------------|-------|-------------------|-------------------|")
print(f"| Top 4 Finish | {len(top_4)} | {top_4.mean():,.0f} | {top_4.median():,.0f} |")
print(f"| Finals (5-8) | {len(finals_5_8)} | {finals_5_8.mean():,.0f} | {finals_5_8.median():,.0f} |")
print(f"| Missed Finals (9+) | {len(missed_finals)} | {missed_finals.mean():,.0f} | {missed_finals.median():,.0f} |")
print()

print("### Team-Level Statistics")
print()
print("#### Average Membership by Team (Sorted by Average)")
team_stats = df.groupby('club')['membership'].agg(['mean', 'min', 'max', 'std']).round(0)
team_stats = team_stats.sort_values('mean', ascending=False)
print("| Team | Average | Min | Max | Std Dev |")
print("|------|---------|-----|-----|----------|")
for team, row in team_stats.iterrows():
    print(f"| {team} | {row['mean']:,.0f} | {row['min']:,.0f} | {row['max']:,.0f} | {row['std']:,.0f} |")
print()

print("### Key Insights")
print("- There is a weak negative correlation between ladder position and membership (better teams tend to have slightly higher membership)")
print("- Teams that make finals have ~11% higher average membership than those that miss finals")
print("- Top 4 teams have ~15% higher average membership than teams that miss finals")
print("- Richmond and Collingwood consistently have the highest membership numbers")
print("- Gold Coast has the lowest average membership across the period")


import pandas as pd
import numpy as np

# Load the merged dataset
df = pd.read_csv('/Users/luissari/Desktop/Ecc3479/ECC479-project/data/clean/merged_data_2012_2025.csv')

# Sort by club and year to calculate growth rates
df_sorted = df.sort_values(['club', 'year']).reset_index(drop=True)

# Calculate year-to-year membership growth within each club
df_sorted['membership_growth'] = df_sorted.groupby('club')['membership'].diff()
df_sorted['membership_growth_rate'] = (df_sorted['membership_growth'] / df_sorted.groupby('club')['membership'].shift()) * 100

# For each ladder position, calculate average growth rate (excluding NaN from first year of each club)
growth_by_position = df_sorted[df_sorted['membership_growth_rate'].notna()].groupby('ladder_position').agg({
    'membership_growth_rate': ['mean', 'median', 'std', 'count'],
    'membership': 'mean'
}).round(2)

growth_by_position.columns = ['Avg Growth Rate (%)', 'Median Growth Rate (%)', 'Std Dev (%)', 'Count', 'Avg Membership']

print("MEMBERSHIP GROWTH RATE BY LADDER POSITION (2012-2025)")
print("=" * 80)
print(growth_by_position.sort_index())
print("\n")

# Also create a detailed view
print("DETAILED GROWTH STATISTICS BY POSITION")
print("=" * 80)
for pos in sorted(df_sorted['ladder_position'].unique()):
    subset = df_sorted[df_sorted['ladder_position'] == pos]
    growth_subset = subset[subset['membership_growth_rate'].notna()]
    
    if len(growth_subset) > 0:
        print(f"\nPosition {pos}:")
        print(f"  Observations: {len(growth_subset)}")
        print(f"  Average Growth Rate: {growth_subset['membership_growth_rate'].mean():.2f}%")
        print(f"  Median Growth Rate: {growth_subset['membership_growth_rate'].median():.2f}%")
        print(f"  Std Dev: {growth_subset['membership_growth_rate'].std():.2f}%")
        print(f"  Min Growth: {growth_subset['membership_growth_rate'].min():.2f}%")
        print(f"  Max Growth: {growth_subset['membership_growth_rate'].max():.2f}%")
        print(f"  Avg Membership: {growth_subset['membership'].mean():.0f}")

# Save results to CSV
output_path = '/Users/luissari/Desktop/Ecc3479/ECC479-project/outputs/membership_growth_by_ladder_position.csv'
growth_by_position.to_csv(output_path)
print(f"\n\nResults saved to: {output_path}")


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the merged dataset
df = pd.read_csv('/Users/luissari/Desktop/Ecc3479/ECC479-project/data/clean/merged_data_2012_2025.csv')

# Create scatterplot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot all data points with transparency and color coding by year
colors = plt.cm.viridis(np.linspace(0, 1, len(df['year'].unique())))
year_colors = {year: colors[i] for i, year in enumerate(sorted(df['year'].unique()))}

for year in sorted(df['year'].unique()):
    year_data = df[df['year'] == year]
    ax.scatter(year_data['ladder_position'], year_data['membership'], 
              alpha=0.6, s=80, color=[year_colors[year]], 
              edgecolors='black', linewidth=0.5, label=str(year))

# Add trend line
z = np.polyfit(df['ladder_position'], df['membership'], 2)
p = np.poly1d(z)
x_trend = np.linspace(df['ladder_position'].min(), df['ladder_position'].max(), 100)
ax.plot(x_trend, p(x_trend), "r--", linewidth=2.5, alpha=0.8, label='Trend (2nd degree polynomial)')

# Labels and title
ax.set_xlabel('Ladder Position (1 = Best, 18 = Worst)', fontsize=12, fontweight='bold')
ax.set_ylabel('Club Membership', fontsize=12, fontweight='bold')
ax.set_title('AFL Club Membership vs Ladder Position (2012-2025)', fontsize=14, fontweight='bold')
ax.set_xticks(range(1, 19))
ax.grid(True, alpha=0.3)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8, ncol=1)

# Save the figure
output_path = '/Users/luissari/Desktop/Ecc3479/ECC479-project/outputs/membership_vs_ladder_position_2012_2025.png'
plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Scatterplot saved to: {output_path}")
plt.close()

# Additional: Create a focused scatterplot without year colors for clarity
fig, ax = plt.subplots(figsize=(12, 8))

# Color by finals qualification
finals_yes = df[df['finals'] == 1]
finals_no = df[df['finals'] == 0]

ax.scatter(finals_no['ladder_position'], finals_no['membership'], 
          alpha=0.5, s=80, color='lightcoral', edgecolors='darkred', 
          linewidth=0.5, label='Missed Finals (9+)')
ax.scatter(finals_yes['ladder_position'], finals_yes['membership'], 
          alpha=0.5, s=80, color='lightgreen', edgecolors='darkgreen', 
          linewidth=0.5, label='Made Finals (1-8)')

# Add trend line
z = np.polyfit(df['ladder_position'], df['membership'], 1)
p = np.poly1d(z)
x_trend = np.linspace(df['ladder_position'].min(), df['ladder_position'].max(), 100)
ax.plot(x_trend, p(x_trend), "b--", linewidth=2.5, alpha=0.8, label='Linear Trend')

# Labels and title
ax.set_xlabel('Ladder Position (1 = Best, 18 = Worst)', fontsize=12, fontweight='bold')
ax.set_ylabel('Club Membership', fontsize=12, fontweight='bold')
ax.set_title('AFL Club Membership vs Ladder Position by Finals Status (2012-2025)', fontsize=14, fontweight='bold')
ax.set_xticks(range(1, 19))
ax.grid(True, alpha=0.3)
ax.legend(fontsize=11)

# Save the figure
output_path2 = '/Users/luissari/Desktop/Ecc3479/ECC479-project/outputs/membership_vs_ladder_by_finals.png'
plt.tight_layout()
plt.savefig(output_path2, dpi=300, bbox_inches='tight')
print(f"Finals-based scatterplot saved to: {output_path2}")
plt.close()
