import socket
from sys import exit
import re

# On définit la destination de la connexion
host = '10.0.3.17'  # IP du serveur
port = 13337               # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
# Connexion au serveur
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    
except :
    print("ça marche pos")

# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)

print(f"{data.decode()}")

print("Que veux-tu envoyer au serveur : ")

message = input()

if type(message) is not str:
    raise TypeError("Ici on veut que des strings !")
    
is_meo_or_waf_pattern = re.compile('.*?((meo)|(waf))')

if not is_meo_or_waf_pattern.match(message):
    raise TypeError("L'entrée doit contenir soit 'meo' soit 'waf'")

s.sendall(bytes(message, 'utf-8'))

server_response = s.recv(1024)

print(f"{server_response.decode()}")

# On libère le socket TCP
s.close()

exit(0)

