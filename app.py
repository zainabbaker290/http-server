from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def all_users():
    #open python file and read it
    users_file = open("users.json", "r")
    #using json loads to read from a string 
    users_object = json.load(users_file)
    users_file.close()
    return json.dumps(users_object["friends"])

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    users_file = open("users.json", "r")
    users_object = json.load(users_file)
    list_of_users = users_object["friends"]
    for user in list_of_users:
        if user["user_id"] == str(user_id):
            users_file.close()
            return json.dumps(user)

@app.route("/add_user", methods=["GET", "POST"])
def add_new_user():

    if request.method == "POST":
        users_file = open("users.json", "r")
        users_object = json.load(users_file)
        data = request.json
        users_object["friends"].append(data)
        users_file.close()
        users_file = open("users.json", "w")
        users_file.write(json.dumps(users_object))
        users_file.close()
        return Response(users_object, status=201)

if __name__ == "__main__":
    app.run()