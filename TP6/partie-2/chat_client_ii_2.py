import socket

def main():
    host = '10.0.3.17'
    port = 8888

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        while True:
            # Envoyer un message au serveur
            message = input("Saisissez un message (ou 'exit' pour quitter) : ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())

            # Attendre la réponse du serveur
            data = client_socket.recv(1024)
            print(f"Réponse du serveur : {data.decode()}")

if __name__ == "__main__":
    main()