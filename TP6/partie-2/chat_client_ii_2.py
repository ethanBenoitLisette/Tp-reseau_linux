import socket
import asyncio

async def receive_messages(client_socket):
    try:
        while True:
            # Attendre la réception d'un message du serveur
            data = await loop.sock_recv(client_socket, 1024)
            print(f"Message du serveur : {data.decode()}")
    except (socket.error, KeyboardInterrupt):
        pass

async def send_message(clients, message):
    for client in clients:
        try:
            client.write(message.encode())
            await client.drain()
        except:
            pass

async def main():
    host = '10.0.3.17'
    port = 8888

    loop = asyncio.get_event_loop()  # Initialiser la boucle d'événements ici

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # Lancer une tâche asynchrone pour recevoir des messages du serveur
        await receive_messages(client_socket)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
