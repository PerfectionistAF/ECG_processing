# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11IYUtSRj--5qwdpVrfaBgztBh062YgMH
"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import pandas as pd

# Specify the path to your CSV file
file_path = "panda_data.csv"  # Replace with your actual file path

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Now you can work with the data in the DataFrame 'df'
print(df.head())  # Print the first few rows of the DataFrame

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Features and target variable
X = df.drop(columns=['age_category','num'])
y = df['num']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gradient Boosting Classifier model
gbmodel = GradientBoostingClassifier(random_state=42,n_estimators=50)

# Train the model on the training set
gbmodel.fit(X_train, y_train)

# Make predictions on the testing set
y_pred_train = gbmodel.predict(X_train)
y_pred = gbmodel.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
conf_matrix_train = confusion_matrix(y_train, y_pred_train)
classification_rep = classification_report(y_test, y_pred)


# Calculate training accuracy
train_accuracy = gbmodel.score(X_train, y_train)

print(f'Training Accuracy: {train_accuracy:.2f}')
print(f'Testing Accuracy: {accuracy:.2f}')
print('\nConfusion Matrix training:')
print(conf_matrix_train)
print('\nConfusion Matrix testing:')
print(conf_matrix)
print('\nClassification Report:')
print(classification_rep)

# Save model as pickle file extension
filename = './models/gradient_boost_model.sav'
pickle.dump(gbmodel, open(filename, 'wb'))
