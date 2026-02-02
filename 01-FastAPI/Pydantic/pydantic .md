# Why we need Pydantic?

When building APIs, especially with FastAPI, we often need to validate and serialize data. This is where Pydantic comes into play. Pydantic is a data validation and settings management library that uses Python type annotations to define data models.

1. **Define a Pytdatic model that represents the ideal schema of the data we expect.**
 - expected data: name (string), age (integer), email (string) and any data validationns we want to perform. (eg: age should be positive, email should be valid format etc)

 2. **Instantiate the model with raw input data**
  - raw input data: data received from an API request, which may be in the form of a dictionary or JSON object.

3. **pass the valudated model instance to our application logic**
 - application logic: the core functionality of our API that processes the validated data and performs the desired operations.

 
