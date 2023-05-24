import requests

headers = {'Authorization':'Bearer c73bb90914c5675cfcff6486d9ff8c74673bd681'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This Field is done" ,
    "price": 32.99
}

get_response = requests.post(endpoint, json = data, headers = headers)  # HTTP Request
print(get_response.json())
