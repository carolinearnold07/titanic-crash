import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

# print("Hello, world!")

# Construct the relative path to the CSV
train_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'train.csv')

# Read the CSV file into a DataFrame
train = pd.read_csv(train_path)

print(train.head())

