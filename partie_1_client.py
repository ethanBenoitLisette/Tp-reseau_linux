import socket
import struct

host = 'localhost'
port = 13337

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connexion au serveur
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")

    # Nombre à envoyer
    number_to_send = 100000

    # Empaqueter l'entier en format binaire
    packed_data = struct.pack('!Q', number_to_send)

    # Envoyer les données empaquetées
    s.sendall(packed_data)
    print(f"Nombre envoyé au serveur : {number_to_send}")

except Exception as e:
    print(f"Impossible de se connecter au serveur {host} sur le port {port}. Erreur : {e}")

finally:
    # Fermer la connexion
    s.close()
