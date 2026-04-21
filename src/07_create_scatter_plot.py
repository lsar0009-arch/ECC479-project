import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the merged dataset
df = pd.read_csv('/Users/luissari/Desktop/Ecc3479/ECC479-project/data/clean/merged_data_2012_2025.csv')

# Sort by club and year to calculate growth rates
df_sorted = df.sort_values(['club', 'year']).reset_index(drop=True)

# Calculate year-to-year membership growth within each club
df_sorted['membership_growth'] = df_sorted.groupby('club')['membership'].diff()
df_sorted['membership_growth_rate'] = (df_sorted['membership_growth'] / df_sorted.groupby('club')['membership'].shift()) * 100

# Remove NaN values from first year of each club
df_growth = df_sorted[df_sorted['membership_growth_rate'].notna()].copy()

# Create scatter plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot all data points with transparency
ax.scatter(df_growth['ladder_position'], df_growth['membership_growth_rate'], 
          alpha=0.4, s=60, color='steelblue', edgecolors='navy', linewidth=0.5)

# Add mean growth rate line for each position
position_means = df_growth.groupby('ladder_position')['membership_growth_rate'].mean()
ax.plot(position_means.index, position_means.values, 
        marker='o', linestyle='-', linewidth=2.5, markersize=8, 
        color='red', label='Mean Growth Rate by Position')

# Add horizontal line at 0% growth
ax.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.7)

# Labels and title
ax.set_xlabel('Ladder Position (1 = Best, 18 = Worst)', fontsize=12, fontweight='bold')
ax.set_ylabel('Membership Growth Rate (%)', fontsize=12, fontweight='bold')
ax.set_title('Membership Growth Rate by Ladder Position (2012-2025)', fontsize=14, fontweight='bold')
ax.set_xticks(range(1, 19))
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10)

# Save the figure
output_path = '/Users/luissari/Desktop/Ecc3479/ECC479-project/outputs/membership_growth_by_position_scatter.png'
plt.tight_layout()
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Scatter plot saved to: {output_path}")
plt.close()
