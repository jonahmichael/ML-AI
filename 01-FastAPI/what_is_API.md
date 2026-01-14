# What is API?

API stands for Application Programming Interface. It is a set of rules and protocols that allows different software applications to communicate with each other. APIs define the methods and data formats that applications can use to request and exchange information.

Analogy:
Think of an API as a waiter in a restaurant. The waiter takes your order (request) and brings you your food (response) from the kitchen (the server). You don't need to know how the kitchen prepares the food; you just need to know how to communicate your order to the waiter.

## Need for APIs
APIs are essential for several reasons:
- **Interoperability**: They enable different software systems to work together, regardless of their underlying technologies.
- **Efficiency**: APIs allow developers to leverage existing functionalities without having to build them from scratch.
- **Scalability**: They facilitate the integration of new features and services into existing applications.
- **Automation**: APIs enable automated processes by allowing systems to interact without human intervention.

## What is needed for an API to work?
For an API to function effectively, the following components are typically required:

1. **Database**: A structured collection of data that the API can access and manipulate. This is where the information is stored.

2. **Server**: A computer or system that hosts the API and processes requests from clients. The server handles incoming API calls, executes the necessary operations, and returns the appropriate responses.

3. **Frontend**: The user interface or application that interacts with the API. The frontend sends requests to the API and displays the data received from it to the end-users.

Before API's came into existence, we used monolithic applications where the frontend and backend were tightly coupled. With the advent of APIs, we can now separate these components, allowing for more flexibility and easier maintenance.

EG: We make a IRCTC ticket application using monolithic architecture where the frontend and backend are tightly coupled. Now, with APIs, we can create a separate frontend application (like a mobile app) that communicates with the backend server through APIs to book tickets, check availability, etc. This separation allows for better scalability and easier updates to either the frontend or backend without affecting the other. For example, we have ixigo app which uses IRCTC APIs to provide ticket booking services without completely relying on IRCTC's own frontend or getting full access to their backend systems.

This is where APIs play a crucial role in modern software development, enabling seamless communication between different systems and components.

API responds are usually in formats like JSON or XML, which are easy to read and parse by both humans and machines.

## Types of APIs
There are several types of APIs, including:
- **REST (Representational State Transfer)**: A popular architectural style for designing networked applications. RESTful APIs use standard HTTP methods (GET, POST, PUT, DELETE) and are stateless.

- **SOAP (Simple Object Access Protocol)**: A protocol for exchanging structured information in web services. SOAP APIs rely on XML and have strict standards for security and transactions.

- **GraphQL**: A query language for APIs that allows clients to request only the data they need. It provides more flexibility compared to REST by enabling clients to specify the structure of the response.

---

APIs are a fundamental building block of modern software development, enabling seamless integration and communication between diverse applications and services.

We use a backend server with a database to create APIs that can be consumed by various frontend applications, enhancing the overall user experience and functionality.

## API - ML Perspective
From a Machine Learning (ML) perspective, APIs play a crucial role in deploying and integrating ML models into applications. Here’s how APIs are relevant in the ML context:

1. **ML Model Deployment**: Once an ML model is trained, it needs to be deployed so that it can be accessed by other applications. APIs provide a way to expose the model's functionality over the web, allowing applications to send data to the model and receive predictions in return.

2. **Data Exchange**: APIs facilitate the exchange of data between the ML model and the application. For example, an application can send user input data to the ML model via an API, and the model can return predictions or classifications based on that data.