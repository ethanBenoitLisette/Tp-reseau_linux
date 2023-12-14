import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            print(f"Serveur a reçu : {message}")
            response = f"Hello client ! Received \"{message}\""
            await websocket.send(response)

    except websockets.exceptions.ConnectionClosedOK:
        print("Client déconnecté.")

if __name__ == "__main__":
    start_server = websockets.serve(handle_client, "10.0.3.17", 8888)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
