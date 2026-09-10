@echo off
echo ========================================
echo Running All Day 3 EDA Analyses
echo ========================================
echo.

echo [1/7] Running EDA Analysis...
py src\eda_analysis.py

echo.
echo [2/7] Running State Analysis...
py src\state_analysis.py

echo.
echo [3/7] Running Area Comparison...
py src\area_comparison.py

echo.
echo [4/7] Running Correlation Analysis...
py src\correlation_analysis.py

echo.
echo [5/7] Running Time Series Analysis...
py src\time_series_analysis.py

echo.
echo [6/7] Running Peak Analysis...
py src\peak_analysis.py

echo.
echo [7/7] Generating Comprehensive Report...
py src\generate_eda_report.py

echo.
echo ========================================
echo All analyses complete!
echo ========================================
pause
