This code does the following things:

1) Stop all running Containers
2) Remove all stopped containers
3) Redeploy the docker-compose file --> Redeploying all Containers freshly again
4) Delete all temp volume files
5) execute the pkill command to restart chrome on every container
6) Start timer
