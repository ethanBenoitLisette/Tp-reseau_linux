import aiohttp
import asyncio
import os
import sys

async def get_content(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Lève une exception en cas d'erreur HTTP
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"Erreur lors de la récupération du contenu : {e}")
        sys.exit(1)

async def write_content(content, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Contenu écrit avec succès dans le fichier : {file_path}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du contenu dans le fichier : {e}")
        sys.exit(1)

async def main():
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    content = await get_content(url)
    file_path = '/tmp/web_page'

    await write_content(content, file_path)

if __name__ == "__main__":
    asyncio.run(main())
