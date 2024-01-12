import psutil
import socket
import os
import json
from datetime import datetime

LOG_FILE = "monit_logs.json"

def init_log_file():
    with open(LOG_FILE, "a") as log_file:
        log_file.write("[]\n")  # Crée un tableau JSON vide

def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {"timestamp": timestamp, "action": action}
    print(log_entry)


    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as log_file:
            logs = json.load(log_file)
    else:
        logs = []
    print(logs)
    logs.append(log_entry)

    with open(LOG_FILE, "w") as log_file:
        json.dump(logs, log_file, indent=2)

def monitor_system():

    log_action("Check")

def list_reports():
    try:
        with open(LOG_FILE, "r") as log_file:
            logs = json.load(log_file)
            for log_entry in logs:
                if log_entry["action"] == "Check":
                    print(f"Timestamp: {log_entry['timestamp']}")
    except FileNotFoundError:
        print("Aucun fichier de log trouvé.")

def get_last_report():
    try:
        with open(LOG_FILE, "r") as log_file:
            logs = json.load(log_file)
            for log_entry in reversed(logs):
                if log_entry["action"] == "Check":
                    print(f"Dernier rapport: {log_entry['timestamp']}")
                    break
    except FileNotFoundError:
        print("Aucun fichier de log trouvé.")

def get_avg_report(last_x_hours):
    try:
        with open(LOG_FILE, "r") as log_file:
            logs = json.load(log_file)
        
        timestamps = [log_entry['timestamp'] for log_entry in logs if log_entry["action"] == "Check"]
        
        if len(timestamps) < last_x_hours:
            print(f"Nombre insuffisant de rapports pour calculer la moyenne sur {last_x_hours} heures.")
            return
        
        avg_timestamps = timestamps[:last_x_hours]
        print(f"Valeurs moyennes des {last_x_hours} dernières heures: {avg_timestamps}")
    except FileNotFoundError:
        print("Aucun fichier de log trouvé.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: monit.py <command>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "check":
        monitor_system()
    elif command == "list":
        list_reports()
    elif command == "get" and len(sys.argv) == 3:
        sub_command = sys.argv[2]

        if sub_command == "last":
            get_last_report()
        elif sub_command == "avg" and len(sys.argv) == 4:
            last_x_hours = int(sys.argv[3])
            get_avg_report(last_x_hours)
        else:
            print("Commande invalide.")
            sys.exit(1)
    else:
        print("Commande invalide.")
        sys.exit(1)
