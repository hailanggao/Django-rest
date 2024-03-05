import requests


try:
    product_id = int(input("Which one you want to delete:\n"))
except:
    product_id = None
    print(f"Not a valid id")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)

    print(get_response.status_code, get_response.status_code == 204)
