import requests
import json

api_url = 'https://reqres.in/'
endpoint_url = "api'/users/2"
uri = api_url+endpoint_url


response = requests.request("GET",uri)
print(response.status_code)

