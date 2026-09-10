"""
Generate visualizations for Day 3 - EDA
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Load cleaned data
df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("Starting visualization generation...")
print(f"Dataset shape: {df.shape}")

# Create output directory
import os
os.makedirs('outputs/figures', exist_ok=True)

# 1. Overall unemployment trend over time
plt.figure(figsize=(14, 6))
df_avg = df.groupby('date')['estimated_unemployment_rate_pct'].mean().reset_index()
plt.plot(df_avg['date'], df_avg['estimated_unemployment_rate_pct'], linewidth=2, color='#2E86AB', marker='o', markersize=4)
plt.axvline(pd.to_datetime('2020-03-01'), color='red', linestyle='--', label='COVID Start', alpha=0.7)
plt.title('Unemployment Rate Trend Over Time (Jan 2019 - Nov 2020)', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/01_unemployment_trend_overall.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 01_unemployment_trend_overall.png")

# 2. State-wise average unemployment
plt.figure(figsize=(10, 6))
state_avg = df.groupby('region')['estimated_unemployment_rate_pct'].mean().sort_values(ascending=True)
colors = sns.color_palette('RdYlGn_r', len(state_avg))
state_avg.plot(kind='barh', color=colors)
plt.title('Average Unemployment Rate by State', fontsize=14, fontweight='bold')
plt.xlabel('Average Unemployment Rate (%)', fontsize=12)
plt.ylabel('State', fontsize=12)
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('outputs/figures/02_state_wise_unemployment.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 02_state_wise_unemployment.png")

# 3. Monthly unemployment pattern
plt.figure(figsize=(12, 6))
monthly_avg = df.groupby('month')['estimated_unemployment_rate_pct'].mean()
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.bar(range(1, 12), monthly_avg.values[:11], color='#A23B72', alpha=0.8, edgecolor='black')
plt.title('Average Unemployment Rate by Month', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Unemployment Rate (%)', fontsize=12)
plt.xticks(range(1, 12), month_names[:11])
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('outputs/figures/03_monthly_unemployment.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 03_monthly_unemployment.png")

# 4. Unemployment distribution
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(df['estimated_unemployment_rate_pct'], bins=30, color='#18A558', alpha=0.7, edgecolor='black')
plt.title('Unemployment Rate Distribution', fontsize=12, fontweight='bold')
plt.xlabel('Unemployment Rate (%)', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.boxplot(df['estimated_unemployment_rate_pct'], vert=True)
plt.title('Unemployment Rate Box Plot', fontsize=12, fontweight='bold')
plt.ylabel('Unemployment Rate (%)', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/04_unemployment_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 04_unemployment_distribution.png")

# 5. Rural vs Urban comparison
plt.figure(figsize=(12, 6))
area_data = df.groupby(['date', 'area'])['estimated_unemployment_rate_pct'].mean().unstack()
plt.plot(area_data.index, area_data['Rural'], label='Rural', linewidth=2, marker='o', markersize=4)
plt.plot(area_data.index, area_data['Urban'], label='Urban', linewidth=2, marker='s', markersize=4)
plt.axvline(pd.to_datetime('2020-03-01'), color='red', linestyle='--', alpha=0.5, label='COVID Start')
plt.title('Rural vs Urban Unemployment Trends', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/05_rural_vs_urban.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 05_rural_vs_urban.png")

# 6. Labour participation trend
plt.figure(figsize=(14, 6))
labour_avg = df.groupby('date')['estimated_labour_participation_rate_pct'].mean().reset_index()
plt.plot(labour_avg['date'], labour_avg['estimated_labour_participation_rate_pct'], linewidth=2, color='#F18F01', marker='o', markersize=4)
plt.axvline(pd.to_datetime('2020-03-01'), color='red', linestyle='--', label='COVID Start', alpha=0.7)
plt.title('Labour Participation Rate Trend Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Labour Participation Rate (%)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/06_labour_participation_trend.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 06_labour_participation_trend.png")

# 7. State comparison heatmap
plt.figure(figsize=(12, 8))
pivot_data = df.pivot_table(values='estimated_unemployment_rate_pct', index='region', columns='month', aggfunc='mean')
sns.heatmap(pivot_data, annot=True, fmt='.1f', cmap='YlOrRd', cbar_kws={'label': 'Unemployment Rate (%)'})
plt.title('State-wise Monthly Unemployment Heatmap', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('State', fontsize=12)
plt.tight_layout()
plt.savefig('outputs/figures/07_state_monthly_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("✓ Generated: 07_state_monthly_heatmap.png")

print("\n" + "="*60)
print("All visualizations generated successfully!")
print("Location: outputs/figures/")
print("="*60)
