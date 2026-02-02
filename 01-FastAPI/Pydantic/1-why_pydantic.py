def insert_patient(name, city, age):
    if type(name) != str:
        raise TypeError("Name must be a string")
    if type(city) != str:
        raise TypeError("City must be a string")
    if type(age) != int:
        raise TypeError("Age must be an integer")
    print(name)
    print(city)
    print(age)
    print("Inserting patient into database...")
    
insert_patient("John", "New York", 30)
# But if we call the function with incorrect types
insert_patient(123, 456, "thirty")  # This will not raise an error
# The above call will not raise an error, leading to potential issues later in the code.

# Pydantic helps solve this problem by enforcing type checks and validations.

def update_patient(name: str, city: str, age: int):
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    if not isinstance(city, str):
        raise ValueError("City must be a string")
    if not isinstance(age, int):
        raise ValueError("Age must be an integer")
    print("Updating patient in database...")