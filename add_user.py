import requests

user_id = input("user_id: ")

user_id = requests.post('http://127.0.0.1:5000/add_user', data={"user_id": str(user_id)})
