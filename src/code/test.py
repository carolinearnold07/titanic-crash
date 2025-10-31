import pandas as pd
import numpy as np
import os

print("Hello, world!")

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Construct the relative path to the CSV file
# We need to go up one level from 'code' to 'src', then down into 'data'
csv_file_path = os.path.join(script_dir, '..', 'data', 'gender_submission.csv')

# Read the CSV file into a pandas DataFrame
# df = pd.read_csv(csv_file_path)
df = pd.read_csv('data/gender_submission.csv')

# You can now work with the DataFrame 'df'
print(df.head())
