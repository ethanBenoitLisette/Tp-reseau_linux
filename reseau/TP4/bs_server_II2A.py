import socket
from sys import exit
import argparse
import logging
import os
from logging.handlers import TimedRotatingFileHandler

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port", action="store", type=int, default=13337, help='precise a port to bind the program, default is 13337')

args = parser.parse_args()

if args.port < 0 or args.port > 65535:
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    exit(1)
elif args.port >= 0 and args.port <= 1024:
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    exit(2)

# On choisit une IP et un port où on va écouter
host = '' # string vide signifie, dans ce conetxte, toutes les IPs de la machine
port = 13337

# SOCK_STREAM c'est pour créer un socket TCP (pas UDP donc)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# On demande à notre programme de se bind sur notre port
s.bind((host, port))

# Place le programme en mode écoute derrière le port auquel il s'est bind
s.listen(1)
# On définit l'action à faire quand quelqu'un se connecte : on accepte

# Dès que quelqu'un se connecte, on affiche un message qui contient son adresse

# Petite boucle infinie (bah oui c'est un serveur)
# A chaque itération la boucle reçoit des données et les traite
while True:
    
    conn, addr = s.accept()
    
    print("Un client vient de se connecter et son IP est " + addr[0])
    
    conn.sendall(b'Hi mate!')

    try:
        # On reçoit 1024 bytes de données
        data = conn.recv(1024).decode()

        # Si on a rien reçu, on continue
        if not data: continue

        # On affiche dans le terminal les données reçues du client
        print(f"{data}")

        # On répond au client un truc
        if "meo" in data:
            conn.sendall(bytes('Meo à toi confrère.', 'utf-8'))
        elif "waf" in data:
            conn.sendall(b'ptdr t ki')
        else:
            conn.sendall(b'Mes respects humble humain.')
            
        conn.close()

    except socket.error:
        print ("Error Occured.")
        conn.close()
        break

# on précise pas quelle exception, ça catch tout


# Créer le dossier des logs s'il n'existe pas
log_directory = '/var/log/bs_server/'
os.makedirs(log_directory, exist_ok=True)

# Configurer le logger
logger = logging.getLogger('bs_server')
logger.setLevel(logging.DEBUG)

# Créer un formateur pour les messages de log
formatter = logging.Formatter('%(levelname)s %(message)s')

# Configurer la sortie console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Configurer la sortie vers le fichier
log_file_path = os.path.join(log_directory, 'bs_server.log')
file_handler = TimedRotatingFileHandler(log_file_path, when='midnight', backupCount=7)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Fonction pour loguer les événements
def log_event(level, message, ip=None, client_message=None):
    if ip:
        message = message.replace('<IP_CLIENT>', ip)
    if client_message:
        message = message.replace('<MESSAGE>', client_message)

    logger.log(level, message)




# On ferme proprement la connexion TCP
conn.close()
exit(0)
