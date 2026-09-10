"""
State-by-State COVID Impact Details
"""
import pandas as pd

df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("="*80)
print("STATE-BY-STATE COVID-19 IMPACT ANALYSIS")
print("="*80)

pre_covid = df[df['covid_period'] == 'Pre-COVID']
covid = df[df['covid_period'] == 'COVID']

for state in sorted(df['region'].unique()):
    print(f"\n{'='*80}")
    print(f"STATE: {state.upper()}")
    print(f"{'='*80}")
    
    state_pre = pre_covid[pre_covid['region'] == state]
    state_covid = covid[covid['region'] == state]
    
    # Overall metrics
    pre_mean = state_pre['estimated_unemployment_rate_pct'].mean()
    covid_mean = state_covid['estimated_unemployment_rate_pct'].mean()
    change = covid_mean - pre_mean
    pct_change = (change / pre_mean) * 100
    
    print(f"\nOVERALL IMPACT:")
    print(f"  Pre-COVID Average:  {pre_mean:.2f}%")
    print(f"  COVID Average:      {covid_mean:.2f}%")
    print(f"  Absolute Change:    {change:+.2f} pp")
    print(f"  Relative Change:    {pct_change:+.1f}%")
    
    # Peak analysis
    peak_row = state_covid.loc[state_covid['estimated_unemployment_rate_pct'].idxmax()]
    print(f"\nPEAK UNEMPLOYMENT:")
    print(f"  Rate: {peak_row['estimated_unemployment_rate_pct']:.2f}%")
    print(f"  Date: {peak_row['date'].strftime('%B %Y')}")
    print(f"  Area: {peak_row['area']}")
    
    # Rural vs Urban if both exist
    areas = state_covid['area'].unique()
    if len(areas) > 1:
        print(f"\nRURAL VS URBAN IMPACT:")
        for area in sorted(areas):
            area_pre = state_pre[state_pre['area'] == area]['estimated_unemployment_rate_pct'].mean()
            area_covid = state_covid[state_covid['area'] == area]['estimated_unemployment_rate_pct'].mean()
            area_change = area_covid - area_pre
            print(f"  {area}:")
            print(f"    Pre-COVID:  {area_pre:.2f}%")
            print(f"    COVID:      {area_covid:.2f}%")
            print(f"    Change:     {area_change:+.2f} pp")
    
    # Monthly progression
    monthly = state_covid.groupby(state_covid['date'].dt.to_period('M'))['estimated_unemployment_rate_pct'].mean()
    print(f"\nMONTHLY PROGRESSION DURING COVID:")
    for month, value in monthly.items():
        print(f"  {month}: {value:.2f}%")
    
    # Recovery
    if len(monthly) > 1:
        peak_month_val = monthly.max()
        latest_val = monthly.iloc[-1]
        recovery = peak_month_val - latest_val
        recovery_pct = (recovery / peak_month_val) * 100
        print(f"\nRECOVERY METRICS:")
        print(f"  Peak: {peak_month_val:.2f}%")
        print(f"  Latest: {latest_val:.2f}%")
        print(f"  Recovery: {recovery:.2f} pp ({recovery_pct:.1f}%)")

print(f"\n{'='*80}")
print("ANALYSIS COMPLETE")
print(f"{'='*80}")
