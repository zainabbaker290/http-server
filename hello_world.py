from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello World!"

@app.route("/users", methods=["GET"])
def all_users():
    #open python file and read it
    users_file = open("users.json", "r")
    #using json loads to read from a string 
    users_object = json.load(users_file)
    return users_object

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    users_file = open("users.json", "r")
    users_object = json.load(users_file)

    #using dictionary attributes to access key and values 
    for key, value in users_object.items():
        for v in value:
            if v == user_id:
                user_returned = value
                result = key + ": " + user_returned[0] + " " + user_returned[1] + " " + user_returned[2]
                return result

if __name__ == "__main__":
    app.run()