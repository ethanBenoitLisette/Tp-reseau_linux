import asyncio
import websockets

async def user_interaction():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        try:
            while True:
                # Saisie utilisateur
                user_input = input("Saisissez une chaîne à envoyer au serveur (ou 'exit' pour quitter) : ")

                if user_input.lower() == 'exit':
                    break

                # Envoyer le message au serveur
                await websocket.send(user_input)

                # Recevoir la réponse du serveur
                response = await websocket.recv()
                print(f"Client a reçu : {response}")

        except websockets.exceptions.ConnectionClosedOK:
            print("Connexion fermée par le serveur.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(user_interaction())

