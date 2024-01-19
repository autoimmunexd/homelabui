# #list containing dictionaries of information about each program and their coorelating links
# import docker

# # Create a docker client object
# client = docker.from_env()

# # Get the list of all containers
# containers = client.containers.list(all=True)

# # Loop through each container
# for container in containers:
#     # Get the name and the ports of the container
#     name = container.name
#     ports = container.ports

#     # Loop through the ports of the container
#     for container_port, port_data in ports.items():
#         if port_data:
#             first_value = next(iter(port_data), {}).get('HostPort', '').split('/')[0]
#             # Print the name and the ports of the container
#             print(f"{name} {first_value}")
#             break  # Break out of the inner loop after printing the first port
#returns -
# overseerr 5055
# zealous_taussig 8081
# syncthing 21027
# lidarr 8686
# prowlarr 9696
# radarr 7878
# sonarr 8989
# gluetun 6881
# homarr 7575
# netbootxyz 3000
# filebrowser 8080
# portainer 8000

apps = [
    {"name": "Plex", "link": "/static/plex.png"},
    {"name": "Overseerr", "link": "/static/overseerr.png"},
    {"name": "qBittorrent", "link": "/static/qbittorrent.png"},
    {"name": "Proxmox", "link": "/static/proxmox.png"},
    {"name": "OPNsense", "link": "/static/opnsense.png"},
    {"name": "Portainer", "link": "/static/portainer.png"},
    {"name": "Radarr", "link": "/static/radarr.png"},
    {"name": "Sonarr", "link": "/static/sonarr.png"},
    {"name": "Lidarr", "link": "/static/lidarr.png"},
    {"name": "Prowlarr", "link": "/static/prowlarr.png"},
    {"name": "Syncthing", "link": "/static/syncthing.png"},
    {"name": "Metube", "link": "/static/metube.png"}
]
