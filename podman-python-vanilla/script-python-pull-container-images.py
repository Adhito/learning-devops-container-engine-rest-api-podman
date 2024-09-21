import requests  # Import the requests library for making HTTP requests

# Define the URL for the API endpoint to pull a specific image from a container registry
url = "http://localhost:10001/v4.0.0/libpod/images/pull?reference=docker.io%2Flibrary%2Fnginx:1.24.0"

# Define the payload for the request. This could be a string or file content, depending on the API's requirements.
# Here it's just a placeholder; replace it with actual data if needed.
payload = "<file contents here>"

# Set the request headers
headers = {
    'Content-Type': 'text/plain',  # Specify the content type of the request body
    'Accept': 'application/json'    # Indicate that we expect a JSON response
}

# Make a POST request to the specified URL with the given headers and payload
response = requests.request("POST", url, headers=headers, data=payload)

# Print the response status code
print(f"Response Status Code: {response.status_code}")

# Print the response from the server, which may contain details about the image pull operation
print(response.text)
