# Visualization Index - Day 3

## Overview

This document catalogs all visualizations created during Day 3 Exploratory Data Analysis.

**Location:** `outputs/figures/`  
**Total Visualizations:** 10  
**Format:** PNG (300 DPI)

---

## 1. Unemployment Trend Over Time
**Filename:** `01_unemployment_trend_overall.png`

**Description:** Line plot showing average unemployment rate across all regions from January 2019 to November 2020.

**Key Features:**
- Monthly unemployment rate trend
- Red dashed line marking COVID-19 start (March 2020)
- Clear visualization of the April 2020 spike

**Insights:**
- Sharp spike in March-April 2020
- Peak at 28.53% in April 2020
- Gradual recovery from June 2020 onwards

---

## 2. State-wise Average Unemployment
**Filename:** `02_state_wise_unemployment.png`

**Description:** Horizontal bar chart comparing average unemployment rates across the 6 Indian states.

**Key Features:**
- Color-coded bars (green=low, red=high)
- Sorted from lowest to highest
- Clear state rankings

**Insights:**
- Andhra Pradesh: Lowest (7.11%)
- Delhi: Highest (11.01%)
- Southern states perform better than northern states

---

## 3. Monthly Unemployment Pattern
**Filename:** `03_monthly_unemployment.png`

**Description:** Bar chart showing average unemployment rate for each month (aggregated across years).

**Key Features:**
- Monthly aggregation showing seasonal patterns
- Highlights April as peak month

**Insights:**
- April shows highest unemployment (15.58%)
- December shows lowest (3.47%)
- Clear impact of COVID months (Mar-Jun 2020)

---

## 4. Unemployment Distribution Analysis
**Filename:** `04_unemployment_distribution.png`

**Description:** Two-panel visualization: histogram and box plot of unemployment rate distribution.

**Key Features:**
- Left: Histogram showing frequency distribution
- Right: Box plot showing quartiles and outliers

**Insights:**
- Right-skewed distribution
- Multiple outliers in 20-36% range (COVID period)
- Median at 4.21%, mean at 8.49%

---

## 5. Rural vs Urban Unemployment Trends
**Filename:** `05_rural_vs_urban.png`

**Description:** Dual-line plot comparing rural and urban unemployment trends over time.

**Key Features:**
- Two lines (Rural and Urban)
- COVID start marker
- Comparative visualization

**Insights:**
- Urban areas show slightly higher unemployment
- Both follow similar trends
- Urban peak higher than rural during COVID

---

## 6. Labour Participation Rate Trend
**Filename:** `06_labour_participation_trend.png`

**Description:** Line plot showing labour participation rate over time.

**Key Features:**
- Monthly labour participation trend
- COVID start marker
- Shows participation decline during COVID

**Insights:**
- Participation dropped from ~43% to ~28% at COVID peak
- Gradual recovery visible
- Strong negative correlation with unemployment

---

## 7. State-Monthly Unemployment Heatmap
**Filename:** `07_state_monthly_heatmap.png`

**Description:** Heatmap showing unemployment rates across states (rows) and months (columns).

**Key Features:**
- Color intensity indicates unemployment level
- Annotated with actual values
- Yellow-Orange-Red color scheme

**Insights:**
- April-May columns show darkest colors (highest unemployment)
- Geographic and temporal patterns visible simultaneously
- Delhi and UP show consistently higher values

---

## 8. Area Monthly Comparison
**Filename:** `08_area_monthly_comparison.png`

**Description:** Line plot comparing rural and urban monthly unemployment patterns.

**Key Features:**
- Two lines showing monthly trends
- Month-by-month comparison
- Grid for easy reading

**Insights:**
- Urban unemployment consistently 0.5-1 pp higher
- Both peak in April
- Similar recovery patterns

---

## 9. Correlation Analysis
**Filename:** `09_correlation_analysis.png`

**Description:** Two-panel scatter plot showing unemployment vs labour participation relationship.

**Key Features:**
- Left: Overall correlation scatter with trend line
- Right: Scatter colored by COVID period

**Insights:**
- Strong negative correlation (-0.67)
- COVID period shows stronger correlation (-0.68)
- Clear inverse relationship visible

---

## 10. Time Series with Moving Average
**Filename:** `10_time_series_analysis.png`

**Description:** Two-panel time series: unemployment rate and labour participation rate.

**Key Features:**
- Top: Unemployment with 3-month moving average
- Bottom: Labour participation trend
- Both marked with COVID start line

**Insights:**
- Moving average smooths out monthly fluctuations
- Both metrics show clear COVID impact
- Recovery trends visible in both

---

## Visualization Summary

### By Type:
- **Line Plots:** 5 (Trends, Time Series)
- **Bar Charts:** 2 (State comparison, Monthly)
- **Scatter Plots:** 1 (Correlation)
- **Heatmap:** 1 (State-Month)
- **Distribution:** 1 (Histogram + Box Plot)

### By Theme:
- **Temporal Analysis:** 4 visualizations
- **Geographic Analysis:** 2 visualizations
- **Comparative Analysis:** 3 visualizations
- **Statistical Analysis:** 1 visualization

### Color Schemes Used:
- **Blue tones:** Unemployment trends
- **Orange tones:** Labour participation
- **Red-Yellow:** Heatmaps
- **Green-Red:** Comparative scales
- **Multi-color:** COVID period distinction

## Usage Recommendations

### For Presentations:
- Use 01, 02, 07 for overview
- Use 05, 08 for rural-urban story
- Use 09 for correlation insights

### For Reports:
- Include all 10 for comprehensive analysis
- Pair text descriptions with visualizations
- Reference specific insights from each

### For Further Analysis:
- Build upon time series (10) for forecasting
- Extend heatmap (07) with more granular data
- Deepen correlation analysis (09) with multivariate approach

---

**Index Generated:** Day 3 - EDA Phase  
**Visualizations:** Professional, publication-ready  
**All files verified:** ✓  
**Ready for Day 4:** ✓
