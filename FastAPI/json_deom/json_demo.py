import json

patients = {
    "P001": {
        "name": "Ravi Mehta",
        "city": "Mumbai",
        "age": 35,
        "gender": "male",
        "height": 1.75,
        "weight": 85,
        "bmi": 27.76,
        "verdict": "Overweight"
    }
}

# CREATE
patients["P002"] = {
    "name": "Priya Sharma",
    "city": "Pune",
    "age": 24
}

# READ
print(patients.get("P001"))

# UPDATE
patients["P001"].update({"city": "Pune"})

# DELETE
patients.pop("P002")

# WRITE data into JSON file
with open("patients.json", "w") as file:
    json.dump(patients, file, indent=4)

# Read JSON data from file
with open("patients.json", "r") as file:
    patients = json.load(file)

# Display all patient data
print(patients)


# Access specific patient
print(patients["P001"])

# Access specific patient details
print(patients["P001"]["name"])
print(patients["P001"]["age"])