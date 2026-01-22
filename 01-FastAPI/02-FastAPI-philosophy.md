# FastAPI Philosophy | How to setup and use FastAPI

FAstAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. The key philosophies behind FastAPI are:
1. **Fast to code**: FastAPI is designed to be easy to use and learn, allowing developers to create APIs quickly. The use of Python type hints helps with code completion and reduces the amount of boilerplate code needed.
2. **High performance**: FastAPI is built on top of Starlette for the web parts and Pydantic for the data parts, which makes it one of the fastest Python frameworks available. It is designed to handle high loads and provide low latency responses.

Starlette manages how your api handles requests and responses, routing, middleware, and other web-related functionalities.

 Pydantic is used to check if rhe data sent to and from the API is valid and correctly formatted, based on the defined data models.

## WHy FASTAPI?

1. Fast to Run: 
2. Fast to Code:


---

## Fast ti Run

![alt text](image.png)

Assume there is a ML Model which takes some input and gives output after processing.

Usinf feature f1 adn f2 we can build a ML model to predict output.

So the web server will send a http request to the API with input features f1 and f2.

which looks like this:
```json
POST /predict HTTP/1.1
Host: api.example.com
Content-Type: application/json
Content-Length: ...
{
  "f1": value1,
  "f2": value2
} 
```


THis is a http request which our API cannot understand, so it uses SGI(Standard Gateway Interface) to convert this http request into a python object which can be understood by our ML model.

The ML model processes the input features and generates a prediction. 
It looks like this:
```python
{
  "prediction": predicted_value
}
```

The API then takes this prediction and converts it back into an HTTP response format using SGI.

The response looks like this:
```json
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: ...
{
  "prediction": predicted_value
}
```
This response is then sent back to the web server, which can then present the prediction to the user.

---

## Same Flow - How does it work in Flask?

SGI is of two types: WSGI(Web Server Gateway Interface) and ASGI(Asynchronous Server Gateway Interface).

Flask follows WSGI standard which is synchronous in nature.
This means that each request is handled one at a time, which can lead to delays if multiple requests are made simultaneously.

![alt text](image-1.png)