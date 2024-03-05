import requests

endpoint = "http://localhost:8000/api/product/"
data = {"title": "This is create view", "price": 22.0}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
