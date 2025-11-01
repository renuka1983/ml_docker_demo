import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('../data/diabetes.csv')


X = df.drop('Outcome', axis = 1)
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = .30, random_state=42)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

model1 = LogisticRegression()
logistic_model = model1.fit(X_train, y_train)
y_test_predict = logistic_model.predict(X_test)

import pickle
file_name = 'log_model.sav'
pickle.dump(logistic_model, open(file_name,"wb") )