from flask import Flask
import json

app = Flask(__name__)

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

@app.route("/all_users")
def all_users():
    json_dump_users = json.dumps(users)
    json_object_users = json.loads(json_dump_users)
    return json_object_users

@app.route("/get_user/<user_id>")
def get_user(user_id):
    user_returned = None
    json_dump_users = json.dumps(users)
    json_object_users = json.loads(json_dump_users)

    for key, value in json_object_users.items():
        for v in value:
            if v == user_id:
                return key

if __name__ == "__main__":
    app.run()