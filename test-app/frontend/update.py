import requests

endpoint = "http://localhost:8000/api/products/3/update/"
data = {"title": "This is view", "price": 2200.0}

get_response = requests.put(endpoint, json=data)

print(get_response.json())
