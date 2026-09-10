"""
COVID-19 Impact Analysis - Comprehensive Assessment
Day 4
"""
import pandas as pd
import numpy as np

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("="*80)
print("COVID-19 IMPACT ANALYSIS - COMPREHENSIVE ASSESSMENT")
print("="*80)

# Period definitions
print("\n1. COVID PERIOD DEFINITIONS")
print("-"*80)
print("Pre-COVID:  Before March 1, 2020")
print("COVID:      March 1, 2020 - December 31, 2020")
print("Post-COVID: After December 31, 2020")

# Overall impact
print("\n2. OVERALL UNEMPLOYMENT IMPACT")
print("-"*80)

pre_covid = df[df['covid_period'] == 'Pre-COVID']
covid = df[df['covid_period'] == 'COVID']
post_covid = df[df['covid_period'] == 'Post-COVID']

pre_mean = pre_covid['estimated_unemployment_rate_pct'].mean()
covid_mean = covid['estimated_unemployment_rate_pct'].mean()

print(f"\nPre-COVID Average:  {pre_mean:.2f}%")
print(f"COVID Average:      {covid_mean:.2f}%")
if len(post_covid) > 0:
    post_mean = post_covid['estimated_unemployment_rate_pct'].mean()
    print(f"Post-COVID Average: {post_mean:.2f}%")

abs_change = covid_mean - pre_mean
pct_change = (abs_change / pre_mean) * 100

print(f"\nAbsolute Change: {abs_change:+.2f} percentage points")
print(f"Relative Change: {pct_change:+.1f}%")

# Peak during COVID
print("\n3. PEAK UNEMPLOYMENT DURING COVID")
print("-"*80)
covid_peak = covid['estimated_unemployment_rate_pct'].max()
peak_record = covid.loc[covid['estimated_unemployment_rate_pct'].idxmax()]

print(f"Peak Rate: {covid_peak:.2f}%")
print(f"Date: {peak_record['date'].strftime('%B %Y')}")
print(f"State: {peak_record['region']}")
print(f"Area: {peak_record['area']}")

# State-level COVID impact
print("\n4. STATE-LEVEL COVID IMPACT ANALYSIS")
print("-"*80)
print(f"{'State':<20} {'Pre-COVID':<12} {'COVID':<12} {'Change':<12} {'% Change':<12}")
print("-"*80)

state_impact = []
for state in sorted(df['region'].unique()):
    state_pre = pre_covid[pre_covid['region'] == state]['estimated_unemployment_rate_pct'].mean()
    state_covid = covid[covid['region'] == state]['estimated_unemployment_rate_pct'].mean()
    state_change = state_covid - state_pre
    state_pct = (state_change / state_pre) * 100
    
    state_impact.append({
        'state': state,
        'pre_covid': state_pre,
        'covid': state_covid,
        'change': state_change,
        'pct_change': state_pct
    })
    
    print(f"{state:<20} {state_pre:>10.2f}%  {state_covid:>10.2f}%  {state_change:>+10.2f}pp  {state_pct:>+10.1f}%")

# Most and least affected states
print("\n5. MOST AND LEAST AFFECTED STATES")
print("-"*80)
state_impact_df = pd.DataFrame(state_impact).sort_values('change', ascending=False)

print("\nMost Affected (Highest Increase):")
for i, row in state_impact_df.head(3).iterrows():
    print(f"  {row['state']:<20} {row['change']:+.2f} pp ({row['pct_change']:+.1f}%)")

print("\nLeast Affected (Lowest Increase):")
for i, row in state_impact_df.tail(3).iterrows():
    print(f"  {row['state']:<20} {row['change']:+.2f} pp ({row['pct_change']:+.1f}%)")

# Area-based impact
print("\n6. RURAL VS URBAN COVID IMPACT")
print("-"*80)
for area in ['Rural', 'Urban']:
    area_pre = pre_covid[pre_covid['area'] == area]['estimated_unemployment_rate_pct'].mean()
    area_covid = covid[covid['area'] == area]['estimated_unemployment_rate_pct'].mean()
    area_change = area_covid - area_pre
    area_pct = (area_change / area_pre) * 100
    
    print(f"\n{area}:")
    print(f"  Pre-COVID:  {area_pre:.2f}%")
    print(f"  COVID:      {area_covid:.2f}%")
    print(f"  Change:     {area_change:+.2f} pp ({area_pct:+.1f}%)")

# Labour participation impact
print("\n7. LABOUR PARTICIPATION DURING COVID")
print("-"*80)
pre_labour = pre_covid['estimated_labour_participation_rate_pct'].mean()
covid_labour = covid['estimated_labour_participation_rate_pct'].mean()
labour_change = covid_labour - pre_labour

print(f"Pre-COVID Labour Participation:  {pre_labour:.2f}%")
print(f"COVID Labour Participation:      {covid_labour:.2f}%")
print(f"Change:                          {labour_change:+.2f} pp")

# Monthly COVID trend
print("\n8. MONTHLY UNEMPLOYMENT DURING COVID PERIOD")
print("-"*80)
covid_monthly = covid.groupby(covid['date'].dt.to_period('M'))['estimated_unemployment_rate_pct'].mean()
print(covid_monthly.round(2))

# Recovery analysis
covid_data = covid.copy()
covid_data = covid_data.sort_values('date')
covid_monthly_avg = covid_data.groupby(covid_data['date'].dt.to_period('M'))['estimated_unemployment_rate_pct'].mean()

peak_month = covid_monthly_avg.idxmax()
latest_month = covid_monthly_avg.index[-1]
peak_value = covid_monthly_avg.max()
latest_value = covid_monthly_avg.iloc[-1]
recovery = peak_value - latest_value
recovery_pct = (recovery / peak_value) * 100

print("\n9. RECOVERY PATTERN ANALYSIS")
print("-"*80)
print(f"Peak Month: {peak_month} ({peak_value:.2f}%)")
print(f"Latest Month: {latest_month} ({latest_value:.2f}%)")
print(f"Recovery: {recovery:.2f} pp ({recovery_pct:.1f}% of peak)")

print("\n" + "="*80)
print("ANALYSIS COMPLETE")
print("="*80)
