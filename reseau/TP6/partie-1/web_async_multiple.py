import aiohttp
import asyncio
import os
import sys
import time

async def get_content(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Lève une exception en cas d'erreur HTTP
            return await response.text()
    except aiohttp.ClientError as e:
        print(f"Erreur lors de la récupération du contenu de {url} : {e}")
        return None

async def write_content(content, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Contenu écrit avec succès dans le fichier : {file_path}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du contenu dans le fichier : {e}")
        sys.exit(1)

async def process_url(session, url):
    content = await get_content(session, url)
    if content is not None:
        filename = '/tmp/web_' + url.replace("https://", "").replace("/", "_")
        await write_content(content, filename)

async def main():
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <fichier_urls>")
        sys.exit(1)

    start_time = time.time()

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            urls = file.read().splitlines()

        async with aiohttp.ClientSession() as session:
            # Utilisation de asyncio.gather pour exécuter les fonctions de manière concurrente
            tasks = [process_url(session, url) for url in urls]

            await asyncio.gather(*tasks)

    except IOError as e:
        print(f"Erreur lors de la lecture du fichier d'URL : {e}")
        sys.exit(1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Le programme a pris {elapsed_time:.2f} secondes pour s'exécuter.")

if __name__ == "__main__":
    asyncio.run(main())
