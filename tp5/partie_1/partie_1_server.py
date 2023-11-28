import socket
import struct

host = ''
port = 13337

# Création de l'objet socket de type TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket au serveur et au port
server_socket.bind((host, port))

# Écoute du socket
server_socket.listen()

print(f"Le serveur écoute sur {host}:{port}")

# Attente de la connexion d'un client
client_socket, client_address = server_socket.accept()
print(f"Connexion établie avec {client_address}")

# Réception des données empaquetées
packed_data = client_socket.recv(8)

# Déballer l'entier
number_received = struct.unpack('!Q', packed_data)[0]

print(f"Nombre reçu du client : {number_received}")

# Fermer la connexion avec le client
client_socket.close()

# Fermer le socket du serveur
server_socket.close()
