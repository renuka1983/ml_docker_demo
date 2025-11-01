import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

mlflow.set_tracking_uri("file:./models/mlruns")
mlflow.set_experiment("diabetes_experiment")

# Load data
data = pd.read_csv("diabetes_preprocessed.csv")
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Evaluate
acc = accuracy_score(y, model.predict(X))

# Log to MLflow
with mlflow.start_run():
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")

# Save locally for FastAPI
pickle.dump(model, open("models/log_model.sav", "wb"))
