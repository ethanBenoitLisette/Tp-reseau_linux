import asyncio
import json
from datetime import datetime

CLIENTS = {}

async def load_history():
    try:
        with open('chat_history.json', 'r') as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []
    return history

async def save_history(history):
    with open('chat_history.json', 'w') as file:
        json.dump(history, file)

async def send_history(writer):
    history = await load_history()
    history_message = json.dumps({"type": "history", "content": history})
    writer.write(history_message.encode())
    await writer.drain()

async def handle_client(reader, writer):
    client_address = writer.get_extra_info('peername')
    if client_address in CLIENTS:
        writer.close()
        await writer.wait_closed()
        return

    try:
        await send_history(writer)
        data = await reader.read(100)
        if not data.startswith(b"Hello|"):
            return

        pseudo = data.decode().split("|")[1]
        CLIENTS[client_address] = {"r": reader, "w": writer, "pseudo": pseudo}

        announcement = f"Annonce : {pseudo} a rejoint la chatroom\n"
        for addr, client in CLIENTS.items():
            if addr != client_address:
                client["w"].write(announcement.encode())
                await client["w"].drain()

        while True:
            data = await reader.read(100)
            if not data:
                break

            message = {"timestamp": datetime.now().isoformat(), "pseudo": pseudo, "content": data.decode()}
            print(f"{pseudo} a dit : {message['content']}")

            history = await load_history()
            history.append(message)
            await save_history(history)

            for addr, client in CLIENTS.items():
                if addr != client_address:
                    client["w"].write(f"{pseudo} a dit : {message['content']}".encode())
                    await client["w"].drain()

    except asyncio.CancelledError:
        pass
    finally:
        print(f"Client déconnecté : {client_address}, Pseudo : {pseudo}")
        del CLIENTS[client_address]

        announcement = f"Annonce : {pseudo} a quitté la chatroom\n"
        for client in CLIENTS.values():
            client["w"].write(announcement.encode())
            await client["w"].drain()
        writer.close()
        await writer.wait_closed()

async def main():
    host = ''
    port = 8888

    try:
        server = await asyncio.start_server(handle_client, host, port)
        addr = server.sockets[0].getsockname()
        print(f'Serveur en écoute sur {addr}')

        async with server:
            await server.serve_forever()

    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    asyncio.run(main())
