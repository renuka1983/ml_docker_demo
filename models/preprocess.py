import pandas as pd
import numpy as np

data = pd.read_csv("~/mlops_docker_demo/data/diabetes.csv")

data.to_csv("~/mlops_docker_demo/data/diabetes_preprocessed.csv")