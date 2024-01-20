import docker

def get_apps():
    # Create a docker client object
    client = docker.from_env()

    # Initialize an empty list to store container dictionaries
    apps = []

    # Get the list of all running containers
    running_containers = client.containers.list()

    # Loop through each running container
    for container in running_containers:
        # Get the name and the ports of the container
        name = container.name
        ports = container.ports

        # Initialize a dictionary for the current container
        container_dict = {
            "name": name,
            "link": f"/static/{name.lower()}.png",  # Assuming PNG file format
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

    return apps