"""
COVID Recovery Pattern Analysis
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("="*80)
print("COVID-19 RECOVERY PATTERN ANALYSIS")
print("="*80)

covid = df[df['covid_period'] == 'COVID'].copy()
covid_monthly = covid.groupby(covid['date'].dt.to_period('M'))['estimated_unemployment_rate_pct'].mean()

print("\n1. RECOVERY TIMELINE")
print("-"*80)
peak_month = covid_monthly.idxmax()
peak_value = covid_monthly.max()
print(f"Peak: {peak_month} at {peak_value:.2f}%")

print("\nMonth-by-Month Recovery:")
for i, (month, value) in enumerate(covid_monthly.items()):
    if i > 0:
        prev_value = covid_monthly.iloc[i-1]
        change = value - prev_value
        print(f"{month}: {value:.2f}% ({change:+.2f} pp from previous month)")
    else:
        print(f"{month}: {value:.2f}% (Initial COVID month)")

# Calculate recovery metrics
print("\n2. RECOVERY METRICS")
print("-"*80)
latest_value = covid_monthly.iloc[-1]
recovery_from_peak = peak_value - latest_value
recovery_pct = (recovery_from_peak / peak_value) * 100

print(f"Peak Unemployment: {peak_value:.2f}%")
print(f"Latest Unemployment: {latest_value:.2f}%")
print(f"Total Recovery: {recovery_from_peak:.2f} pp")
print(f"Recovery Percentage: {recovery_pct:.1f}% of peak")
print(f"Remaining Gap from Peak: {latest_value:.2f}%")

# State recovery comparison
print("\n3. STATE-WISE RECOVERY COMPARISON")
print("-"*80)
print(f"{'State':<20} {'Peak':<10} {'Latest':<10} {'Recovery':<12}")
print("-"*80)

for state in sorted(df['region'].unique()):
    state_covid = covid[covid['region'] == state]
    state_monthly = state_covid.groupby(state_covid['date'].dt.to_period('M'))['estimated_unemployment_rate_pct'].mean()
    
    if len(state_monthly) > 0:
        state_peak = state_monthly.max()
        state_latest = state_monthly.iloc[-1]
        state_recovery = state_peak - state_latest
        state_recovery_pct = (state_recovery / state_peak) * 100
        
        print(f"{state:<20} {state_peak:>8.2f}%  {state_latest:>8.2f}%  {state_recovery_pct:>10.1f}%")

# Recovery speed
print("\n4. RECOVERY SPEED ANALYSIS")
print("-"*80)
peak_idx = covid_monthly.values.argmax()
post_peak = covid_monthly.iloc[peak_idx:]

if len(post_peak) > 1:
    months_elapsed = len(post_peak) - 1
    total_decline = post_peak.iloc[0] - post_peak.iloc[-1]
    avg_monthly_decline = total_decline / months_elapsed
    
    print(f"Months Since Peak: {months_elapsed}")
    print(f"Total Decline: {total_decline:.2f} pp")
    print(f"Average Monthly Decline: {avg_monthly_decline:.2f} pp/month")

# Create recovery visualization
plt.figure(figsize=(12, 6))
months = [str(m) for m in covid_monthly.index]
values = covid_monthly.values

plt.plot(range(len(values)), values, marker='o', linewidth=2, markersize=8, color='#E63946')
plt.fill_between(range(len(values)), values, alpha=0.3, color='#E63946')

# Mark peak
peak_idx = values.argmax()
plt.scatter([peak_idx], [values[peak_idx]], color='red', s=200, zorder=5, edgecolor='black', linewidth=2)
plt.annotate(f'Peak: {values[peak_idx]:.2f}%', 
             xy=(peak_idx, values[peak_idx]), 
             xytext=(peak_idx-0.5, values[peak_idx]+2),
             fontsize=11, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))

plt.xticks(range(len(months)), months, rotation=45)
plt.title('COVID-19 Recovery Pattern (March-November 2020)', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Average Unemployment Rate (%)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/17_covid_recovery_pattern.png', dpi=300, bbox_inches='tight')
plt.close()
print("\n✓ Visualization saved: 17_covid_recovery_pattern.png")

print("\n" + "="*80)
print("RECOVERY ANALYSIS COMPLETE")
print("="*80)
