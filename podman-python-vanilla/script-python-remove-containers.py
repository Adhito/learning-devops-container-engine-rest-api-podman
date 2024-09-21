import requests  # Import the requests library to make HTTP requests

# Define the URL for the API endpoint to delete the container named "application-nginx-1.24.0"
# Query parameters: `force=false` and `v=false`
url = "http://localhost:10001/containers/application-nginx-1.24.0?force=false&v=false"

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
print(response.text)
