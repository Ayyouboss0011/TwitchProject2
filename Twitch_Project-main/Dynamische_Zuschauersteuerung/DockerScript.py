import subprocess
from datetime import datetime
import random
import time 
import re

def getTime(): # Die Aktuelle Zeit wird erfasst
    current_time = datetime.now().hour
    if current_time == 0:
        return 24
    else:
        return current_time

def count_all_containers(): # Die (Roh-)Anzahl der Container wird erfasst --> Wird für die Berechnung der Graphenskalierung verwendet
    try:
        cmd = "docker container ls -a --format '{{.Names}}'"
        containers_output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        container_names = containers_output.strip().split('\n')

        if not container_names:
            print("Keine Container gefunden.")
            return 0  # Keine Container gefunden

        pattern = r'^b\d+$' 
        filtered_containers = [name for name in container_names if re.match(pattern, name)]

        return len(filtered_containers)
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim empfangen der Containernamen: {e}")
        return None

count = count_all_containers()
if count is not None:
    print(f"Anzahl der verfügbaren Browser-Container: {count}")


def GetAnzahlDocker(): # Anzahl der zu schaltenden Dockercontainer wird ermittelt
    x = getTime()
    print(f"Die aktuelle Uhrzeit (in ganzen Stunden) ist: {x} Uhr")
    if x is not None:
        ContainerCount = count_all_containers()
        AnzahlDocker = int((ContainerCount / 34) * ((((((5/162792) - ((8275*(x-20))/78628536)) * (x-15) + (5/504)) * (x-10) - (20/63)) * (x-3) + 5) * (x+0.5) + 5))
        print(f"Die Aktuelle Anzahl an Dockercontainern wird auf {AnzahlDocker} gesetzt")
        return AnzahlDocker
    else:
        print("Fehler beim Abrufen der Zeit.")


#############################################################################################################################
#############################################################################################################################

# Ab hier beginnt die Steuerung der Dockercontainer.

def list_containers(): # Dockercontainer, die einen Browser enthalten (fangen mit b an) werden hier ermittelt
    try:
        cmd = "docker ps --format '{{.Names}}'"
        containers_output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        container_names = containers_output.strip().split('\n')
        pattern = r'^b\d+$'  # Container mit dem Muster "b{Zahl}" wie z.B b1, b2, b3, etc. wird erkannt

        # Filter container names based on the pattern
        filtered_containers = [name for name in container_names if re.match(pattern, name)]

        return filtered_containers
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Abrufen von Containernamen: {e}")
        return None

def stop_random_containers(number_to_stop): # Diese Funktion stopt Container (random)
    containers = list_containers()
    
    if containers:
        num_containers = len(containers)
        num_to_stop = min(num_containers, number_to_stop)
        containers_to_stop = random.sample(containers, num_to_stop)
        
        for container_id in containers_to_stop:
            stop_cmd = f"docker stop {container_id}"
            subprocess.run(stop_cmd, shell=True)
            print(f"Stopped container: {container_id}")
    else:
        print("Keine Container gefunden.")

def start_stopped_containers(number_to_start): # Gestoppte Container werden hier falls nötig gestartet
    stopped_containers = []
    try:
        cmd = "docker ps -q -f status=exited"
        containers_output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        stopped_containers = containers_output.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Abrufen von gestoppten Container-IDs: {e}")

    num_stopped = len(stopped_containers)
    
    if num_stopped > 0:
        num_to_start = min(num_stopped, number_to_start)
        containers_to_start = random.sample(stopped_containers, num_to_start)
        
        for container_id in containers_to_start:
            start_cmd = f"docker start {container_id}"
            subprocess.run(start_cmd, shell=True)
            print(f"Gestarteter Container: {container_id}")
    else:
        print("Keine gestoppte Container vorhanden.")

MAX_ATTEMPTS = 1  # Maximale Anzahl an Versuchen die Container zu fetchen

def manage_containers(target_number): # Die Manage Container Funktion bestimmt, wie Container an und ausgeschaltet werden
    attempts = 0
    
    while attempts < MAX_ATTEMPTS:
        containers = list_containers()
        current_number = len(containers)

        if containers is None or current_number == 0:
            print("Es wurden keine Container gefunden oder es ist ein Fehler beim Abrufen der Container aufgetreten.")
            break

        if current_number > target_number:
            stop_random_containers(current_number - target_number)
        elif current_number < target_number:
            start_stopped_containers(target_number - current_number)
        else:
            print("Die Anzahl der Container entspricht dem Ziel.")
            break

        attempts += 1
        time.sleep(1)

    if attempts >= MAX_ATTEMPTS:
        print(f"Es wurden nach {MAX_ATTEMPTS} Versuchen keine Container gefunden.")


while True:
    target_number = GetAnzahlDocker()
    manage_containers(target_number)  # Ermittle wie viele (und ob überhaupt) Container an/aus-geschaltet werden müssen
    time.sleep(300)



