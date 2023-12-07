import asyncio

async def handle_client(reader, writer):
    # Récupérer les informations sur le client
    client_address = writer.get_extra_info('peername')
    print(f"Client connecté : {client_address}")

    # Envoyer un message de bienvenue
    welcome_message = f"Hello {client_address[0]}:{client_address[1]}\n"
    writer.write(welcome_message.encode())
    await writer.drain()

    try:
        while True:
            # Lire le message du client
            data = await reader.read(100)
            if not data:
                break

            # Afficher le message du client
            message = data.decode()
            print(f"Message du client {client_address}: {message}")

            # Envoyer une réponse (écho)
            writer.write(data)
            await writer.drain()

    except asyncio.CancelledError:
        pass
    finally:
        # Fermer la connexion avec le client
        print(f"Client déconnecté : {client_address}")
        writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '', 8888)

    # Afficher l'adresse du serveur
    addr = server.sockets[0].getsockname()
    print(f'Serveur en écoute sur {addr}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())