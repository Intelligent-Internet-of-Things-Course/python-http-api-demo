import requests

import requests

# Target API URL
api_url = "http://127.0.0.1:7070/api/iot/inventory/location"

# Define Create Request Body as Python dictionary
request_dictionary = {
    "uuid": "l101",
    "name": "PythonTestBuilding",
    "latitude": 48.412321,
    "longitude": 10.533423211
}

# Send the POST Request with the body serialized as Json (Internally managed by the library)
response = requests.post(api_url, json=request_dictionary)

location_header = response.headers["Location"]

print(f'HTTP Response Code: {response.status_code} - Buffer Body: {response.content} - Location Header: {location_header}')