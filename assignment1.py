import pandas as pd

def data_exploration():

    df = pd.read_csv("graduation_dataset.csv")
    print(df.head())

data_exploration()