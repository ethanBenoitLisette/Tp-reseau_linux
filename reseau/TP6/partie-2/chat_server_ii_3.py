import asyncio

async def handle_client(reader, writer):

    client_address = writer.get_extra_info('peername')


    welcome_message = f"Hello {client_address[0]}:{client_address[1]}\n"
    writer.write(welcome_message.encode())
    await writer.drain()

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break

            message = data.decode()
            print(f"Message du client {client_address}: {message}")

            
            writer.write(data)
            await writer.drain()

    except asyncio.CancelledError:
        pass
    finally:
        print(f"Client déconnecté : {client_address}")
        writer.close()

async def main():
    server = await asyncio.start_server(
        handle_client, '', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serveur en écoute sur {addr}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
