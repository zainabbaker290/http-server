import requests

response = requests.get("http://127.0.0.1:5000/users")

if response:
    print('Success! ' + str(response.status_code) )
else:
    print('An error has occurred.')

print(response.text)

