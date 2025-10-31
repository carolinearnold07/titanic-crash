import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

# Construct the relative paths to the CSV
train_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'train.csv')
test_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test.csv')

# Read the CSV files into DataFrames
train = pd.read_csv(train_path)
test = pd.read_csv(test_path)

# Use OneHotEncoder for non-numeric variables
categorical_features = ['Sex', 'Embarked']
one_hot_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

# Combine transformers with ColumnTransformer
preprocessor = ColumnTransformer(transformers=[('cat', one_hot_encoder, categorical_features)],
                                 remainder='passthrough')

X_train = train.drop(['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'], axis=1)
y_train = train['Survived']

X_test = test.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

imputer = SimpleImputer(strategy='mean')

X_train_imputed = imputer.fit_transform(X_train_processed)
X_test_imputed = imputer.fit_transform(X_test_processed)

model = LogisticRegression(solver='liblinear', max_iter=1000)
model.fit(X_train_imputed, y_train)

y_pred = model.predict(X_train_imputed)

print(f'Accuracy with respect to training set: {round(accuracy_score(y_train, y_pred), 2)}')

p_ids = np.array(test['PassengerId'])
y_pred = ['Survived' if pred==1 else 'Did Not Survive' for pred in model.predict(X_test_imputed)]

data = {'PassengerId': p_ids, 'Predicted Outcome': y_pred}

df = pd.DataFrame(data)

print('Predicted outcomes on test set:')
print(df)

