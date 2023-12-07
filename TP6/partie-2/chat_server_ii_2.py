import asyncio

async def handle_client(reader, writer, clients):
    client_address = writer.get_extra_info('peername')
    print(f"Client connecté : {client_address}")
    clients.add(writer)

    welcome_message = f"Hello {client_address[0]}:{client_address[1]}\n"
    writer.write(welcome_message.encode())
    await writer.drain()

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break

            message = data.decode()
            print(f"Message du client {client_address}: {message}")

            # Envoyer une réponse (écho)
            writer.write(data)
            await writer.drain()

    except asyncio.CancelledError:
        pass
    finally:
        print(f"Client déconnecté : {client_address}")
        clients.remove(writer)
        writer.close()

async def send_message(clients, message):
    for client in clients:
        try:
            client.write(message.encode())
            await client.drain()
        except:
            pass

async def main():
    server = await asyncio.start_server(
        handle_client, '', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serveur en écoute sur {addr}')

    clients = set()

    try:
        while True:
            # Attendre un message du terminal (console)
            server_message = input("Saisissez un message pour les clients : ")

            # Envoyer le message à tous les clients
            await send_message(clients, server_message)

    except KeyboardInterrupt:
        pass
    finally:
        for client in clients:
            client.close()

if __name__ == "__main__":
    asyncio.run(main())

