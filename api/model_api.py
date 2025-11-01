from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy
import os


app = FastAPI()

class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# laoding the saved mode

model_path = os.path.join(os.path.dirname(__file__), '../models/log_model.sav')
diab_model = pickle.load(open(model_path, 'rb'))

@app.post('/diabetes_prediction')

def diab_pred(input_parameters: model_input):
    input_data = input_parameters.model_dump_json()
    input_dictionary = json.loads(input_data)

    preg = input_dictionary['Pregnancies']
    gluc = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin_thick = input_dictionary['SkinThickness']
    insu = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    diab = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    input_list = [preg,gluc,bp,skin_thick,insu,bmi,diab, age]

    prediction = diab_model.predict([input_list])

    if prediction[0]==0:
        return 'Patient is not diabetic'
    else:
         return 'Patient is not diabetic'
    

