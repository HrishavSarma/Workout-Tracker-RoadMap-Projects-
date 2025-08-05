# Read Me first
A backend system for workout tracker app where users can sign up, log in, create plans and track progress. An API basically

# What am i doing with Flask?
Flask is a micro web framework for python
Popular for doing web development and creating APIs
    -we install flask:
        pip install flask
Flask is the server that will be running out API
    -we run:
        python main.py
    -it creates a development server for us
    -we created first root inside of flask
Other roots we can create with HTTP methods
HTTP is how we communicate data over the internet
when we create different api routes we can mark them with different methods
Methods:
    -GET to retrieve some value from server
    -POST when we want to create something new
    -PUT when we want to modify existing data
    -Delete to delete data from database or from resource we are accessing
Path Parameter
    a dynamic value we can pass in the path of a url that we will be able to acess inside of the root
Query Parameter
    whenever accessing a route, we can pass an extra value that is included after the main path
    ex: 
        "get-user/123?extra=helloworld"
        after ? we can add different query parameters
        extra = helloworld is an additional variable that we pass along through our route
Whenever we are returning data from an API we use JSON - collection of key value pairs
    we create dictionary in flask, jsonify that dictionary and thats what we return to the user, this allows flask to parse this value and return it as json data