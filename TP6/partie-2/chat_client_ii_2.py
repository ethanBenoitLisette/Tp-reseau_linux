import socket
import asyncio

async def receive_messages(client_socket):
    try:
        while True:
            # Attendre la réception d'un message du serveur
            data = client_socket.recv(1024)
            print(f"Message du serveur : {data.decode()}")
    except (socket.error, KeyboardInterrupt):
        pass

def main():
    host = '10.0.3.17'
    port = 8888

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # Lancer une tâche asynchrone pour recevoir des messages du serveur
        asyncio.create_task(receive_messages(client_socket))

        try:
            while True:
                # Envoyer un message au serveur
                message = input("Saisissez un message (ou 'exit' pour quitter) : ")
                if message.lower() == 'exit':
                    break
                client_socket.sendall(message.encode())
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
