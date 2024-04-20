import time
import os
import subprocess

while True:
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


    # Docker-Compose-Datei neu ausführen
    result = subprocess.run(['docker-compose', '-f', '/home/ayyouboss/Desktop/docker-compose.yml', 'up', '-d'], stdout=subprocess.PIPE, text=True)

    # Fehler überprüfen
    if result.returncode != 0:
        print(f"Error: {result.returncode}")
        print(result.stdout)
    else:
        print("Docker Compose up -d succeeded.")

    print(result.stdout)
    
    
    # Kurze Wartezeit (10 Sekunden), um sicherzustellen, dass die Container gestartet wurden
    time.sleep(25)
    
    
    # Lösche alle temporären Volume Dateien
    try:
        subprocess.run(['docker', 'system', 'prune', '-a', '--volumes'], check=True, input='y', text=True)
        print("Cleanup successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error cleaning up: {e}")
    
    
    
    #######################################################################################################
    #######################################################################################################
    
    # Führe den pkill -f chrome Befehl auf jedem Container aus, um Chrome ohne Meldung zu starten
    container_ids = subprocess.check_output(['docker', 'ps', '-q'], text=True).split()

    command_to_execute = 'pkill -f chrome'

    def execute_command_in_container(container_id, command):
        try:
            subprocess.run(['docker', 'exec', container_id, *command.split()], check=True)
            print(f"Command executed successfully in container {container_id}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command in container {container_id}: {e}")

    for container_id in container_ids:
        execute_command_in_container(container_id, command_to_execute)


    #######################################################################################################
    #######################################################################################################
    
    # Lösche das Terminal
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')
    clear_terminal()
    
    
    # Starte einen Timer im Terminal
    print("Der nächste Refresh erfolgt in: ")
    for i in range(500, 0, -1):
        print(f"Sekunde {i}", end='\r')
        time.sleep(1)
        

