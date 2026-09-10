# Summary Statistics - Day 3 EDA

## Overall Dataset Statistics

| Metric | Value |
|--------|-------|
| Total Records | 253 |
| Time Period | Jan 2019 - Nov 2020 (23 months) |
| States Covered | 6 |
| Area Types | Rural & Urban |

## Unemployment Rate Statistics

| Statistic | Value |
|-----------|-------|
| Mean | 8.49% |
| Median | 4.21% |
| Mode Region | ~3-5% (Pre-COVID baseline) |
| Standard Deviation | 8.02% |
| Minimum | 1.45% (Karnataka, Urban, May 2019) |
| Maximum | 35.89% (Uttar Pradesh, Urban, April 2020) |
| 25th Percentile | 2.98% |
| 75th Percentile | 11.67% |
| Range | 34.44 percentage points |

## State Rankings

### By Average Unemployment (Lowest to Highest):

| Rank | State | Mean | Std Dev | Min | Max |
|------|-------|------|---------|-----|-----|
| 1 | Andhra Pradesh | 7.11% | 5.82% | 2.34% | 23.87% |
| 2 | Karnataka | 7.15% | 7.16% | 1.45% | 26.78% |
| 3 | Tamil Nadu | 7.71% | 7.50% | 1.78% | 28.67% |
| 4 | Maharashtra | 8.77% | 8.43% | 2.01% | 31.23% |
| 5 | Uttar Pradesh | 10.45% | 9.54% | 2.78% | 35.89% |
| 6 | Delhi | 11.01% | 9.60% | 3.67% | 34.56% |

## Year-wise Comparison

| Year | Mean | Median | Min | Max | Change from 2019 |
|------|------|--------|-----|-----|------------------|
| 2019 | 3.10% | 3.00% | 1.45% | 5.12% | - |
| 2020 | 14.36% | 12.34% | 2.89% | 35.89% | +11.26 pp (+363%) |

## Monthly Patterns

| Month | Avg Unemployment | Status |
|-------|------------------|--------|
| January | 3.48% | Low |
| February | 4.38% | Low |
| March | 6.64% | Rising |
| April | 15.58% | **PEAK** |
| May | 14.17% | Very High |
| June | 12.00% | High |
| July | 10.28% | Elevated |
| August | 9.08% | Declining |
| September | 7.75% | Moderate |
| October | 6.62% | Moderate |
| November | 5.90% | Declining |
| December | 3.47% | Low |

## Quarterly Analysis

| Quarter | Avg Unemployment | Relative to Q1 |
|---------|------------------|----------------|
| Q1 (Jan-Mar) | 4.83% | Baseline |
| Q2 (Apr-Jun) | 13.92% | +188% |
| Q3 (Jul-Sep) | 9.04% | +87% |
| Q4 (Oct-Dec) | 5.70% | +18% |

## COVID Period Comparison

| Period | Mean | Median | Min | Max | Records |
|--------|------|--------|-----|-----|---------|
| Pre-COVID (before Mar 2020) | 3.32% | 3.12% | 1.45% | 7.12% | 126 |
| COVID (Mar-Dec 2020) | 16.53% | 14.23% | 6.12% | 35.89% | 120 |
| Post-COVID (after Dec 2020) | - | - | - | - | 7 |
| **Absolute Change** | **+13.21 pp** | **+11.11 pp** | **+4.67 pp** | **+28.77 pp** | - |
| **Relative Change** | **+397.9%** | **+356.4%** | **+322.1%** | **+404.2%** | - |

## Rural vs Urban Comparison

| Area | Mean | Median | Min | Max | Records |
|------|------|--------|-----|-----|---------|
| Rural | 8.08% | 4.21% | 1.87% | 32.45% | 115 |
| Urban | 8.83% | 4.18% | 1.45% | 35.89% | 138 |
| **Difference** | **+0.75 pp** | **-0.03 pp** | **-0.42 pp** | **+3.44 pp** | - |

### Pre-COVID vs COVID by Area:

| Area | Pre-COVID | COVID | Change |
|------|-----------|-------|--------|
| Rural | 3.49% | 15.22% | +11.73 pp (+336%) |
| Urban | 3.18% | 17.62% | +14.44 pp (+454%) |

## Labour Participation Rate

| Metric | Value |
|--------|-------|
| Mean | 42.85% |
| Median | 42.89% |
| Minimum | 28.12% |
| Maximum | 53.12% |
| Range | 25.00 pp |

### By Area:

| Area | Mean Labour Participation |
|------|---------------------------|
| Rural | 44.55% |
| Urban | 41.42% |
| **Difference** | **+3.13 pp (Rural higher)** |

## Correlation Analysis

| Variables | Correlation | Strength |
|-----------|-------------|----------|
| Unemployment vs Labour Participation | -0.6694 | Strong Negative |

### By Period:

| Period | Correlation |
|--------|-------------|
| Pre-COVID | -0.1350 |
| COVID | -0.6785 |

### By Area:

| Area | Correlation |
|------|-------------|
| Rural | -0.6839 |
| Urban | -0.7019 |

## Key Turning Points

| Event | Date | Value | Description |
|-------|------|-------|-------------|
| Lowest Point | May 2019 | 2.48% | Pre-COVID baseline |
| COVID Start | March 2020 | 10.38% | Initial spike |
| Highest Point | April 2020 | 28.53% | Peak unemployment |
| Recovery Start | June 2020 | 21.22% | Beginning decline |
| Latest Data | November 2020 | 8.64% | Continued recovery |

## Month-to-Month Changes

### Largest Increases:

| Month | Change | New Rate |
|-------|--------|----------|
| April 2020 | +18.15 pp | 28.53% |
| March 2020 | +5.02 pp | 10.38% |
| February 2020 | +1.49 pp | 5.36% |

### Largest Decreases:

| Month | Change | New Rate |
|-------|--------|----------|
| June 2020 | -4.65 pp | 21.22% |
| July 2020 | -4.03 pp | 17.19% |
| August 2020 | -2.77 pp | 14.42% |

## State + Area Combinations

| State | Rural | Urban | Difference |
|-------|-------|-------|------------|
| Andhra Pradesh | 7.07% | 7.14% | +0.07 pp |
| Karnataka | 6.99% | 7.31% | +0.32 pp |
| Tamil Nadu | 7.53% | 7.88% | +0.35 pp |
| Maharashtra | 8.61% | 8.94% | +0.33 pp |
| Uttar Pradesh | 10.19% | 10.71% | +0.52 pp |
| Delhi | N/A | 11.01% | N/A |

**Finding:** Urban unemployment consistently higher across all states.

---

**Generated:** Day 3 - Exploratory Data Analysis  
**Data Period:** January 2019 - November 2020  
**Analysis Complete:** ✓
