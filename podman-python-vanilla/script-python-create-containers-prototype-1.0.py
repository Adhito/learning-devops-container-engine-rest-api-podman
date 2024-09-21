import requests  # Import the requests library for making HTTP requests
import json      # Import the json library for handling JSON data

# Define the URL for the API endpoint to create a container named 'nginx-sample'
url = "http://localhost:10001/containers/create?name=nginx-sample"

# Prepare the payload as a JSON string representing the container configuration
payload = json.dumps({
    "ArgsEscaped": False,
    "AttachStderr": False,
    "AttachStdin": False,
    "AttachStdout": False,
    "Cmd": [
        "nginx",
        "-g",
        "daemon off;"
    ]
})

# Set the request headers indicating content type and expected response format
headers = {
    'Content-Type': 'application/json',  # Specify that the request body is JSON
    'Accept': 'application/json'          # Indicate that we expect a JSON response
}

# Make a POST request to create the container with the given headers and payload
response = requests.request("POST", url, headers=headers, data=payload)

# Print the HTTP response status code
print("Response Code:", response.status_code)

# Parse the response text as JSON
response_data = response.json()

# Pretty-print the JSON response
pretty_json = json.dumps(response_data, indent=4)
print(pretty_json)
