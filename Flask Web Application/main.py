# we import the website package grab the create_app and use it to create an application
from website import create_app

app = create_app()

if __name__ == "__main__" : #it will run when we want it to run not when we are trying to import the file
    app.run(debug=True) #changes in the code will make it automatically rerun the webserver