import socket

def main():
    host = '10.0.3.17'  # L'adresse IP du serveur
    port = 8888         # Le port utilisé par le serveur

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # Envoyer "Hello" au serveur
        client_socket.sendall(b'Hello')

        # Attendre la réponse du serveur
        data = client_socket.recv(1024)

    print(f"Réponse du serveur : {data.decode()}")

if __name__ == "__main__":
    main()