II. Opti calculatrice
Dans cette partie on va commencer par gérer correctement l'envoi/réception comme un flux de données plutôt qu'un appel à recv(1024) random (pourquoi 1024 ?).

On reste sur le thème nul de la calculatrice réseau pour le moment.



II. Opti calculatrice

0. Setup
1. Strings sur mesure
2. Code Encode Decode




0. Setup
Réutilisez votre code du TP5, la calculatrice, ou partez avec cette version minimale et simplifiée :

Pas besoin de logs ni rien là, on se concentre sur le sujet : l'encodage.

➜ Client

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

# Récupération d'une string utilisateur
msg = input("Calcul à envoyer: ")

# On envoie
s.send(msg.encode())

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()


➜ Serveur

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 9999))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        # On reçoit la string Hello du client
        data = conn.recv(1024)
        if not data: break
        print(f"Données reçues du client : {data}")

        conn.send("Hello".encode())

        # On reçoit le calcul du client
        data = conn.recv(1024)

        # Evaluation et envoi du résultat
        res  = eval(data.decode())
        conn.send(str(res).encode())
         
    except socket.error:
        print("Error Occured.")
        break

conn.close()



1. Strings sur mesure
   
On gère toujours que des strings pour le moment, on reste sur de simples encode() et decode() pour le transit sur le réseau.

🌞 tp5_enc_client_1.py

[tp5_enc_client_1.py](tp5_enc_client_1.py)

il réceptionne un message utilisateur
calcule sa taille 
créer un header
envoie le tout sur le réseau

🌞 tp5_enc_server_1.py

attend la réception des messages d'un client
à la réception d'un message

lit l'en-tête pour déterminer combien il doit lire ensuite
lit les x octets suivants
reconstitue le message
vérifie que le message se terminent bien par la séquence de fin
[bs_server_I1.py](bs_server_I1.py)



➜ Bout de code serveur pour vous aider

fonctionnel avec le client juste avant
il lit le header et lit dynamiquement la taille du message qui suit


Hé on s'approche de plus en plus de problèmes réels là, tu le sens ou pas meow. 🐈‍



1. Code Encode Decode
🌞 tp5_enc_client_2.py et tp5_enc_server_2.py

maintenant vous traitez les entiers comme des entiers et plus comme des strings