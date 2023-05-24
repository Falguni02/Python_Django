import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"
get_response = requests.post(endpoint, json={"title" : "Hello World!", "content": "Abc123", "price": "abc134"})  # HTTP Request
#print(get_response.headers)
#print(get_response.text)  # prints the raw text response
print(get_response.json())
#print(get_response.status_code)
