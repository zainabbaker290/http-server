from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route("/users", methods=["GET", "POST"])
def all_users():
    if request.method == "GET":
        #open python file and read it
        users_file = open("users.json", "r")
        #using json loads to read from a string 
        users_object = json.load(users_file)
        users_file.close()
        return Response(json.dumps(users_object["friends"]), status = 200)
    
    if request.method == "POST":
        users_file = open("users.json", "r")
        users_object = json.load(users_file)
        data = request.json
        users_object["friends"].append(data)
        users_file.close()
        users_file = open("users.json", "w")
        users_file.write(json.dumps(users_object))
        users_file.close()
        return Response(json.dumps(data), status=201)

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    users_file = open("users.json", "r")
    users_object = json.load(users_file)
    list_of_users = users_object["friends"]
    for user in list_of_users:
        if user["user_id"] == str(user_id):
            users_file.close()
            return json.dumps(user)
    
    return Response("user not found", status=404)

if __name__ == "__main__":
    app.run()