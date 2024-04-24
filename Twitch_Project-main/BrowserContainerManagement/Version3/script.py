import time
import os
import subprocess
from run_docker_compose import run_docker_compose
from restart_chrome import restart_chrome
from restartVPNxBrowser import restartVPNxBrowser

# Docker-Befehl "docker stop" für alle laufenden Container
running_containers = subprocess.check_output(['docker', 'ps', '-q'], text=True).splitlines()
for container_id in running_containers:
    subprocess.run(['docker', 'stop', container_id])

# Docker-Befehl "docker rm" für alle Container
all_containers = subprocess.check_output(['docker', 'ps', '-aq'], text=True).splitlines()
for container_id in all_containers:
    subprocess.run(['docker', 'rm', container_id])

# Kurze Wartezeit (5 Sekunden), um sicherzustellen, dass die Container gelöscht wurden
time.sleep(5)

# Docker-Befehl "docker ps -a" zur Überprüfung
result = subprocess.run(['docker', 'ps', '-a'], stdout=subprocess.PIPE, text=True)

# Ausgabe anzeigen
print(result.stdout)

# Führe alle Docker Compose files aus
run_docker_compose()

while True:
    container_ids = subprocess.check_output(['docker', 'ps', '-q'], text=True).split()
    command_to_execute = 'pkill -f chrome'

    def restart_chrome_container(container_id, command):
        try:
            subprocess.run(['docker', 'exec', container_id, *command.split()], check=True)
            print(f"Command executed successfully in container {container_id}")
            
        except subprocess.CalledProcessError as e:
            print(f"Error executing command in container {container_id}: {e}")

    for container_id in container_ids:
        restart_chrome_container(container_id, command_to_execute)
        time.sleep(15)

    
        

