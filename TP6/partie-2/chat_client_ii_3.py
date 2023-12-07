import asyncio
import aioconsole

async def user_input(writer):
    while True:
        user_message = await aioconsole.ainput("Saisissez un message (ou 'exit' pour quitter) : ")

        
        writer.write(user_message.encode())
        await writer.drain()

async def receive_messages(reader):
    while True:
        
        data = await reader.read(1024)
        if not data:
            break

    
        print(f"Message du serveur : {data.decode()}")

async def main():
    host = '10.0.3.17'  
    port = 8888         

    try:
        
        reader, writer = await asyncio.open_connection(host=host, port=port)

        
        await asyncio.gather(
            user_input(writer),
            receive_messages(reader)
        )

    except asyncio.CancelledError:
        pass
    finally:
        print("Client déconnecté.")
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
