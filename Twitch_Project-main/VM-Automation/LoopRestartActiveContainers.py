import docker

def restart_active_containers():
    # Create a Docker client
    client = docker.from_env()

    # Get a list of all containers
    containers = client.containers.list(all=True)

    if containers:
        print("Restarting Active Docker Containers:")
        for container in containers:
            if container.status == 'running':
                if 'portainer' in container.name.lower():
                    print(f"Skipping Portainer container: {container.name}")
                else:
                    print(f"Restarting container: {container.name}")
                    container.restart()
                    print(f"Container restarted successfully.")
                print("----------------------------")
            else:
                print(f"Skipping non-active container: {container.name}")
    else:
        print("No Docker containers found.")

if __name__ == "__main__":
    restart_active_containers()

