"""
Seasonality Analysis - Day 5
Analyzes seasonal patterns in unemployment data
Compares year-over-year monthly patterns (2019 vs 2020)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('data/unemployment_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])

print("=" * 80)
print("SEASONALITY ANALYSIS - UNEMPLOYMENT DATA")
print("=" * 80)
print()

# ============================================================================
# 1. YEAR-OVER-YEAR MONTHLY COMPARISON (2019 vs 2020)
# ============================================================================
print("1. YEAR-OVER-YEAR MONTHLY COMPARISON")
print("-" * 80)

# Calculate monthly averages by year
monthly_by_year = df.groupby(['year', 'month', 'month_name'])['estimated_unemployment_rate_pct'].mean().reset_index()
monthly_by_year = monthly_by_year.sort_values(['year', 'month'])

print("\nMonthly Unemployment by Year:")
print()
for month in range(1, 13):
    month_data = monthly_by_year[monthly_by_year['month'] == month]
    if len(month_data) == 2:
        y2019 = month_data[month_data['year'] == 2019]['estimated_unemployment_rate_pct'].values[0]
        y2020 = month_data[month_data['year'] == 2020]['estimated_unemployment_rate_pct'].values[0]
        change = y2020 - y2019
        pct_change = ((y2020 - y2019) / y2019) * 100
        month_name = month_data['month_name'].values[0]
        
        print(f"{month_name:12s} | 2019: {y2019:6.2f}% | 2020: {y2020:6.2f}% | "
              f"Change: {change:+7.2f} pp ({pct_change:+7.1f}%)")

# Calculate which months show highest year-over-year change
yoy_changes = []
for month in range(1, 13):
    month_data = monthly_by_year[monthly_by_year['month'] == month]
    if len(month_data) == 2:
        y2019 = month_data[month_data['year'] == 2019]['estimated_unemployment_rate_pct'].values[0]
        y2020 = month_data[month_data['year'] == 2020]['estimated_unemployment_rate_pct'].values[0]
        change = y2020 - y2019
        pct_change = ((y2020 - y2019) / y2019) * 100
        month_name = month_data['month_name'].values[0]
        yoy_changes.append({
            'month': month,
            'month_name': month_name,
            'y2019': y2019,
            'y2020': y2020,
            'absolute_change': change,
            'percent_change': pct_change
        })

yoy_df = pd.DataFrame(yoy_changes)
yoy_df = yoy_df.sort_values('absolute_change', ascending=False)

print("\n" + "=" * 80)
print("MONTHS WITH HIGHEST YEAR-OVER-YEAR CHANGE (2019 vs 2020):")
print("-" * 80)
for idx, row in yoy_df.head(5).iterrows():
    print(f"{row['month_name']:12s} | Change: {row['absolute_change']:+7.2f} pp ({row['percent_change']:+7.1f}%)")

print("\n" + "=" * 80)
print("MONTHS WITH LOWEST YEAR-OVER-YEAR CHANGE (2019 vs 2020):")
print("-" * 80)
for idx, row in yoy_df.tail(5).iterrows():
    print(f"{row['month_name']:12s} | Change: {row['absolute_change']:+7.2f} pp ({row['percent_change']:+7.1f}%)")

# ============================================================================
# 2. SEASONAL PATTERN ANALYSIS (PRE-COVID 2019 ONLY)
# ============================================================================
print("\n" + "=" * 80)
print("2. SEASONAL PATTERN ANALYSIS (2019 - PRE-COVID BASELINE)")
print("-" * 80)

df_2019 = df[df['year'] == 2019]
monthly_2019 = df_2019.groupby(['month', 'month_name'])['estimated_unemployment_rate_pct'].agg(['mean', 'std', 'min', 'max']).reset_index()
monthly_2019 = monthly_2019.sort_values('month')

print("\n2019 Monthly Pattern (Baseline):")
print()
for idx, row in monthly_2019.iterrows():
    print(f"{row['month_name']:12s} | Mean: {row['mean']:5.2f}% | Std: {row['std']:5.2f}% | "
          f"Range: {row['min']:5.2f}% - {row['max']:5.2f}%")

# Identify high/low months in 2019
highest_2019 = monthly_2019.nlargest(3, 'mean')
lowest_2019 = monthly_2019.nsmallest(3, 'mean')

print("\n" + "-" * 80)
print("HIGHEST UNEMPLOYMENT MONTHS (2019):")
for idx, row in highest_2019.iterrows():
    print(f"  {row['month_name']}: {row['mean']:.2f}%")

print("\nLOWEST UNEMPLOYMENT MONTHS (2019):")
for idx, row in lowest_2019.iterrows():
    print(f"  {row['month_name']}: {row['mean']:.2f}%")

# ============================================================================
# 3. QUARTERLY SEASONALITY
# ============================================================================
print("\n" + "=" * 80)
print("3. QUARTERLY SEASONALITY ANALYSIS")
print("-" * 80)

quarterly = df[df['year'] == 2019].groupby('quarter')['estimated_unemployment_rate_pct'].agg(['mean', 'std']).reset_index()
quarterly['quarter_label'] = ['Q1 (Jan-Mar)', 'Q2 (Apr-Jun)', 'Q3 (Jul-Sep)', 'Q4 (Oct-Dec)']

print("\n2019 Quarterly Pattern:")
for idx, row in quarterly.iterrows():
    print(f"{row['quarter_label']:15s} | Mean: {row['mean']:5.2f}% | Std: {row['std']:5.2f}%")

# Calculate coefficient of variation for seasonal variability
cv_monthly = (monthly_2019['mean'].std() / monthly_2019['mean'].mean()) * 100
print(f"\nCoefficient of Variation (Monthly, 2019): {cv_monthly:.2f}%")
print("  (Measure of seasonal variability - lower = less seasonal pattern)")

# ============================================================================
# 4. STATE-WISE SEASONAL PATTERNS
# ============================================================================
print("\n" + "=" * 80)
print("4. STATE-WISE SEASONAL PATTERNS (2019)")
print("-" * 80)

df_2019_states = df[df['year'] == 2019].copy()
state_seasonality = []

for state in df_2019_states['region'].unique():
    state_data = df_2019_states[df_2019_states['region'] == state]
    monthly_state = state_data.groupby('month')['estimated_unemployment_rate_pct'].mean()
    
    # Calculate seasonality metrics
    max_month = monthly_state.idxmax()
    min_month = monthly_state.idxmin()
    seasonal_range = monthly_state.max() - monthly_state.min()
    cv = (monthly_state.std() / monthly_state.mean()) * 100
    
    state_seasonality.append({
        'state': state,
        'max_month': max_month,
        'min_month': min_month,
        'seasonal_range': seasonal_range,
        'cv': cv,
        'mean': monthly_state.mean()
    })

state_season_df = pd.DataFrame(state_seasonality)
state_season_df = state_season_df.sort_values('seasonal_range', ascending=False)

print("\nState-wise Seasonal Variability (2019):")
print("(Seasonal Range = Difference between highest and lowest month)")
print()
for idx, row in state_season_df.iterrows():
    print(f"{row['state']:20s} | Range: {row['seasonal_range']:5.2f} pp | CV: {row['cv']:5.2f}% | Mean: {row['mean']:5.2f}%")

# ============================================================================
# 5. DISRUPTION OF SEASONAL PATTERNS BY COVID
# ============================================================================
print("\n" + "=" * 80)
print("5. COVID-19 DISRUPTION OF SEASONAL PATTERNS")
print("-" * 80)

# Compare expected (2019) vs actual (2020) patterns
print("\nExpected (2019) vs Actual (2020) Seasonal Pattern:")
print()

# Calculate how much COVID disrupted normal seasonal patterns
disruption_scores = []
for month in range(1, 12):  # Up to November (data limit)
    y2019 = monthly_by_year[(monthly_by_year['year'] == 2019) & (monthly_by_year['month'] == month)]['estimated_unemployment_rate_pct'].values
    y2020 = monthly_by_year[(monthly_by_year['year'] == 2020) & (monthly_by_year['month'] == month)]['estimated_unemployment_rate_pct'].values
    
    if len(y2019) > 0 and len(y2020) > 0:
        deviation = abs(y2020[0] - y2019[0])
        disruption_scores.append({
            'month': month,
            'deviation': deviation
        })

disruption_df = pd.DataFrame(disruption_scores)
disruption_df = disruption_df.sort_values('deviation', ascending=False)

print("Months with Highest Disruption from Normal Pattern:")
month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
for idx, row in disruption_df.head(5).iterrows():
    month_idx = int(row['month'])
    print(f"  {month_names[month_idx]:12s}: {row['deviation']:.2f} pp deviation from 2019")

# ============================================================================
# 6. AREA-WISE SEASONALITY
# ============================================================================
print("\n" + "=" * 80)
print("6. RURAL VS URBAN SEASONALITY (2019)")
print("-" * 80)

for area in ['Rural', 'Urban']:
    area_2019 = df[(df['year'] == 2019) & (df['area'] == area)]
    monthly_area = area_2019.groupby('month')['estimated_unemployment_rate_pct'].mean()
    
    cv = (monthly_area.std() / monthly_area.mean()) * 100
    seasonal_range = monthly_area.max() - monthly_area.min()
    
    print(f"\n{area}:")
    print(f"  Seasonal Range: {seasonal_range:.2f} pp")
    print(f"  Coefficient of Variation: {cv:.2f}%")
    print(f"  Mean: {monthly_area.mean():.2f}%")
    print(f"  Highest: {monthly_area.max():.2f}% (Month {monthly_area.idxmax()})")
    print(f"  Lowest: {monthly_area.min():.2f}% (Month {monthly_area.idxmin()})")

# ============================================================================
# 7. SUMMARY STATISTICS
# ============================================================================
print("\n" + "=" * 80)
print("7. SEASONALITY SUMMARY")
print("=" * 80)

print("\nKey Findings:")
print("-" * 80)
print(f"1. Average year-over-year change: {yoy_df['absolute_change'].mean():+.2f} pp")
print(f"2. Largest YoY increase: {yoy_df['absolute_change'].max():+.2f} pp ({yoy_df.iloc[0]['month_name']})")
print(f"3. Smallest YoY increase: {yoy_df['absolute_change'].min():+.2f} pp ({yoy_df.iloc[-1]['month_name']})")
print(f"4. 2019 seasonal variability (CV): {cv_monthly:.2f}%")
print(f"5. State with highest seasonality: {state_season_df.iloc[0]['state']} ({state_season_df.iloc[0]['seasonal_range']:.2f} pp range)")
print(f"6. State with lowest seasonality: {state_season_df.iloc[-1]['state']} ({state_season_df.iloc[-1]['seasonal_range']:.2f} pp range)")

print("\nConclusion:")
print("-" * 80)
if cv_monthly < 10:
    print("The 2019 baseline shows LOW seasonal variation (CV < 10%).")
    print("Unemployment patterns were relatively stable across months.")
elif cv_monthly < 20:
    print("The 2019 baseline shows MODERATE seasonal variation (10% < CV < 20%).")
    print("Some monthly fluctuation present but not extreme.")
else:
    print("The 2019 baseline shows HIGH seasonal variation (CV > 20%).")
    print("Significant monthly fluctuation in unemployment patterns.")

print("\n2020 completely disrupted any normal seasonal patterns due to COVID-19 impact.")
print("Year-over-year changes dominated by pandemic timing rather than seasonal factors.")

print("\n" + "=" * 80)
print("SEASONALITY ANALYSIS COMPLETE")
print("=" * 80)
