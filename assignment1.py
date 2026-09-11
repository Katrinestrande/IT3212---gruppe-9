import pandas as pd

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