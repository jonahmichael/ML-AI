from fastapi import FastAPI

app = FastAPI() # create an instance of FastAPI

@app.get("/")   # to fetch data from server , we use get method ( we'll discuss indetail later)

def hello_world(): # cretae a function to handle requests to the root endpoint
    return {"message": "Hello, World!"}