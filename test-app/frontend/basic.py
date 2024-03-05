import requests

enndpoint = "http://localhost:8000/api/"

get_response = requests.get(enndpoint, params={"id": 1}, json={"query": "Hello"})

print(get_response.json())
# print(get_response.status_code)
