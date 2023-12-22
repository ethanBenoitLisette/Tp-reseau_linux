import asyncio
import aioconsole

async def send_pseudo(writer):
    # Saisir le pseudo de l'utilisateur
    pseudo = input("Veuillez saisir votre pseudo : ")

    # Envoyer le message contenant le pseudo au serveur
    writer.write(f"Hello|{pseudo}".encode())
    await writer.drain()

async def user_input(writer):
    try:
        while True:
            user_message = await aioconsole.ainput("Saisissez un message (ou 'exit' pour quitter) : ")
            if user_message.lower() == 'exit':
                break

            # Envoyer le message au serveur
            writer.write(user_message.encode())
            await writer.drain()
    except asyncio.CancelledError:
        pass

async def receive_messages(reader):
    try:
        while True:
            # Attendre les messages du serveur
            data = await reader.read(1024)
            if not data:
                break

            # Afficher le message du serveur
            message = data.decode()
            if message.strip() == "":
                print("Déconnecté du serveur. Quittez l'application.")
                break

            print(f"Message du serveur : {message}")
    except asyncio.CancelledError:
        pass

async def main():
    host = '10.0.3.17'  # L'adresse IP du serveur
    port = 8888         # Le port utilisé par le serveur

    try:
        # Ouvrir une connexion vers le serveur
        reader, writer = await asyncio.open_connection(host=host, port=port)

        # Envoyer le pseudo au serveur
        await send_pseudo(writer)

        # Lancer les deux coroutines en parallèle
        await asyncio.gather(
            user_input(writer),
            receive_messages(reader)
        )

    except KeyboardInterrupt:
        pass
    finally:
        print("Client déconnecté.")
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
