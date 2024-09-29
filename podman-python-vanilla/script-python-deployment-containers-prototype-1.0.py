import requests  # Import the requests library to handle HTTP requests
import json      # Import the json library for working with JSON data

def print_line_separator():
    # Get the current line width in characters
    import shutil
    terminal_width = shutil.get_terminal_size().columns

    # Print '=' until the end of the line
    print('=' * terminal_width)


def get_list_container(url):
    """Fetch container information from the specified URL and print filtered data."""
    
    ## Print Stage / Function
    print(" ")
    print("Stage : Listing All Containers ...")
    print_line_separator()

    url = f"{url}/containers/json?all=true&external=false&size=false"

    payload = {}
    headers = {
        'Accept': 'application/json'  
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(f"Response Status Code: {response.status_code}")
    print(" ")

    try:
        json_data = response.json()
        filtered_data = []
        
        # Iterate through each container in the JSON response
        for container in json_data:
            # Extract the desired fields
            container_info = {
                'Id': container.get('Id'),
                'Names': container.get('Names'),
                'Image': container.get('Image'),
                'Ports': container.get('Ports')
            }
            filtered_data.append(container_info) 

        print(json.dumps(filtered_data, indent=4))

    except ValueError:
        print("Response is not valid JSON.")


def get_list_container_image(url):
    """Fetch image information from the specified URL and print filtered data."""
    
    ## Print Stage / Function
    print(" ")
    print("Stage : Listing All Container Images  ...")
    print_line_separator()

    url = f"{url}/images/json?all=false&digests=false"

    payload = {}
    headers = {
        'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(f"Response Status Code: {response.status_code}")
    print(" ")
    
    try:
        json_data = response.json()
        filtered_data = []
        
        # Iterate through each container image in the JSON response
        for container_image in json_data:
            # Extract the desired fields
            container_image_info = {
                'Id': container_image.get('Id'),
                'RepoTags': container_image.get('RepoTags'),
                'Names': container_image.get('Names'),
                'Containers': container_image.get('Containers')
            }
            filtered_data.append(container_image_info) 

        print(json.dumps(filtered_data, indent=4))

    except ValueError:
        print("Response is not valid JSON.")


def stop_container(url, container_name, timeout=15):
    """Stop a specified container and print the response."""
    
    ## Print Stage / Function
    print(" ")
    print(f"Stage : Stopping Container  ... ")
    print_line_separator()
    print(f"LOG : Stopping Container {container_name} .. ")

    url = f"{url}/containers/{container_name}/stop?t={timeout}"

    payload = {}
    headers = {
        'Accept': 'application/json'  
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(f"Response Status Code: {response.status_code}")
    print(" ")

    try:
        # Parse the response as JSON
        response_data = response.json()             
        print(json.dumps(response_data, indent=4)) 
    except json.JSONDecodeError:
        print("Response is not valid JSON:", response.text) 


def start_container(container_name):
    """Start a specified container and print the response."""
    
    ## Print Stage / Function
    print(" ")
    print(f"Stage : Starting Container  ... ")
    print_line_separator()
    print("LOG : Starting Container",container_name, " ... ")
    print(f"LOG : Starting Container {container_name} .. ")

    # Define the URL for the API endpoint to start the specified container
    url = f"http://localhost:10001/containers/{container_name}/start"

    # Payload is empty because the request does not need any body content
    payload = {}

    # Set the headers for the request
    headers = {
        'Accept': 'application/json'  # Indicate that we expect a JSON response
    }

    # Send a POST request to the specified URL with the given headers and payload
    response = requests.post(url, headers=headers, data=payload)

    # Print the response status code
    print(f"Response Status Code: {response.status_code}")

    # Print the response text which will contain information about the result of the start request
    # print(response.text)

    # Print the response text which will contain information about the result of the start request
    try:
        response_data = response.json()             # Parse the response as JSON
        print(json.dumps(response_data, indent=4))  # Print formatted JSON with an indentation of 4 spaces
    except json.JSONDecodeError:
        print("Response is not valid JSON:", response.text)  # Handle cases where response is not JSON


def delete_container(container_name, force=False, v=False):
    """
    Delete a specified container using the Docker API.

    Args:
        container_name (str): The name of the container to delete.
        force (bool): Whether to force the removal of the container (default is False).
        v (bool): Whether to remove volumes associated with the container (default is False).

    Returns:
        None
    """
    ## Print Stage / Function
    print(" ")
    print("Stage : Deleting Containers ...")
    print_line_separator()

    # Define the URL for the API endpoint to delete the specified container
    url = f"http://localhost:10001/containers/{container_name}?force={str(force).lower()}&v={str(v).lower()}"

    # Payload is empty because the request does not need any body content
    payload = {}

    # Set the headers for the request
    headers = {
        'Accept': 'application/json'  # Indicate that we expect a JSON response
    }

    # Send a DELETE request to the specified URL with the given headers and payload
    response = requests.delete(url, headers=headers, data=payload)

    # Print the response status code
    print(f"Response Status Code: {response.status_code}")

    # # Print the response text which will contain information about the result of the delete request
    # try:
    #     # Parse the JSON response
    #     data = response.json()
    #     # Pretty-print the JSON data
    #     pretty_json = json.dumps(data, indent=4)
    #     print(pretty_json)
    # except ValueError:
    #     # If the response is not JSON, just print the raw text
    #     print("Response is not in JSON format:")
    #     print(response.text)

    # Pretty-print the JSON response
    try:
        response_data = response.json()             # Parse the response as JSON
        print(json.dumps(response_data, indent=4))  # Print formatted JSON with an indentation of 4 spaces
    except json.JSONDecodeError:
        print("Response is not valid JSON:", response.text)  # Handle cases where response is not JSON


def delete_container_image(image_name, force=False, noprune=False):
    """Delete a specified Docker image and print the response."""
    
    ## Print Stage / Function
    print(" ")
    print("Stage : Deleting  Container Images  ...")
    print_line_separator()

    # Define the URL for the API endpoint to delete the specified image
    url = f"http://localhost:10001/images/docker.io/library/{image_name}?force={str(force).lower()}&noprune={str(noprune).lower()}"

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


def pull_container_image(image_reference):
    """Pull a specified image from a container registry and print the response."""
    
    ## Print Stage / Function
    print(" ")
    print("Stage : Pulling Container Images ...")
    print_line_separator()

    # Define the URL for the API endpoint to pull the specified image
    url = f"http://localhost:10001/v4.0.0/libpod/images/pull?reference={image_reference}"

    # Define the payload for the request (placeholder; adjust as needed)
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
    # print(response.text)

    # Print the response from the server, which may contain details about the image pull operation
    try:
        response_data = response.json()             # Parse the response as JSON
        print(json.dumps(response_data, indent=4))  # Print formatted JSON with an indentation of 4 spaces
    except json.JSONDecodeError:
        print("Response is not valid JSON:", response.text)  # Handle cases where response is not JSON


def create_container(container_name, payload):
    """
    Create a container using the specified container name and payload.

    Args:
        container_name (str): The name of the container to create.
        payload (dict): A dictionary representing the container configuration.

    Returns:
        None
    """

    ## Print Stage / Function
    print(" ")
    print("Stage : Creating Containers ...")
    print_line_separator()

    # Define the URL for the API endpoint to create a container
    url = f"http://localhost:10001/containers/create?name={container_name}"

    # Convert the payload dictionary to a JSON string
    payload_json = json.dumps(payload)

    # Set headers for the request to specify content type and accepted response type
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Make a POST request to the specified URL with the payload and headers
    response = requests.post(url, headers=headers, data=payload_json)

    # Print the HTTP response status code
    print("Response Code:", response.status_code)

    # Pretty-print the JSON response
    try:
        response_data = response.json()             # Parse the response as JSON
        print(json.dumps(response_data, indent=4))  # Print formatted JSON with an indentation of 4 spaces
    except json.JSONDecodeError:
        print("Response is not valid JSON:", response.text)  # Handle cases where response is not JSON


# Main Function usage
if __name__ == "__main__":

    # Define the URL for the Podman RESTAPI 
    url_base = "http://localhost:10001"

    # # Define the URL for the HTTP request
    # url_container = "http://localhost:10001/containers/json?all=true&external=false&size=false"

    # # Define the URL for the API endpoint For Container Images
    # url_container_image = "http://localhost:10001/images/json?all=false&digests=false"

    # Define & Prepare the payload as a dictionary representing the container configuration
    # 1. Replace Image ID with image name with version ( EX : "Image" : "docker.io/library/nginx:1.24.0",) otherwise it may cause not found error 
    # 2. Comment the "State" subsection since the container hasn't run yet (No state)
    # 3. Replace true with True
    # 4. Replace false with False
    # 5. Replace null with None

    payload = {
            "Id": "4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92",
            "Created": "2024-09-20T09:15:54.237931385Z",
            "Path": "/docker-entrypoint.sh",
            "Args": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            # "State": {
            #     "OciVersion": "1.0.2-dev",
            #     "Status": "running",
            #     "Running": True,
            #     "Paused": False,
            #     "Restarting": False,
            #     "OOMKilled": False,
            #     "Dead": False,
            #     "Pid": 5813,
            #     "ConmonPid": 5810,
            #     "ExitCode": 0,
            #     "Error": "",
            #     "StartedAt": "2024-09-20T09:15:54.437488847Z",
            #     "FinishedAt": "0001-01-01T00:00:00Z",
            #     "Healthcheck": {
            #         "Status": "",
            #         "FailingStreak": 0,
            #         "Log": None
            #     },
            #     "CgroupPath": "/user.slice/user-1000.slice/user@1000.service/user.slice/libpod-4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92.scope"
            # },
            "Image": "docker.io/library/nginx:1.24.0",
            "ImageName": "docker.io/library/nginx:1.24.0",
            "Rootfs": "",
            "Pod": "",
            "ResolvConfPath": "/run/user/1000/containers/overlay-containers/4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92/userdata/resolv.conf",
            "HostnamePath": "/run/user/1000/containers/overlay-containers/4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92/userdata/hostname",
            "HostsPath": "/run/user/1000/containers/overlay-containers/4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92/userdata/hosts",
            "StaticDir": "/home/vagrant/.local/share/containers/storage/overlay-containers/4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92/userdata",
            "OCIConfigPath": "/home/vagrant/.local/share/containers/storage/overlay-containers/4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92/userdata/config.json",
            "OCIRuntime": "crun",
            "ConmonPidFile": "/run/user/1000/containers/overlay-containers/4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92/userdata/conmon.pid",
            "PidFile": "/run/user/1000/containers/overlay-containers/4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92/userdata/pidfile",
            "Name": "intelligent_jemison",
            "RestartCount": 0,
            "Driver": "overlay",
            "MountLabel": "",
            "ProcessLabel": "",
            "AppArmorProfile": "",
            "EffectiveCaps": [
                "CAP_CHOWN",
                "CAP_DAC_OVERRIDE",
                "CAP_FOWNER",
                "CAP_FSETID",
                "CAP_KILL",
                "CAP_NET_BIND_SERVICE",
                "CAP_SETFCAP",
                "CAP_SETGID",
                "CAP_SETPCAP",
                "CAP_SETUID",
                "CAP_SYS_CHROOT"
            ],
            "BoundingCaps": [
                "CAP_CHOWN",
                "CAP_DAC_OVERRIDE",
                "CAP_FOWNER",
                "CAP_FSETID",
                "CAP_KILL",
                "CAP_NET_BIND_SERVICE",
                "CAP_SETFCAP",
                "CAP_SETGID",
                "CAP_SETPCAP",
                "CAP_SETUID",
                "CAP_SYS_CHROOT"
            ],
            "ExecIDs": [],
            "GraphDriver": {
                "Name": "overlay",
                "Data": {
                    "LowerDir": "/home/vagrant/.local/share/containers/storage/overlay/426903844bc9405bb0be130283e15486acf1dd71cd4daae8487a0c9149fef0b6/diff:/home/vagrant/.local/share/containers/storage/overlay/89fdb3e0e550a324a53ee11b460448cb8fda28b51f0db3d9a54997ce0f81ca17/diff:/home/vagrant/.local/share/containers/storage/overlay/d72f76042e0998bf0faceb447863c0f0c4eb7ccb6d2ba6bc653c3b1ccaa6c580/diff:/home/vagrant/.local/share/containers/storage/overlay/a468e23a8178f533ae3063897246599a28a06d2ff56c6ce2110754bcd3820c7f/diff:/home/vagrant/.local/share/containers/storage/overlay/a8ad3297ad18e8b2f0f0a2d96db12eaf3180d8addf7f1b5f3f62a567ceae3111/diff:/home/vagrant/.local/share/containers/storage/overlay/07d71a9dbc32a697080301e84bbf94972fe090a49d0fb5c920d90009a01b7ec9/diff:/home/vagrant/.local/share/containers/storage/overlay/8e2ab394fabf557b00041a8f080b10b4e91c7027b7c174f095332c7ebb6501cb/diff",
                    "MergedDir": "/home/vagrant/.local/share/containers/storage/overlay/1544b4aaed84b2ce4def1bf7a678226637551aa7e36004e5a30c2bbca95a18ef/merged",
                    "UpperDir": "/home/vagrant/.local/share/containers/storage/overlay/1544b4aaed84b2ce4def1bf7a678226637551aa7e36004e5a30c2bbca95a18ef/diff",
                    "WorkDir": "/home/vagrant/.local/share/containers/storage/overlay/1544b4aaed84b2ce4def1bf7a678226637551aa7e36004e5a30c2bbca95a18ef/work"
                }
            },
            "Mounts": [],
            "Dependencies": [],
            "NetworkSettings": {
                "EndpointID": "",
                "Gateway": "",
                "IPAddress": "",
                "IPPrefixLen": 0,
                "IPv6Gateway": "",
                "GlobalIPv6Address": "",
                "GlobalIPv6PrefixLen": 0,
                "MacAddress": "",
                "Bridge": "",
                "SandboxID": "",
                "HairpinMode": False,
                "LinkLocalIPv6Address": "",
                "LinkLocalIPv6PrefixLen": 0,
                "Ports": {
                    "80/tcp": [
                        {
                            "HostIp": "",
                            "HostPort": "8081"
                        }
                    ]
                },
                "SandboxKey": "/run/user/1000/netns/cni-10376f1b-5734-6f43-0168-f6bded3cadbf"
            },
            "ExitCommand": [
                "/usr/bin/podman",
                "--root",
                "/home/vagrant/.local/share/containers/storage",
                "--runroot",
                "/run/user/1000/containers",
                "--log-level",
                "warning",
                "--cgroup-manager",
                "systemd",
                "--tmpdir",
                "/run/user/1000/libpod/tmp",
                "--runtime",
                "crun",
                "--storage-driver",
                "overlay",
                "--events-backend",
                "journald",
                "container",
                "cleanup",
                "4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92"
            ],
            "Namespace": "",
            "IsInfra": False,
            "Config": {
                "Hostname": "4d6afbcf669e",
                "Domainname": "",
                "User": "",
                "AttachStdin": False,
                "AttachStdout": False,
                "AttachStderr": False,
                "Tty": False,
                "OpenStdin": False,
                "StdinOnce": False,
                "Env": [
                    "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                    "TERM=xterm",
                    "container=podman",
                    "DYNPKG_RELEASE=2~bookworm",
                    "NGINX_VERSION=1.27.1",
                    "NJS_VERSION=0.8.5",
                    "NJS_RELEASE=1~bookworm",
                    "PKG_RELEASE=1~bookworm",
                    "HOME=/root",
                    "HOSTNAME=4d6afbcf669e"
                ],
                "Cmd": [
                    "nginx",
                    "-g",
                    "daemon off;"
                ],
                "Image": "docker.io/library/nginx:1.24.0",
                "Volumes": None,
                "WorkingDir": "/",
                "Entrypoint": "/docker-entrypoint.sh",
                "OnBuild": None,
                "Labels": {
                    "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
                },
                "Annotations": {
                    "com.docker.official-images.bashbrew.arch": "amd64",
                    "io.container.manager": "libpod",
                    "io.kubernetes.cri-o.Created": "2024-09-20T09:15:54.237931385Z",
                    "io.kubernetes.cri-o.TTY": "false",
                    "io.podman.annotations.autoremove": "FALSE",
                    "io.podman.annotations.init": "FALSE",
                    "io.podman.annotations.privileged": "FALSE",
                    "io.podman.annotations.publish-all": "FALSE",
                    "org.opencontainers.image.base.digest": "sha256:903d3225acecaa272bbdd7273c6c312c2af8b73644058838d23a8c9e6e5c82cf",
                    "org.opencontainers.image.base.name": "debian:bookworm-slim",
                    "org.opencontainers.image.created": "2024-08-14T21:31:12Z",
                    "org.opencontainers.image.revision": "e78cf70ce7b73a0c9ea734c9cf8aaaa283c1cc5a",
                    "org.opencontainers.image.source": "https://github.com/nginxinc/docker-nginx.git#e78cf70ce7b73a0c9ea734c9cf8aaaa283c1cc5a:mainline/debian",
                    "org.opencontainers.image.stopSignal": "3",
                    "org.opencontainers.image.url": "https://hub.docker.com/_/nginx",
                    "org.opencontainers.image.version": "1.27.1"
                },
                "StopSignal": 3,
                "CreateCommand": [
                    "podman",
                    "run",
                    "-d",
                    "-p",
                    "8081:80",
                    "nginx"
                ],
                "Umask": "0022",
                "Timeout": 0,
                "StopTimeout": 10
            },
            "HostConfig": {
                "Binds": [],
                "CgroupManager": "systemd",
                "CgroupMode": "private",
                "ContainerIDFile": "",
                "LogConfig": {
                    "Type": "journald",
                    "Config": None,
                    "Path": "",
                    "Tag": "",
                    "Size": "0B"
                },
                "NetworkMode": "slirp4netns",
                "PortBindings": {
                    "80/tcp": [
                        {
                            "HostIp": "",
                            "HostPort": "8081"
                        }
                    ]
                },
                "RestartPolicy": {
                    "Name": "",
                    "MaximumRetryCount": 0
                },
                "AutoRemove": False,
                "VolumeDriver": "",
                "VolumesFrom": None,
                "CapAdd": [],
                "CapDrop": [
                    "CAP_AUDIT_WRITE",
                    "CAP_MKNOD",
                    "CAP_NET_RAW"
                ],
                "Dns": [],
                "DnsOptions": [],
                "DnsSearch": [],
                "ExtraHosts": [],
                "GroupAdd": [],
                "IpcMode": "private",
                "Cgroup": "",
                "Cgroups": "default",
                "Links": None,
                "OomScoreAdj": 0,
                "PidMode": "private",
                "Privileged": False,
                "PublishAllPorts": False,
                "ReadonlyRootfs": False,
                "SecurityOpt": [],
                "Tmpfs": {},
                "UTSMode": "private",
                "UsernsMode": "",
                "ShmSize": 65536000,
                "Runtime": "oci",
                "ConsoleSize": [
                    0,
                    0
                ],
                "Isolation": "",
                "CpuShares": 0,
                "Memory": 0,
                "NanoCpus": 0,
                "CgroupParent": "user.slice",
                "BlkioWeight": 0,
                "BlkioWeightDevice": None,
                "BlkioDeviceReadBps": None,
                "BlkioDeviceWriteBps": None,
                "BlkioDeviceReadIOps": None,
                "BlkioDeviceWriteIOps": None,
                "CpuPeriod": 0,
                "CpuQuota": 0,
                "CpuRealtimePeriod": 0,
                "CpuRealtimeRuntime": 0,
                "CpusetCpus": "",
                "CpusetMems": "",
                "Devices": [],
                "DiskQuota": 0,
                "KernelMemory": 0,
                "MemoryReservation": 0,
                "MemorySwap": 0,
                "MemorySwappiness": 0,
                "OomKillDisable": False,
                "PidsLimit": 2048,
                "Ulimits": [],
                "CpuCount": 0,
                "CpuPercent": 0,
                "IOMaximumIOps": 0,
                "IOMaximumBandwidth": 0,
                "CgroupConf": None
            }
    }

    # Call the function to get and print container information
    get_list_container(url_base)

    # Call the function to get and print image information
    get_list_container_image(url_base)

    # Call the function to stop the container based on the parameter"
    stop_container(url_base, "application-nginx-1.24.0", timeout=15)

    # # Call the function to delete the container
    # delete_container("application-nginx-1.24.0")

    # # Call the function to delete the image "nginx:1.24.0"
    # delete_container_image("nginx:1.24.0", force=False, noprune=False)

    # # Call the function to pull the image "docker.io/library/nginx:1.24.0"
    # pull_container_image("docker.io/library/nginx:1.24.0")

    # # Call the function to create the container
    # create_container("application-nginx-1.24.0", payload)

    # # Call the function to start the container named "application-nginx-1.24.0"
    # start_container("application-nginx-1.24.0")

    # # Call the function to get and print container information
    # get_list_container(url_container)