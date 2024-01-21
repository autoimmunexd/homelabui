import docker

def get_apps():
    # Create a docker client object
    client = docker.from_env()

    # Initialize an empty list to store container dictionaries
    apps = []

    # Get the list of all running containers
    all_containers = client.containers.list(all)

    # Loop through each running container
    for container in all_containers:
        # Get the name, status, and the ports of the container
        name = container.name
        status = container.status
        ports = container.ports

        # Initialize a dictionary for the current container
        container_dict = {
            "name": name,
            "status": status,
            "link": f"/static/{name.lower()}.svg",  # Assuming PNG file format
            "port": None  # Placeholder for port, to be updated below
        }

        # Loop through the ports of the container
        for container_port, port_data in ports.items():
            if port_data:
                host_port = next(iter(port_data), {}).get('HostPort', '').split('/')[0]
                # Update the port information in the container dictionary
                container_dict["port"] = host_port

        # Add the container dictionary to the list
        apps.append(container_dict)
        print(apps)
    return apps