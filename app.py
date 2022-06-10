from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def all_users():
    #open python file and read it
    users_file = open("users.json", "r")
    #using json loads to read from a string 
    users_object = json.load(users_file)
    return json.dumps(users_object["friends"])

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    users_file = open("users.json", "r")
    users_object = json.load(users_file)
    list_of_users = users_object["friends"]
    for user in list_of_users:
        if user["user_id"] == str(user_id):
            return json.dumps(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    users_file = open("users.json", "a")
    users_object = json.load(users_file)
    data = request.json
    users_object.write(data)

    return json.dumps(users_object)

if __name__ == "__main__":
    app.run()