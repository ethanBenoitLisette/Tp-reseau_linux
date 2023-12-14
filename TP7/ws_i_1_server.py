import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        
        while True:
            # Recevoir le message du client
            message = await websocket.recv()

            # Afficher le message côté serveur
            print(f"Serveur a reçu : {message}")

            # Répondre au client
            response = f"Hello client ! Received \"{message}\""
            await websocket.send(response)

    except websockets.exceptions.ConnectionClosedOK:
        print("Client déconnecté.")

if __name__ == "__main__":
    start_server = websockets.serve(handle_client, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
