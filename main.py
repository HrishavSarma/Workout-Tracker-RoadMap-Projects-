from flask import Flask, request, jsonify #These the dependencies
 
app = Flask(__name__) #Flask application

#creating roots

## DEMO ##
# @app.route("/") #root is what comes after the slash
# def home():
#     return "Home"
## DEMO ##

# a complicated get root
@app.route("/get-user/<user_id>") #we implement path parameter
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Troy",
        "email": "troystyles2020@gmail.com"
    }

    #How we access the query parameters
    extra = request.args.get("extra") #args stores all the query parameters in a dictionary
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200 #200 default status code for success


## POST route ##
@app.route("/create-user", methods=["POST"]) #since not using default GET request, we specify the accpeted method that we write inside the array, we could do like ["POST", "GET"]
def create_user():
    # if request.method == "POST": #to check what method being used
    data = request.get_json() #gives all the json data that we passed in the request

    return jsonify(data), 201
        

if __name__ == "__main__":      #running our flask application
    app.run(debug=True)