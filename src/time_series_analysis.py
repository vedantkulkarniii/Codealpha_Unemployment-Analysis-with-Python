"""
Time Series Analysis - Trends and Patterns
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("="*70)
print("TIME SERIES ANALYSIS")
print("="*70)

# Daily average
daily_avg = df.groupby('date').agg({
    'estimated_unemployment_rate_pct': 'mean',
    'estimated_labour_participation_rate_pct': 'mean'
}).reset_index()

# Calculate moving averages
daily_avg['MA_3month'] = daily_avg['estimated_unemployment_rate_pct'].rolling(window=3).mean()

print("\n1. UNEMPLOYMENT RATE OVER TIME")
print("-"*70)
print(daily_avg[['date', 'estimated_unemployment_rate_pct', 'MA_3month']].tail(10))

# Find key turning points
print("\n2. KEY TURNING POINTS")
print("-"*70)

# Minimum point
min_idx = daily_avg['estimated_unemployment_rate_pct'].idxmin()
print(f"\nLowest Point:")
print(f"  Date: {daily_avg.loc[min_idx, 'date'].strftime('%B %Y')}")
print(f"  Rate: {daily_avg.loc[min_idx, 'estimated_unemployment_rate_pct']:.2f}%")

# Maximum point
max_idx = daily_avg['estimated_unemployment_rate_pct'].idxmax()
print(f"\nHighest Point:")
print(f"  Date: {daily_avg.loc[max_idx, 'date'].strftime('%B %Y')}")
print(f"  Rate: {daily_avg.loc[max_idx, 'estimated_unemployment_rate_pct']:.2f}%")

# Create comprehensive time series plot
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Plot 1: Unemployment with moving average
axes[0].plot(daily_avg['date'], daily_avg['estimated_unemployment_rate_pct'], 
             label='Monthly Average', color='#2E86AB', linewidth=2, marker='o', markersize=5)
axes[0].plot(daily_avg['date'], daily_avg['MA_3month'], 
             label='3-Month Moving Average', color='#A23B72', linewidth=2, linestyle='--')
axes[0].axvline(pd.to_datetime('2020-03-01'), color='red', linestyle='--', 
                alpha=0.7, linewidth=2, label='COVID Start')
axes[0].axhline(daily_avg['estimated_unemployment_rate_pct'].mean(), 
                color='green', linestyle=':', alpha=0.5, label='Overall Mean')
axes[0].set_title('Unemployment Rate Time Series with Moving Average', 
                  fontsize=14, fontweight='bold')
axes[0].set_xlabel('Date', fontsize=12)
axes[0].set_ylabel('Unemployment Rate (%)', fontsize=12)
axes[0].legend(loc='upper left')
axes[0].grid(True, alpha=0.3)

# Plot 2: Labour participation
axes[1].plot(daily_avg['date'], daily_avg['estimated_labour_participation_rate_pct'], 
             color='#F18F01', linewidth=2, marker='s', markersize=5)
axes[1].axvline(pd.to_datetime('2020-03-01'), color='red', linestyle='--', 
                alpha=0.7, linewidth=2, label='COVID Start')
axes[1].set_title('Labour Participation Rate Over Time', 
                  fontsize=14, fontweight='bold')
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('Labour Participation Rate (%)', fontsize=12)
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/figures/10_time_series_analysis.png', dpi=300, bbox_inches='tight')
plt.close()
print("\n✓ Visualization saved: 10_time_series_analysis.png")

# Growth rates
print("\n3. MONTH-TO-MONTH CHANGES")
print("-"*70)
daily_avg['change'] = daily_avg['estimated_unemployment_rate_pct'].diff()
daily_avg['pct_change'] = daily_avg['estimated_unemployment_rate_pct'].pct_change() * 100

print("\nLargest Increases:")
increases = daily_avg.nlargest(3, 'change')[['date', 'estimated_unemployment_rate_pct', 'change']]
for _, row in increases.iterrows():
    print(f"  {row['date'].strftime('%b %Y')}: +{row['change']:.2f} pp (to {row['estimated_unemployment_rate_pct']:.2f}%)")

print("\nLargest Decreases:")
decreases = daily_avg.nsmallest(3, 'change')[['date', 'estimated_unemployment_rate_pct', 'change']]
for _, row in decreases.iterrows():
    print(f"  {row['date'].strftime('%b %Y')}: {row['change']:.2f} pp (to {row['estimated_unemployment_rate_pct']:.2f}%)")

print("\n" + "="*70)
