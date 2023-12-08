import asyncio


CLIENTS = {}

async def handle_client(reader, writer):
    
    client_address = writer.get_extra_info('peername')

    if client_address in CLIENTS:
        print(f"Client déjà connecté : {client_address}")
        writer.close()
        await writer.wait_closed()
        return

    CLIENTS[client_address] = {"r": reader, "w": writer}
    print(f"Client connecté : {client_address}")

    welcome_message = f"Hello {client_address[0]}:{client_address[1]}\n"
    writer.write(welcome_message.encode())
    await writer.drain()

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break

            message = data.decode()
            print(f"Message reçu de {client_address[0]}:{client_address[1]} : {message}")

            for addr, client in CLIENTS.items():
                if addr != client_address:
                    client["w"].write(data)
                    await client["w"].drain()

    except asyncio.CancelledError:
        pass
    finally:

        print(f"Client déconnecté : {client_address}")
        del CLIENTS[client_address]
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
