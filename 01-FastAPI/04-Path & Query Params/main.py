
from flask import app, HTTPException
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
    raise HTTPException(status_code=404, detail="Patient not found")
  
@app.get('/search/')
def search(city: str = None, age: int = None):
    data = load_data()
    results = []
    for patient_id, details in data.items():
        if city and details['city'].lower() != city.lower():
            continue
        if age and details['age'] != age:
            continue
        results.append({patient_id: details})
    return results
  
@app.get('/sort')
def sort(by: str = 'age'):
    data = load_data()
    if by not in ['age', 'bmi']:
        return {"error": "Invalid sort parameter"}
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1][by]))
    return sorted_data