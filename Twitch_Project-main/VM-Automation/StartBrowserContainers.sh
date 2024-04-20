#!/bin/bash

# Get a list of all Docker containers
containers=$(docker ps -a --format "{{.Names}}")

echo "Starting Inactive Browser Containers with 'b' in their name:"
for container in $containers; do
    # Check if the container name contains the substring "mongo"
    if [[ "$container" == *"b"* ]]; then
        # Check if the container is not currently running
        if [ "$(docker inspect -f '{{.State.Running}}' $container)" == "false" ]; then
            echo "Starting container: $container"
            docker start $container
            echo "Container started successfully."
            echo "----------------------------"
        else
            echo "Skipping already running container: $container"
        fi
    fi
done

