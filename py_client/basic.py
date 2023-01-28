import requests

endpoint = "http://localhost:8000/api/?abc=123"

get_response = requests.get(endpoint, json={'product_id': 1})
print(get_response.json())
