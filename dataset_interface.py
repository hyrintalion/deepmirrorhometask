# This is storage of functions that working with dataset file

import pandas as pd

def get_dataset():
    dataset = pd.read_csv('random_dataset.csv')
    return dataset

def update_column(column):
    dataset = get_dataset()
    dataset[column] = dataset[column] + 1
    dataset.to_csv('random_dataset.csv', index=False)
