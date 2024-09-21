import requests  # Import the requests library to handle HTTP requests
import json      # Import the json library for working with JSON data

# Define the URL for the API endpoint to create a container named 'application-nginx-1.24.0'
url = "http://localhost:10001/containers/create?name=application-nginx-1.24.0"

# Prepare the payload as a JSON string representing the container configuration
payload = json.dumps({
    "Id": "4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92",
    "Created": "2024-09-20T09:15:54.237931385Z",
    "Path": "/docker-entrypoint.sh",
    "Args": [
        "nginx",
        "-g",
        "daemon off;"
    ],
    "State": {
        "OciVersion": "1.0.2-dev",
        "Status": "running",
        "Running": True,
        "Paused": False,
        "Restarting": False,
        "OOMKilled": False,
        "Dead": False,
        "Pid": 5813,
        "ConmonPid": 5810,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2024-09-20T09:15:54.437488847Z",
        "FinishedAt": "0001-01-01T00:00:00Z",
        "Healthcheck": {
            "Status": "",
            "FailingStreak": 0,
            "Log": None
        },
        "CgroupPath": "/user.slice/user-1000.slice/user@1000.service/user.slice/libpod-4d6afbcf669e6342da8864190234ace265dabc5d48cf57c19823fa0072f7cc92.scope"
    },
    "Image": "39286ab8a5e14aeaf5fdd6e2fac76e0c8d31a0c07224f0ee5e6be502f12e93f3",
    "ImageName": "docker.io/library/nginx:latest",
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
        "Image": "docker.io/library/nginx:latest",
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
})

# Set headers for the request to specify content type and accepted response type
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Make a POST request to the specified URL with the payload and headers
response = requests.post(url, headers=headers, data=payload)

# Print the HTTP response status code
print("Response Code:", response.status_code)

# Pretty-print the JSON response
try:
    response_data = response.json()  # Parse the response as JSON
    print(json.dumps(response_data, indent=4))  # Print formatted JSON with an indentation of 4 spaces
except json.JSONDecodeError:
    print("Response is not valid JSON:", response.text)  # Handle cases where response is not JSON
