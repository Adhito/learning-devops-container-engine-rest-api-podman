
import requests  # Import the requests library for making HTTP requests
import json      # Import the json library for handling JSON data

# Define the URL for the API endpoint
url = "http://localhost:10001/images/json?all=false&digests=false"

# Define any payload (data to send with the request); in this case, it's empty
payload = {}

# Set the request headers; we're specifying that we want a JSON response
headers = {
    'Accept': 'application/json'
}

# Make a GET request to the specified URL with the given headers and payload
response = requests.request("GET", url, headers=headers, data=payload)

# Parse the JSON response into a Python dictionary
data = response.json()

# Convert the Python dictionary back into a formatted JSON string for pretty-printing
pretty_json = json.dumps(data, indent=4)

# Print the nicely formatted JSON output
print(pretty_json)
