import pandas as pd
import numpy as np

# a) Data exploration: first few rows, summary statistics, data types
def data_exploration():
    df = pd.read_csv("graduation_dataset.csv")

    # First few rows
    print("First few rows:")
    print(df.head())

    # Summary statistics
    print("\nSummary statistics:")
    print(df.describe()) 

    # Data types
    print("\nData types:")
    print(df.dtypes)

data_exploration()

df = pd.read_csv('graduation_dataset.csv')

# b) Missing values, outliers and unique values
print(df.isnull().sum())

# Outliers with IQR-method
for col in ['Age at enrollment', 'Curricular units 1st sem (grade)', 
            'Curricular units 2nd sem (grade)']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f'{col}: {len(outliers)} outliers')

# Unique values in categorical columns
for col in ['Marital status', 'Gender', 'Course', 'Application mode']:
    print(f'{col}: {df[col].nunique()} unique values')