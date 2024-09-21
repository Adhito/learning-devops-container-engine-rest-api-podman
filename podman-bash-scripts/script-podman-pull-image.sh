#!/bin/bash

# Set the Podman API URL
PODMAN_API_URL="http://localhost:10001/v1.0.0"

# Define the image to pull
IMAGE="nginx:latest"

# Pull the container image
PULL_RESPONSE=$(curl -s -X POST "$PODMAN_API_URL/images/pull" \
-H "Content-Type: application/json" \
-d '{
  "image": "'"$IMAGE"'"
}')

# Check if the pull was successful by looking for "Id" in the response
if [[ "$PULL_RESPONSE" == *"\"Id\":"* ]]; then
  echo "Image pulled successfully: $PULL_RESPONSE"
else
  echo "Failed to pull image: $PULL_RESPONSE"
fi
