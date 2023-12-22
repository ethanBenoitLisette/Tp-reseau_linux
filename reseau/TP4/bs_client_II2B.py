import socket
import re
import logging
from sys import exit

# Configuration du logger
logger = logging.getLogger('bs_client')
logger.setLevel(logging.DEBUG)

# Création d'un formateur pour les messages de log
formatter = logging.Formatter('%(levelname)s %(message)s')

# Configuration de la sortie console en rouge pour les erreurs
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Configuration de la sortie vers le fichier de log
log_directory = '/var/log/'
log_file_path = f'{log_directory}/bs_client.log'
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# On définit la destination de la connexion
host = '10.0.3.17'  # IP du serveur
port = 13337  # Port choisi par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connexion au serveur
    s.connect((host, port))
    logger.info(f"Connexion réussie à {host}:{port}")

except Exception as e:
    logger.error(f"Impossible de se connecter au serveur {host} sur le port {port}. Erreur : {e}")
    exit(1)

# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)
logger.info(f"Réponse reçue du serveur {host}:{port} : {data.decode()}")

print("Que veux-tu envoyer au serveur : ")

message = input()

if not isinstance(message, str):
    raise TypeError("Ici on veut que des strings !")

is_meo_or_waf_pattern = re.compile('.*?((meo)|(waf))')

if not is_meo_or_waf_pattern.match(message):
    raise TypeError("L'entrée doit contenir soit 'meo' soit 'waf'")

s.sendall(bytes(message, 'utf-8'))

server_response = s.recv(1024)
logger.info(f"Réponse reçue du serveur {host}:{port} : {server_response.decode()}")

# On libère le socket TCP
s.close()
exit(0)
