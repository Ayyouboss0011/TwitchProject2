#!/bin/bash

# Get a list of all Docker containers
containers=$(docker ps --format "{{.Names}}")

echo "Stopping Active VPN Containers with 'vpn' in their name:"
for container in $containers; do
    # Check if the container name contains the substring "mongo"
    if [[ "$container" == *"vpn"* ]]; then
        echo "Stopping container: $container"
        docker stop $container
        echo "Container stopped successfully."
        echo "----------------------------"
    fi
done

