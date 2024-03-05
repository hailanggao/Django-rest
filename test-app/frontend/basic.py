import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "This is from post "})

print(get_response.json())
# print(get_response.status_code)
