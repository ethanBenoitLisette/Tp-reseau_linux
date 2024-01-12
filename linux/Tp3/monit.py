import psutil
import socket
import os
import json
from datetime import datetime

LOG_FILE = "monit_logs.json"

def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {"timestamp": timestamp, "action": action}
    
    with open(LOG_FILE, "a") as log_file:
        json.dump(log_entry, log_file)
        log_file.write("\n")

def monitor_system():
    log_action("Check")

def list_reports():
    try:
        with open(LOG_FILE, "r") as log_file:
            for line in log_file:
                log_entry = json.loads(line)
                if log_entry["action"] == "Check":
                    print(f"Timestamp: {log_entry['timestamp']}")
    except FileNotFoundError:
        print("Aucun fichier de log trouvé.")

def get_last_report():
    try:
        with open(LOG_FILE, "r") as log_file:
            for line in reversed(list(log_file)):
                log_entry = json.loads(line)
                if log_entry["action"] == "Check":
                    print(f"Dernier rapport: {log_entry['timestamp']}")
                    break
    except FileNotFoundError:
        print("Aucun fichier de log trouvé.")

def get_avg_report(last_x_hours):
    try:
        avg_timestamps = []

        with open(LOG_FILE, "r") as log_file:
            for line in reversed(list(log_file)):
                log_entry = json.loads(line)

                if log_entry["action"] == "Check":
                    timestamp = datetime.strptime(log_entry['timestamp'], "%Y-%m-%d %H:%M:%S")
                    now = datetime.now()

                    # Calcul de la différence en heures
                    hours_difference = (now - timestamp).total_seconds() / 3600

                    # Ajout du timestamp si dans la plage spécifiée
                    if 0 <= hours_difference < last_x_hours:
                        avg_timestamps.append(log_entry['timestamp'])
                    elif hours_difference >= last_x_hours:
                        break  # Sortir du parcours si les données sont trop anciennes

        if len(avg_timestamps) == 0:
            print(f"Aucun rapport trouvé pour les {last_x_hours} dernières heures.")
        else:
            print(f"Valeurs moyennes des {last_x_hours} dernières heures: {avg_timestamps}")
    except FileNotFoundError:
        print("Aucun fichier de log trouvé.")

if __name__ == "__main__":
    get_avg_report(24)
