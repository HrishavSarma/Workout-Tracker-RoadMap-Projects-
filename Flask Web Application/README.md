This folder is following the youtube tutorial for creating a python website
https://youtu.be/dam0GPOAvVI?si=UP4VihSWbw-qyXy0

This is to understand the working of websites and their backend databases storage and etc.

-We create directories
    -Flask Web Application(the main folder): stores our main application
    -website: stores all the code for the website
    -main.py: when we want the run the web server
    -static:
    -templates:
    -__init__.py: this makes the website folder a python package
    -auth.py:
    -models.py: we use this for storing database models
    -views.py: stores main views where the URL endpoints for the actual functioning frontend aspects of the website
-setting up flask
    -installed modules
        -flask-login
        -flask-sqlalchemy: database thing we can use wrapper for sql to make it easier to create database models, delete models, add models
-we are setting up routes for the website in the views.py file
    -routes are usually where the users go to
    -we define that the file is a blueprint of the application
        -it has a bunch of routes inside 
        -has all the URLS defined
        -way to seperate the app out
        -so that we dont have all of the views defined in one file
        -but defined in multiple files split up and nicely organised
-we made the first blueprints defined now we need to register these blueprints to the init file
-app.register_blueprint(auth, url_prefix="/auth/")
    -this means if
        we were to go to the website like ..../auth/hello
        then we will be able to access the route in the     auth.py file
        if it was like @auth.route("hello")