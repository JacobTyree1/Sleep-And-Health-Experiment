#!/usr/bin/env python3
"""
Sleep and Health Data Analysis - Main Entry Point

This script demonstrates basic data loading and analysis using the installed packages.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    """Load the sleep health dataset."""
    try:
        data = pd.read_csv('SleepHealthandLifestyle.csv')
        print(f"Dataset loaded successfully!")
        print(f"Shape: {data.shape}")
        print(f"Columns: {list(data.columns)}")
        return data
    except FileNotFoundError:
        print("Error: SleepHealthandLifestyle.csv not found in current directory")
        return None

def basic_analysis(data):
    """Perform basic exploratory data analysis."""
    if data is None:
        return
    
    print("\n=== Basic Dataset Information ===")
    print(f"Total records: {len(data)}")
    print(f"Missing values:\n{data.isnull().sum()}")
    
    print("\n=== Sleep Duration Statistics ===")
    print(data['Sleep Duration'].describe())
    
    print("\n=== Quality of Sleep Distribution ===")
    print(data['Quality of Sleep'].value_counts().sort_index())

def main():
    """Main function to run the analysis."""
    print("Sleep and Health Data Analysis")
    print("=" * 40)
    
    # Load data
    data = load_data()
    
    # Perform basic analysis
    basic_analysis(data)
    
    print("\n=== Next Steps ===")
    print("1. Run 'uv run jupyter notebook' to start Jupyter")
    print("2. Open DataSciencePractice.ipynb for interactive analysis")
    print("3. Use 'uv add package_name' to add new dependencies")

if __name__ == "__main__":
    main()
