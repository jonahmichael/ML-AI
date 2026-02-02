from Pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient(name,age):
    print(name)
    print(age)
    print("Inserting patient into database...")
    
patient1={"name":"Jonah","age":19}
patient1_obj=Patient(**patient1)  # Pydantic will validate the data here

insert_patient(patient1_obj.name, patient1_obj.age)