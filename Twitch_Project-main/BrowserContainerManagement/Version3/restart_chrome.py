import subprocess
import time

container_ids = subprocess.check_output(['docker', 'ps', '-q'], text=True).split()
command_to_execute = 'pkill -f chrome'

def restart_chrome_container(container_id, command):
    try:
        subprocess.run(['docker', 'exec', container_id, *command.split()], check=True)
        print(f"Command executed successfully in container {container_id}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error executing command in container {container_id}: {e}")

def restart_chrome():
    for container_id in container_ids:
        restart_chrome_container(container_id, command_to_execute)
        time.sleep(15)