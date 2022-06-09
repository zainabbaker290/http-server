import requests

user_id = input("enter user you want to search for ")

response = requests.get("http://127.0.0.1:5000/users/", params =  str(user_id))

print(response.status_code)
print(response.text)