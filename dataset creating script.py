# This is script that creating dataset in needed number of rows and columns,
# and filling it with randon int numbers

import pandas as pd
import numpy as np

np.random.seed(42)

num_rows = 500
num_columns = 10

data = {}

for i in range(num_columns):
    column_name = f'Column_{i + 1}'

    data_type = np.random.choice(['int'])
    data[column_name] = np.random.randint(0, 1001, num_rows)

df = pd.DataFrame(data)

csv_filename = 'random_dataset.csv'
df.to_csv(csv_filename, index=False)

print(f"Dataset created and saved as {csv_filename}")
