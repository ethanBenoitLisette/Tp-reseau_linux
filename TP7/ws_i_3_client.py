import asyncio
import websockets

async def user_interaction():
    uri = "ws://10.0.3.17:8888"
    async with websockets.connect(uri) as websocket:
        pseudo = input("Choisissez un pseudo : ")
        await websocket.send(pseudo)

        try:
            while True:
                user_input = input("Saisissez un message (ou 'exit' pour quitter) : ")

                if user_input.lower() == 'exit':
                    break

                await websocket.send(user_input)

        except websockets.exceptions.ConnectionClosedOK:
            print("Connexion fermée par le serveur.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(user_interaction())
