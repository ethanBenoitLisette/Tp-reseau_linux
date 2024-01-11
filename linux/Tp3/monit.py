import psutil
import socket
import os

def monitor_system():
    # Informations sur la mémoire RAM
    memory_info = psutil.virtual_memory()
    print(f"RAM Usage: {memory_info.percent}%")

    # Informations sur l'utilisation du disque
    disk_info = psutil.disk_usage("/")
    print(f"Disk Usage: {disk_info.percent}%")

    # Informations sur l'activité du CPU
    cpu_info = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_info}%")

    # Vérification des ports TCP ouverts
    open_ports = get_open_ports()
    print(f"Open TCP Ports: {open_ports}")

def get_open_ports():
    open_ports = []
    for port in range(1, 1025):  # Vérifiez les ports de 1 à 1024
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(("localhost", port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    monitor_system()
