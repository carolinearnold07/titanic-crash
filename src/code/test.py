import pandas as pd
import numpy as np
import os

print("Hello, world!")

# Get the current directory of the script
script_dir = os.path.dirname(__file__)

# Construct the path to the data folder
data_folder_path = os.path.join(script_dir, '..', 'data')

# Construct the full path to the data file
data_file_path = os.path.join(data_folder_path, 'gender_submission.csv')

df = pd.read_csv(data_file_path)
df.head()