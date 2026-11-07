from fastapi import FastAPI,Path,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from fastapi.middleware.cors import CORSMiddleware
import json

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Patient(BaseModel):
    id:Annotated[str,Field(min_length=4,max_length=4)]
    name:Annotated[str,Field(min_length=1,max_length=10)]
    city:Annotated[str,Field(min_length=1,max_length=20)]
    age:Annotated[int,Field(gt=0,lt=121)]
    gender:Annotated[Literal["male","female"],Field(description="gender of patient")]
    height:Annotated[float,Field(gt=0,lt=10)]
    weight:Annotated[float,Field(gt=0,lt=100,description="weight in kg")]


class PatientUpdate(BaseModel):
    height: Annotated[float, Field(gt=0, lt=10)]
    weight: Annotated[float, Field(gt=0, lt=100)]

    @computed_field#add new field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2))
        return bmi

    @computed_field
    @property
    def verdic(self)->str:
        if self.bmi<18.5:
            return "underweight"
        elif self.bmi<25:
            return "normal"
        else:
            return "obsec"
   

def load_data():
    with open("patients.json","r") as file:
        data=json.load(file)
        return data

def save_data(data):
    with open("patients.json","w") as obj1:
        json.dump(data,obj1)
        
@app.get("/view")
def view_patient_data():
    patient_data=load_data()
    return patient_data

@app.post("/create")
def create_patient(patient: Patient):
    print(patient)
    print(type(patient))
    patient_data = load_data()
    if patient.id in patient_data:
        print("patient already exists")
    patient_data[patient.id]=patient.model_dump(exclude=["id"])#model_dump is used to convert the object into json
    save_data(patient_data)
    return JSONResponse(content={
        "message":"Patient create successfully"
    })

@app.get("/view/{patient_id}")
def view_specific_patient_data(patient_id:str=Path(...,description="ID Of patient",example="P001")):
    data1=load_data()
    if patient_id in data1:
        return data1[patient_id]


@app.put("/edit/{patient_id}")
def update_patient(patient_id:str,patient: Patient):
    patient_data=load_data()
    if patient_id not in patient_data:
        raise HTTPException(status_code=404,detail="Patient not found")


    #update existing patient record
    patient_data[patient_id]=patient.model_dump(exclude=["id"])

    save_data(patient_data)

    return JSONResponse(content={
        "message":"Patient updated successfully"
    })

@app.put("/edit/{patient_id}")
def update_patient(
    patient_id: str,
    patient_update: PatientUpdate
):
    patient_data = load_data()

    # Check patient exists
    if patient_id not in patient_data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    # Update only height and weight
    patient_data[patient_id]["height"] = patient_update.height
    patient_data[patient_id]["weight"] = patient_update.weight

    # Save updated data
    save_data(patient_data)

    return JSONResponse(
        content={
            "message": "Patient height and weight updated successfully"
        }
    )


@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):

    patient_data = load_data()

    # Check whether patient exists
    if patient_id not in patient_data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    # Delete patient record
    del patient_data[patient_id]

    # Save updated data
    save_data(patient_data)

    return JSONResponse(
        content={
            "message": "Patient deleted successfully"
        }
    )