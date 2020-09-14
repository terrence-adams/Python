Tools:
To Do:
Authentication
Create Session
Create Posts
Load Json
Write Json to File
Write Json to Screen
Return Response
Repeat...


Create Session:
    Log in to authenticate:
        Log in must return a header and map that to a value for all subsequent http methods
    Create session:
        Session will be initialized one per lender.
        Each session requires a bearer token for subsequent requests

    Return Session:
        We will return the session as a method in the case of a session generator
    End session:
        garbage collection, it would end sessions and free resources
        Sessions should be created in context, which would address garbage collection
    Each session authenticates once, but multiple calls are made during that session.
        Session1.Request.Post()
        Session1.Request.Get() etc...
    For API testing, credentials are stored.
    ? Can they be stored at release pipeline level as variables and passed into the script?
    In order to be modular:
        Constructor should take a parameter of environment string and set the values.


Workflow_________________
Create Session
Authenticate
Receive Response
Store authentication token in response
set Authentication Token as property of Session class

***********
Session Class:
    Constructor()
        pass in creds and url for authentication
    P:
        url for log in
    P:
        credentials
    P:
        response
    P:
        bearer token from response
    P:
        error property for non 200 responses
    Internal class vars '_'
    Set at time of construction and response assignment
    M:
        Parse bearer token from response
        set token to _token property

