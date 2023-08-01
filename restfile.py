import requests


endpoint = "https://httpbin.org/"
endpoint2 = "https://httbin.org/status/200"
endpoint3 = "https://httpbin.org/anything"
response = requests.get(endpoint3, json={'password': 123})
print(response.json())
