import requests

target_location_id = "l101"
api_url = f'http://127.0.0.1:7070/api/iot/inventory/location/{target_location_id}'

print(f'Deleting Location with id: {target_location_id}')

# Send the DELETE Request for the target URL
response = requests.delete(api_url)

print(f'HTTP Response Code: {response.status_code} - String Body: {str(response.content, "UTF-8").strip()}')
