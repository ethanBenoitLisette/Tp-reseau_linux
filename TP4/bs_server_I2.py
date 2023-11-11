import socket
from sys import exit
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
conn, addr = s.accept()
# Dès que quelqu'un se connecte, on affiche un message qui contient son adresse

# Petite boucle infinie (bah oui c'est un serveur)
# A chaque itération la boucle reçoit des données et les traite
while True:

    try:
        # On reçoit 1024 bytes de données
        data = conn.recv(1024)

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

    except socket.error:
        print ("Error Occured.")
        break

# on précise pas quelle exception, ça catch tout
    print("Un client vient de se connecter et son IP est " + addr[0])



# On ferme proprement la connexion TCP
conn.close()
exit(0)