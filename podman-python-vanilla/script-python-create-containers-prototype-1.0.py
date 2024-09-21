import requests  # Import the requests library for making HTTP requests
import json      # Import the json library for handling JSON data

# Define the URL for the API endpoint to create a container named 'application-nginx-1.24.0'
url = "http://localhost:10001/containers/create?name=application-nginx-1.24.0"

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
    ],
    "Domainname": "",
    "Entrypoint": "/docker-entrypoint.sh",
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
    "Healthcheck": {
        "Status": "",
        "FailingStreak": 0,
        "Log": None
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
    },
    "Hostname": "<string>",
    "Image": "docker.io/library/nginx:1.24.0",
    "Labels": {
        "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
    },
    "MacAddress": "",
    "Name": "<string>",
    "OnBuild": [
        "<string>",
        "<string>"
    ],
    "OpenStdin": False,
    "StdinOnce": False,
    "StopSignal": "3",
    "StopTimeout": 10,
    "Tty": False,
    "User": "",
    "Volumes": None,
    "WorkingDir": "/"
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
