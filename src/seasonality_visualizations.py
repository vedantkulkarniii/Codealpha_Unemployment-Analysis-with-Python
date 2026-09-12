"""
Seasonality Visualizations - Day 5
Creates comprehensive seasonality charts
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Load cleaned data
df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("Generating seasonality visualizations...")

# ============================================================================
# VISUALIZATION 20: Year-over-Year Monthly Comparison
# ============================================================================
print("Creating Visualization 20: Year-over-Year Monthly Comparison...")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Seasonality Analysis: Year-over-Year Comparison (2019 vs 2020)', 
             fontsize=16, fontweight='bold', y=0.995)

# Panel 1: Monthly comparison line chart
ax1 = axes[0, 0]
monthly_by_year = df.groupby(['year', 'month'])['estimated_unemployment_rate_pct'].mean().reset_index()
pivot_data = monthly_by_year.pivot(index='month', columns='year', values='estimated_unemployment_rate_pct')

month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax1.plot(range(1, 13), pivot_data[2019], marker='o', linewidth=2.5, markersize=8, 
         label='2019 (Pre-COVID)', color='#3498db')
ax1.plot(range(1, 12), pivot_data[2020][:11], marker='s', linewidth=2.5, markersize=8, 
         label='2020 (COVID)', color='#e74c3c')
ax1.set_xlabel('Month', fontsize=11, fontweight='bold')
ax1.set_ylabel('Unemployment Rate (%)', fontsize=11, fontweight='bold')
ax1.set_title('Monthly Unemployment: 2019 vs 2020', fontsize=12, fontweight='bold')
ax1.set_xticks(range(1, 13))
ax1.set_xticklabels(month_labels)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.axvspan(3, 11, alpha=0.1, color='red', label='COVID Period (Mar-Nov 2020)')

# Panel 2: Year-over-year change bars
ax2 = axes[0, 1]
yoy_change = pivot_data[2020][:11].values - pivot_data[2019][:11].values
colors = ['#27ae60' if x < 5 else '#f39c12' if x < 15 else '#e74c3c' for x in yoy_change]
bars = ax2.bar(range(1, 12), yoy_change, color=colors, edgecolor='black', linewidth=0.5)
ax2.set_xlabel('Month', fontsize=11, fontweight='bold')
ax2.set_ylabel('Change (percentage points)', fontsize=11, fontweight='bold')
ax2.set_title('Year-over-Year Change (2020 vs 2019)', fontsize=12, fontweight='bold')
ax2.set_xticks(range(1, 12))
ax2.set_xticklabels(month_labels[:11])
ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax2.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for i, (bar, val) in enumerate(zip(bars, yoy_change)):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'+{val:.1f}', ha='center', va='bottom', fontsize=8, fontweight='bold')

# Panel 3: 2019 Seasonal Pattern (Baseline)
ax3 = axes[1, 0]
df_2019 = df[df['year'] == 2019]
monthly_2019 = df_2019.groupby('month')['estimated_unemployment_rate_pct'].agg(['mean', 'std']).reset_index()
ax3.errorbar(monthly_2019['month'], monthly_2019['mean'], yerr=monthly_2019['std'],
             marker='o', linewidth=2.5, markersize=8, capsize=5, capthick=2,
             color='#3498db', ecolor='#3498db', label='2019 Mean ± Std Dev')
ax3.fill_between(monthly_2019['month'], 
                 monthly_2019['mean'] - monthly_2019['std'],
                 monthly_2019['mean'] + monthly_2019['std'],
                 alpha=0.2, color='#3498db')
ax3.set_xlabel('Month', fontsize=11, fontweight='bold')
ax3.set_ylabel('Unemployment Rate (%)', fontsize=11, fontweight='bold')
ax3.set_title('2019 Seasonal Pattern (Pre-COVID Baseline)', fontsize=12, fontweight='bold')
ax3.set_xticks(range(1, 13))
ax3.set_xticklabels(month_labels)
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)

# Panel 4: State-wise seasonality (2019)
ax4 = axes[1, 1]
states = df['region'].unique()
for state in states:
    state_2019 = df[(df['year'] == 2019) & (df['region'] == state)]
    monthly_state = state_2019.groupby('month')['estimated_unemployment_rate_pct'].mean()
    ax4.plot(monthly_state.index, monthly_state.values, marker='o', linewidth=2, 
             markersize=6, label=state, alpha=0.8)

ax4.set_xlabel('Month', fontsize=11, fontweight='bold')
ax4.set_ylabel('Unemployment Rate (%)', fontsize=11, fontweight='bold')
ax4.set_title('State-wise Seasonal Patterns (2019)', fontsize=12, fontweight='bold')
ax4.set_xticks(range(1, 13))
ax4.set_xticklabels(month_labels)
ax4.legend(fontsize=8, loc='best')
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/figures/20_seasonality_yoy_comparison.png', dpi=300, bbox_inches='tight')
print("  ✓ Saved: 20_seasonality_yoy_comparison.png")
plt.close()

# ============================================================================
# VISUALIZATION 21: Quarterly Analysis
# ============================================================================
print("Creating Visualization 21: Quarterly Analysis...")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Quarterly Unemployment Analysis', fontsize=16, fontweight='bold', y=0.995)

# Panel 1: Quarterly trends by year
ax1 = axes[0, 0]
quarterly = df.groupby(['year', 'quarter'])['estimated_unemployment_rate_pct'].mean().reset_index()
pivot_q = quarterly.pivot(index='quarter', columns='year', values='estimated_unemployment_rate_pct')
x_pos = np.arange(len(pivot_q.index))
width = 0.35
bars1 = ax1.bar(x_pos - width/2, pivot_q[2019], width, label='2019', 
                color='#3498db', edgecolor='black', linewidth=0.5)
bars2 = ax1.bar(x_pos + width/2, pivot_q[2020], width, label='2020', 
                color='#e74c3c', edgecolor='black', linewidth=0.5)
ax1.set_xlabel('Quarter', fontsize=11, fontweight='bold')
ax1.set_ylabel('Unemployment Rate (%)', fontsize=11, fontweight='bold')
ax1.set_title('Quarterly Unemployment: 2019 vs 2020', fontsize=12, fontweight='bold')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=9)

# Panel 2: Quarterly change
ax2 = axes[0, 1]
q_change = pivot_q[2020].values - pivot_q[2019].values
colors_q = ['#27ae60' if x < 5 else '#f39c12' if x < 10 else '#e74c3c' for x in q_change]
bars_q = ax2.bar(range(1, 5), q_change, color=colors_q, edgecolor='black', linewidth=0.5)
ax2.set_xlabel('Quarter', fontsize=11, fontweight='bold')
ax2.set_ylabel('Change (percentage points)', fontsize=11, fontweight='bold')
ax2.set_title('Year-over-Year Quarterly Change', fontsize=12, fontweight='bold')
ax2.set_xticks(range(1, 5))
ax2.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
ax2.grid(True, alpha=0.3, axis='y')

for bar, val in zip(bars_q, q_change):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             f'+{val:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Panel 3: State-wise quarterly patterns (2019)
ax3 = axes[1, 0]
for state in states:
    state_q = df[(df['year'] == 2019) & (df['region'] == state)]
    quarterly_state = state_q.groupby('quarter')['estimated_unemployment_rate_pct'].mean()
    ax3.plot(quarterly_state.index, quarterly_state.values, marker='o', 
             linewidth=2.5, markersize=8, label=state, alpha=0.8)

ax3.set_xlabel('Quarter', fontsize=11, fontweight='bold')
ax3.set_ylabel('Unemployment Rate (%)', fontsize=11, fontweight='bold')
ax3.set_title('State-wise Quarterly Pattern (2019)', fontsize=12, fontweight='bold')
ax3.set_xticks(range(1, 5))
ax3.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel 4: Rural vs Urban quarterly
ax4 = axes[1, 1]
for area in ['Rural', 'Urban']:
    for year in [2019, 2020]:
        area_year = df[(df['area'] == area) & (df['year'] == year)]
        quarterly_area = area_year.groupby('quarter')['estimated_unemployment_rate_pct'].mean()
        linestyle = '-' if year == 2019 else '--'
        marker = 'o' if area == 'Rural' else 's'
        label = f'{area} {year}'
        ax4.plot(quarterly_area.index, quarterly_area.values, marker=marker,
                linewidth=2, markersize=7, label=label, linestyle=linestyle, alpha=0.8)

ax4.set_xlabel('Quarter', fontsize=11, fontweight='bold')
ax4.set_ylabel('Unemployment Rate (%)', fontsize=11, fontweight='bold')
ax4.set_title('Rural vs Urban Quarterly Trends', fontsize=12, fontweight='bold')
ax4.set_xticks(range(1, 5))
ax4.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
ax4.legend(fontsize=9, ncol=2)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/figures/21_quarterly_analysis.png', dpi=300, bbox_inches='tight')
print("  ✓ Saved: 21_quarterly_analysis.png")
plt.close()

# ============================================================================
# VISUALIZATION 22: Seasonal Disruption Heatmap
# ============================================================================
print("Creating Visualization 22: Seasonal Disruption Heatmap...")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Seasonal Pattern Disruption Analysis', fontsize=16, fontweight='bold')

# Panel 1: State-Month heatmap for 2019 (baseline)
ax1 = axes[0]
pivot_2019 = df[df['year'] == 2019].pivot_table(
    values='estimated_unemployment_rate_pct',
    index='region',
    columns='month',
    aggfunc='mean'
)
sns.heatmap(pivot_2019, annot=True, fmt='.1f', cmap='YlOrRd', ax=ax1,
            cbar_kws={'label': 'Unemployment Rate (%)'}, linewidths=0.5)
ax1.set_title('2019 Baseline Seasonal Pattern', fontsize=12, fontweight='bold')
ax1.set_xlabel('Month', fontsize=11, fontweight='bold')
ax1.set_ylabel('State', fontsize=11, fontweight='bold')
ax1.set_xticklabels(month_labels)

# Panel 2: Disruption magnitude (2020 vs 2019 difference)
ax2 = axes[1]
pivot_2020 = df[df['year'] == 2020].pivot_table(
    values='estimated_unemployment_rate_pct',
    index='region',
    columns='month',
    aggfunc='mean'
)
disruption = pivot_2020 - pivot_2019.iloc[:, :11]  # Only use first 11 months
sns.heatmap(disruption, annot=True, fmt='.1f', cmap='Reds', ax=ax2,
            cbar_kws={'label': 'Change (pp)'}, linewidths=0.5)
ax2.set_title('2020 Disruption from Baseline (pp change)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Month', fontsize=11, fontweight='bold')
ax2.set_ylabel('State', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('outputs/figures/22_seasonal_disruption_heatmap.png', dpi=300, bbox_inches='tight')
print("  ✓ Saved: 22_seasonal_disruption_heatmap.png")
plt.close()

print("\n✓ All seasonality visualizations created successfully!")
print("  Total: 3 visualizations (Viz 20-22)")
