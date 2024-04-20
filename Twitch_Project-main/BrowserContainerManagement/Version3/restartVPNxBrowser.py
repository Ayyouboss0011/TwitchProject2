import subprocess
import time

# Liste der Containerpaare
container_pairs = [
    {"vpn": "vpn1", "browser": "b1"},
    {"vpn": "vpn2", "browser": "b2"},
    {"vpn": "vpn3", "browser": "b3"},
    {"vpn": "vpn4", "browser": "b4"},
    {"vpn": "vpn5", "browser": "b5"},
    {"vpn": "vpn6", "browser": "b6"},
    {"vpn": "vpn7", "browser": "b7"},
    {"vpn": "vpn8", "browser": "b8"},
    {"vpn": "vpn9", "browser": "b9"},
    {"vpn": "vpn10", "browser": "b10"},
    {"vpn": "vpn11", "browser": "b11"},
    {"vpn": "vpn12", "browser": "b12"},
    {"vpn": "vpn13", "browser": "b13"},
    {"vpn": "vpn14", "browser": "b14"},
    {"vpn": "vpn15", "browser": "b15"},
    {"vpn": "vpn16", "browser": "b16"},
    {"vpn": "vpn17", "browser": "b17"},
    {"vpn": "vpn18", "browser": "b18"},
    {"vpn": "vpn19", "browser": "b19"},
    {"vpn": "vpn20", "browser": "b20"},
    {"vpn": "vpn21", "browser": "b21"},
    {"vpn": "vpn22", "browser": "b22"},
    {"vpn": "vpn23", "browser": "b23"},
    {"vpn": "vpn24", "browser": "b24"},
    {"vpn": "vpn25", "browser": "b25"},
    {"vpn": "vpn26", "browser": "b26"},
    {"vpn": "vpn27", "browser": "b27"},
]

def restart_container(container_name):
    subprocess.run(["docker", "restart", container_name])

def restart_container_pair(vpn_container, browser_container):
    print(f"Restarting VPN container: {vpn_container}")
    restart_container(vpn_container)
    time.sleep(10)
    print(f"Restarting Browser container: {browser_container}")
    restart_container(browser_container)
    time.sleep(5)
    
# Iteriere über alle Containerpaare und starte sie neu
def restartVPNxBrowser():
    for pair in container_pairs:
        restart_container_pair(pair["vpn"], pair["browser"])
