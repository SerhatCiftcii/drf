import requests

endpoint="http://localhost:8000/products/"

get_reponse= requests.get(endpoint , json={"product_id":123})

print(get_reponse.json())