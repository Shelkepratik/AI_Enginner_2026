from fastapi import FastAPI,Path,HTTPException
import json

app=FastAPI()

def load_data():
    with open("patients.json","r") as file:
        data=json.load(file)
        return data
        
@app.get("/view")
def view_patient_data():
    patient_data=load_data()
    return patient_data

@app.get("/view/{patient_id}")
def view_specific_patient_data(patient_id:str=Path(...,description="ID Of patient",example="P001")):
    data1=load_data()
    if patient_id in data1:
        return data1[patient_id]




