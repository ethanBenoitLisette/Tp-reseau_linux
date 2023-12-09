import asyncio

# Dictionnaire global pour stocker les informations des clients
CLIENTS = {}

async def handle_client(reader, writer):
    # Récupérer les informations sur le client
    client_address = writer.get_extra_info('peername')

    # Vérifier si le client est déjà connecté
    if client_address in CLIENTS:
        print(f"Client déjà connecté : {client_address}")
        writer.close()
        await writer.wait_closed()
        return

    try:
        # Lire le pseudo du message "Hello|<PSEUDO>"
        data = await reader.read(100)
        if not data.startswith(b"Hello|"):
            print(f"Message invalide du client {client_address}")
            return

        pseudo = data.decode().split("|")[1]

        # Ajouter les informations du client au dictionnaire
        CLIENTS[client_address] = {"r": reader, "w": writer, "pseudo": pseudo}
        print(f"Client connecté : {client_address}, Pseudo : {pseudo}")

        # Envoyer une annonce à tous les clients
        announcement = f"Annonce : {pseudo} a rejoint la chatroom\n"
        for addr, client in CLIENTS.items():
            if addr != client_address:
                client["w"].write(announcement.encode())
                await client["w"].drain()

        while True:
            # Lire le message du client
            data = await reader.read(100)
            if not data:
                break

            # Afficher le message du client avec les informations de l'expéditeur
            message = data.decode()
            if message.strip() == "":
                print(f"Client déconnecté : {client_address}, Pseudo : {pseudo}")
                break

            print(f"{pseudo} a dit : {message}")

            # Envoyer le message à tous les autres clients
            for addr, client in CLIENTS.items():
                if addr != client_address:
                    client["w"].write(f"{pseudo} a dit : {message}".encode())
                    await client["w"].drain()

    except asyncio.CancelledError:
        pass
    finally:
        # Supprimer les informations du client lorsqu'il se déconnecte
        print(f"Client déconnecté : {client_address}, Pseudo : {pseudo}")
        del CLIENTS[client_address]
        # Envoyer une annonce à tous les clients
        announcement = f"Annonce : {pseudo} a quitté la chatroom\n"
        for client in CLIENTS.values():
            client["w"].write(announcement.encode())
            await client["w"].drain()
        writer.close()
        await writer.wait_closed()

async def main():
    host = '127.0.0.1'  # L'adresse IP du serveur
    port = 8888         # Le port utilisé par le serveur

    try:
        # Ouvrir une connexion vers le serveur
        server = await asyncio.start_server(
            handle_client, host, port)

        # Afficher l'adresse du serveur
        addr = server.sockets[0].getsockname()
        print(f'Serveur en écoute sur {addr}')

        async with server:
            await server.serve_forever()

    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    asyncio.run(main())
