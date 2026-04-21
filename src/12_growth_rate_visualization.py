import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load the merged dataset
df = pd.read_csv('/Users/luissari/Desktop/Ecc3479/ECC479-project/data/clean/merged_data_2012_2025.csv')

# Sort by club and year to calculate growth rates
df_sorted = df.sort_values(['club', 'year']).reset_index(drop=True)

# Calculate year-to-year membership growth within each club
df_sorted['membership_growth'] = df_sorted.groupby('club')['membership'].diff()
df_sorted['membership_growth_rate'] = (df_sorted['membership_growth'] / df_sorted.groupby('club')['membership'].shift()) * 100

# Calculate average growth rate by ladder position (excluding NaN from first year of each club)
growth_by_position = df_sorted[df_sorted['membership_growth_rate'].notna()].groupby('ladder_position').agg({
    'membership_growth_rate': ['mean', 'median', 'std', 'count']
}).round(2)

growth_by_position.columns = ['Avg Growth Rate (%)', 'Median Growth Rate (%)', 'Std Dev (%)', 'Count']

# Create output directory
output_dir = '/Users/luissari/Desktop/Ecc3479/ECC479-project/outputs'
os.makedirs(output_dir, exist_ok=True)

# Create bar chart of average growth rates by ladder position
fig, ax = plt.subplots(figsize=(14, 8))

positions = growth_by_position.index
avg_growth = growth_by_position['Avg Growth Rate (%)']
std_dev = growth_by_position['Std Dev (%)']

# Color bars: positive growth in green, negative in red
colors = ['green' if x >= 0 else 'red' for x in avg_growth]

bars = ax.bar(positions, avg_growth, color=colors, alpha=0.7, edgecolor='black', linewidth=0.5)

# Add error bars for standard deviation
ax.errorbar(positions, avg_growth, yerr=std_dev, fmt='none', ecolor='black', capsize=3, alpha=0.6)

# Add horizontal line at 0%
ax.axhline(y=0, color='black', linestyle='-', linewidth=1, alpha=0.8)

# Labels and title
ax.set_xlabel('Ladder Position (1 = Best, 18 = Worst)', fontsize=12, fontweight='bold')
ax.set_ylabel('Average Membership Growth Rate (%)', fontsize=12, fontweight='bold')
ax.set_title('Average Membership Growth Rate by Ladder Position (2012-2025)', fontsize=14, fontweight='bold')
ax.set_xticks(range(1, 19))

# Add value labels on bars
for bar, rate in zip(bars, avg_growth):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + (1 if height >= 0 else -1),
            f'{rate:.1f}%', ha='center', va='bottom' if height >= 0 else 'top',
            fontsize=9, fontweight='bold')

ax.grid(True, alpha=0.3, axis='y')

# Add legend
legend_elements = [plt.Rectangle((0,0),1,1, facecolor='green', alpha=0.7, label='Positive Growth'),
                   plt.Rectangle((0,0),1,1, facecolor='red', alpha=0.7, label='Negative Growth')]
ax.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()

# Save the figure
output_path = os.path.join(output_dir, 'membership_growth_rate_by_position.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Growth rate visualization saved to: {output_path}")
plt.close()

# Also create a line plot for trend visualization
fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(positions, avg_growth, marker='o', linestyle='-', linewidth=2, markersize=8,
        color='blue', markerfacecolor='white', markeredgecolor='blue', markeredgewidth=2)

# Add error bars
ax.fill_between(positions, avg_growth - std_dev, avg_growth + std_dev,
                alpha=0.2, color='blue', label='±1 Std Dev')

ax.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.8)

ax.set_xlabel('Ladder Position (1 = Best, 18 = Worst)', fontsize=12, fontweight='bold')
ax.set_ylabel('Average Membership Growth Rate (%)', fontsize=12, fontweight='bold')
ax.set_title('Membership Growth Rate Trend by Ladder Position (2012-2025)', fontsize=14, fontweight='bold')
ax.set_xticks(range(1, 19))
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()

# Save the line plot
output_path2 = os.path.join(output_dir, 'membership_growth_rate_trend.png')
plt.savefig(output_path2, dpi=300, bbox_inches='tight')
print(f"Growth rate trend plot saved to: {output_path2}")
plt.close()

print("\nGrowth Rate Summary by Position:")
print(growth_by_position)
