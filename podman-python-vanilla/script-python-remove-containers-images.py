import requests  # Import the requests library to make HTTP requests
import json  # Import the json library for handling JSON data

# Define the URL for the API endpoint to delete the image "nginx:1.24.0"
# Query parameters: `force=false` and `noprune=false`
url = "http://localhost:10001/images/docker.io/library/nginx:1.24.0?force=false&noprune=false"

# Payload is empty because the request does not need any body content
payload = {}

# Set the headers for the request
headers = {
    'Accept': 'application/json'  # Indicate that we expect a JSON response
}

# Send a DELETE request to the specified URL with the given headers and payload
response = requests.request("DELETE", url, headers=headers, data=payload)

# Print the response status code
print(f"Response Status Code: {response.status_code}")

# Print the response text which will contain information about the result of the delete request
try:
    # Parse the JSON response
    data = response.json()
    # Pretty-print the JSON data
    pretty_json = json.dumps(data, indent=4)
    print(pretty_json)
except ValueError:
    # If the response is not JSON, just print the raw text
    print("Response is not in JSON format:")
    print(response.text)
