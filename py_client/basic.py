import requests

endpoint = "http://localhost:8000/api/create/"

data = {
    "title": "hello",
    "content": "this is a product",
    "price": 20
}

response = requests.post(endpoint, json=data)

print(response.status_code)
print(response.json())