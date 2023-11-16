import requests
import json

url = 'http://127.0.0.1:5000/predict'
data = {"year": 2021, "month": 12}

response = requests.post(url, json=data)
if response.status_code == 200:
    print(response.json())  # This will print the prediction response
else:
    print(f"Request failed with status code: {response.status_code}")
