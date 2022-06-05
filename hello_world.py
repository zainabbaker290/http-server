from flask import Flask
import json
from users import users

app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello World!"

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