from podman import PodmanClient

# Connect to the Podman socket on port 9090
client = PodmanClient(base_url='http://localhost:10001/v1.0/libpod')

try:
    # Create an Nginx container with version 1.24.0
    container = client.containers.create(
        image='nginx:1.24.0',  # Use a valid Nginx version tag
        name='my-nginx',       # Name the container
        ports={'80/tcp': 8080}  # Map port 80 in the container to port 8080 on the host
    )

    # Start the container
    container.start()

    print("Nginx 1.24.0 container started!")
    print("Access it at http://localhost:8080")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Cleanup: Uncomment if you want to remove the container after running
    # container.remove(force=True)
    pass