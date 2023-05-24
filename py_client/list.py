import requests
from getpass import getpass

# cfe passwrod: Jerry@22
auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your Password?\n")


auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token'] #get the token that is generated and store it in the 'token' variable
    headers = {
        "Authorization":f"Bearer {token}"
    }
endpoint = "http://localhost:8000/api/products/"

get_response = requests.get(endpoint, headers=headers)
print(get_response.json())
