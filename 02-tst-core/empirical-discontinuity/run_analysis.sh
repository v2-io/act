#!/bin/bash

# Simple script to run complete discontinuity analysis

echo "==================================="
echo "Empirical Discontinuity Analysis"
echo "==================================="

# Check if running from correct directory
if [ ! -f "analyze_git_history.py" ]; then
    echo "Error: Please run this script from the empirical-discontinuity directory"
    exit 1
fi

# Create output directories if they don't exist
mkdir -p data results

# Step 1: Analyze git history
echo ""
echo "Step 1: Analyzing git history..."
echo "---------------------------------"
python analyze_git_history.py --repo .. --max-commits 500 --output data

# Check if analysis succeeded
if [ $? -ne 0 ]; then
    echo "Error: Git history analysis failed"
    exit 1
fi

# Step 2: Generate visualizations
echo ""
echo "Step 2: Generating visualizations..."
echo "------------------------------------"
python visualize_results.py --data data --output results

# Step 3: Generate report
echo ""
echo "Step 3: Generating HTML report..."
echo "---------------------------------"
python visualize_results.py --data data --output results --report

echo ""
echo "==================================="
echo "Analysis Complete!"
echo "==================================="
echo ""
echo "Results available in:"
echo "  - Data: data/"
echo "  - Plots: results/"
echo "  - Report: results/report.html"
echo ""
echo "To view the report:"
echo "  open results/report.html"