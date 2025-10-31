import pandas as pd
import numpy as np
import os

print("Hello, world!")

# Construct the relative path to the CSV
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'gender_submission.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv(data_path)

print(df.head())

