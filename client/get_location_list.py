import requests

# Target URL
api_url = "http://127.0.0.1:7070/api/iot/inventory/location"

# Send the DELETE Request for the target URL
response = requests.get(api_url)

# Read Status code and Body in 3 different ways (Byte Buffer, String, Json)
print(f'HTTP Response Code: {response.status_code} - Buffer Body: {response.content}')
print(f'HTTP Response Code: {response.status_code} - String Body: {str(response.content, "UTF-8").strip()}')
print(f'HTTP Response Code: {response.status_code} - Json Parsed Body (Type: {type(response.json())}): {response.json()}')