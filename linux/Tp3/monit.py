import psutil
import socket
import os
import json
from datetime import datetime

LOG_FILE = "monit_logs.json"

def init_log_file():
    # Correction : Utilisation de `w` au lieu de `a` pour écrire un tableau JSON vide
    with open(LOG_FILE, "w") as log_file:
        json.dump([], log_file)

def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Correction : Utilisation de `r+` pour ouvrir le fichier en mode lecture/écriture
        with open(LOG_FILE, "r+") as log_file:
            logs = json.load(log_file)
            logs.append({"timestamp": timestamp, "action": action})
            # Correction : Retour au début du fichier pour éviter d'ajouter des espaces inutiles
            log_file.seek(0)
            json.dump(logs, log_file, indent=2)
            # Correction : Tronquer le fichier après l'écriture pour éviter des données en double
            log_file.truncate()
    except FileNotFoundError:
        print("Aucun fichier de log trouvé.")

def monitor_system():
    # ... (comme dans le premier exemple)

    # Log de l'action de vérification
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
        now = datetime.now()
        avg_timestamps = []

        with open(LOG_FILE, "r") as log_file:
            for line in reversed(list(log_file)):
                log_entry = json.loads(line)
                temp_entry = log_entry.get("action")

                if temp_entry is not None and temp_entry == "Check" \
                        and 0 <= (now - datetime.strptime(log_entry['timestamp'], "%Y-%m-%d %H:%M:%S")).total_seconds() / 3600 < last_x_hours:
                    avg_timestamps.append(log_entry['timestamp'])

        if avg_timestamps:
            print(f"Valeurs moyennes des {last_x_hours} dernières heures: {avg_timestamps}")
        else:
            print(f"Aucun rapport trouvé pour les {last_x_hours} dernières heures.")
    except FileNotFoundError:
        print("Aucun fichier de log trouvé.")

if __name__ == "__main__":
    init_log_file()
    get_avg_report(24)

