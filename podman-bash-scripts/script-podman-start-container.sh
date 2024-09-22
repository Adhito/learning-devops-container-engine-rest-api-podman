#!/bin/bash

# Set the Podman API URL
PODMAN_API_URL="http://localhost:10001/v1.0.0"

# Define the container name and image
CONTAINER_NAME="my_nginx_container"
IMAGE="nginx:1.24.0"

# Create the Nginx container
CREATE_RESPONSE=$(curl -s -X POST "$PODMAN_API_URL/containers/create" \
-H "Content-Type: application/json" \
-d '{
  "image": "'"$IMAGE"'",
  "name": "'"$CONTAINER_NAME"'",
  "ports": {
    "80": 80
  }
}')

# Check if the container was created successfully by looking for "Id" in the response
if [[ "$CREATE_RESPONSE" == *"\"Id\":"* ]]; then
  echo "Container created successfully: $CREATE_RESPONSE"
  
  # Start the Nginx container
  START_RESPONSE=$(curl -s -X POST "$PODMAN_API_URL/containers/$CONTAINER_NAME/start")
  
  if [[ $? -eq 0 ]]; then
    echo "Container started successfully."
  else
    echo "Failed to start the container."
  fi
else
  echo "Failed to create container: $CREATE_RESPONSE"
fi
