
from flask import app
from fastapi import FastAPI
import json
app = FastAPI() # create an instance of FastAPI

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data


@app.get('/view')
def view():
    data=load_data()
    return data
  
@app.get('/view/{patient_id}')
def view_patient(patient_id: str):
    # load data
    data = load_data()
    # fetch patient details by id
    if patient_id in data:
        return data[patient_id] 
    else:
        return {"error": "Patient not found"}