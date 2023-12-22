import asyncio

USER_ID_COUNTER = 1
CLIENTS = {}

async def handle_client(reader, writer):
    global USER_ID_COUNTER

    client_address = writer.get_extra_info('peername')

    if client_address in CLIENTS:
        print(f"Client déjà connecté : {client_address}")
        user_id = CLIENTS[client_address]["id"]
        CLIENTS[client_address]["connected"] = True
    else:
        user_id = USER_ID_COUNTER
        USER_ID_COUNTER += 1

        CLIENTS[client_address] = {"id": user_id, "r": reader, "w": writer, "connected": True}
        print(f"Client connecté : {client_address}, ID : {user_id}")

        writer.write(f"Welcome back, User {user_id}!\n".encode())
        await writer.drain()

        announcement = f"Annonce : User {user_id} est de retour !\n"
        for addr, client in CLIENTS.items():
            if addr != client_address and client["connected"]:
                client["w"].write(announcement.encode())
                await client["w"].drain()

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break

            message = data.decode()
            print(f"User {user_id} a dit : {message}")

            for addr, client in CLIENTS.items():
                if addr != client_address and client["connected"]:
                    client["w"].write(f"User {user_id} a dit : {message}".encode())
                    await client["w"].drain()

    except asyncio.CancelledError:
        pass
    finally:
        print(f"Client déconnecté : {client_address}, ID : {user_id}")
        CLIENTS[client_address]["connected"] = False
        writer.close()
        await writer.wait_closed()

async def main():
    host = ''
    port = 8888

    try:
        server = await asyncio.start_server(
            handle_client, host, port)

        addr = server.sockets[0].getsockname()
        print(f'Serveur en écoute sur {addr}')

        async with server:
            await server.serve_forever()

    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    asyncio.run(main())
