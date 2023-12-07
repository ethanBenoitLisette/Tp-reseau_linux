import socket

def handle_client(client_socket):
    client_address = client_socket.getpeername()
    print(f"Client connecté : {client_address}")

    # Envoyer un message de bienvenue
    welcome_message = f"Hello {client_address[0]}:{client_address[1]}\n"
    client_socket.sendall(welcome_message.encode())

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            message = data.decode()
            print(f"Message du client {client_address}: {message}")

            # Envoyer une réponse (écho)
            client_socket.sendall(data)

    finally:
        print(f"Client déconnecté : {client_address}")
        client_socket.close()

def main():
    host = ''
    port = 8888

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f'Serveur en écoute sur {host}:{port}')

        while True:
            client_socket, addr = server_socket.accept()
            handle_client(client_socket)

if __name__ == "__main__":
    main()
