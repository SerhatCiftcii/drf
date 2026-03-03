import requests

# endpoint = "http://localhost:8000"
endpoint="https://httpbin.org/status/200"
endpoint="https://httpbin.org"
endpoint="https://httpbin.org/anything"



get_response= requests.get(endpoint,json={"query":"hello world"})  #http request

print(get_response.json())  #print the response text
