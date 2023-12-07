import os
import requests
import sys
import time

def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lève une exception en cas d'erreur HTTP
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération du contenu de {url} : {e}")
        return None

def write_content(content, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Contenu écrit avec succès dans le fichier : {file_path}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du contenu dans le fichier : {e}")
        sys.exit(1)

def process_url(url):
    content = get_content(url)
    if content is not None:
        filename = '/tmp/web_' + url.replace("https://", "").replace("/", "_")
        write_content(content, filename)

def main():
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <fichier_urls>")
        sys.exit(1)

    start_time = time.time()

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            urls = file.read().splitlines()

        for url in urls:
            process_url(url)

    except IOError as e:
        print(f"Erreur lors de la lecture du fichier d'URL : {e}")
        sys.exit(1)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Le programme a pris {elapsed_time:.2f} secondes pour s'exécuter.")

if __name__ == "__main__":
    main()
