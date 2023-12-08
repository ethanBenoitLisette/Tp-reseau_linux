import asyncio
import aioconsole

async def send_pseudo(writer):
    
    pseudo = input("Veuillez saisir votre pseudo : ")

    writer.write(f"Hello|{pseudo}".encode())
    await writer.drain()

async def user_input(writer):
    try:
        while True:
            user_message = await aioconsole.ainput("Saisissez un message (ou 'exit' pour quitter) : ")
            if user_message.lower() == 'exit':
                break

            writer.write(user_message.encode())
            await writer.drain()
    except asyncio.CancelledError:
        pass

async def receive_messages(reader):
    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break

            print(f"Message du serveur : {data.decode()}")
    except asyncio.CancelledError:
        pass

async def main():
    host = '10.0.3.17' 
    port = 8888         

    try:
        reader, writer = await asyncio.open_connection(host=host, port=port)

        await send_pseudo(writer)

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
