from pickle import TRUE
from flask import Flask, request
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-my-secret-key"

@app.route("/users", methods=["GET"])
def all_users():
    #open python file and read it
    users_file = open("users.json", "r")
    #using json loads to read from a string 
    users_object = json.load(users_file)
    return json.dumps(users_object)

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    users_file = open("users.json", "r")
    users_object = json.load(users_file)

    #using dictionary attributes to access key and values 
    for key in users_object.keys():
        if key == user_id:
            return json.dumps(users_object[key])

@app.route("/add_user", methods=["POST"])
def add_user():
    users_file = open("users.json", "a")
    users_object = json.load(users_file)
    data = request.json
    users_object.write(data)

    return json.dumps(users_object)

if __name__ == "__main__":
    app.run()