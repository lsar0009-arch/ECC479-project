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
