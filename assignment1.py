import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

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

    cols_to_check = ['Age at enrollment', 
                  'Curricular units 1st sem (grade)', 
                  'Curricular units 2nd sem (grade)']

# Outliers with Z-score
print("\nZ-SCORE METHOD (threshold = 3)")
zscore_results = {}
for col in cols_to_check:
    z_scores = np.abs(stats.zscore(df[col]))
    outliers = df[z_scores > 3]
    zscore_results[col] = len(outliers)
    print(f'{col}: {len(outliers)} outliers')

# Comparison: IQR vs Z-score
iqr_results = {}
for col in cols_to_check:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    iqr_results[col] = len(outliers)

print("\nCOMPARISON")
print(pd.DataFrame({'IQR': iqr_results, 'Z-score': zscore_results}))

# Boxplots
fig, axes = plt.subplots(1, len(cols_to_check), figsize=(15, 4))
for i, col in enumerate(cols_to_check):
    axes[i].boxplot(df[col])
    axes[i].set_title(col, fontsize=9)
plt.tight_layout()
plt.savefig('outliers_boxplot.png', dpi=150)
plt.show()

# Handle outliers: cap Age at enrollment (IQR-based), keep grades unchanged
Q1 = df['Age at enrollment'].quantile(0.25)
Q3 = df['Age at enrollment'].quantile(0.75)
IQR = Q3 - Q1
lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
df['Age at enrollment'] = df['Age at enrollment'].clip(lower=lower, upper=upper)

print(f"\nAge at enrollment after capping: min={df['Age at enrollment'].min()}, "
      f"max={df['Age at enrollment'].max()}")
# Grade columns kept unchanged - 0s likely reflect real dropout cases