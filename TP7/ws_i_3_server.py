import asyncio
import websockets

CLIENTS = {}

async def handle_client(websocket, path):
    try:
        pseudo = await websocket.recv()
        addr = websocket.remote_address

        CLIENTS[addr] = {"w": websocket, "pseudo": pseudo}
        print(f"{pseudo} a rejoint la chatroom.")

        announcement = f"Annonce : {pseudo} a rejoint la chatroom."
        await broadcast(announcement, addr)

        while True:
            message = await websocket.recv()
            announcement = f"{pseudo} a dit : {message}"
            await broadcast(announcement, addr)

    except websockets.exceptions.ConnectionClosedOK:
        addr = websocket.remote_address
        if addr in CLIENTS:
            del CLIENTS[addr]
            pseudo = CLIENTS[addr]["pseudo"]
            print(f"{pseudo} a quitté la chatroom.")
            
            announcement = f"Annonce : {pseudo} a quitté la chatroom."
            await broadcast(announcement, addr)

async def broadcast(message, exclude_addr):
    for addr, client in CLIENTS.items():
        if addr != exclude_addr:
            await client["w"].send(message)

if __name__ == "__main__":
    start_server = websockets.serve(handle_client, '', 8888)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
