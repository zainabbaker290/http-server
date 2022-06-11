import requests

user_id = input("enter user id:")

response = requests.get("http://127.0.0.1:5000/users/" + str(user_id))

print(response.status_code)
print(response.text)