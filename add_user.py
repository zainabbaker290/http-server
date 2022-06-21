import requests

user_id = input("user_id: ")
name = input("name: ")
dob = input("dob: ")
new_user = {"user_id": str(user_id), "name": str(name), "dob": str(dob)}
user_id = requests.post('http://127.0.0.1:5000/users', json= new_user)

print(user_id.status_code)
print(user_id.text)