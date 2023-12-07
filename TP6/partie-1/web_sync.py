import os
import requests
import sys
import time

def get_content(url):
    try:
        start_time = time.time()

        response = requests.get(url)
        response.raise_for_status()  # Lève une exception en cas d'erreur HTTP

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"La requête a pris {elapsed_time:.2f} secondes.")

        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération du contenu : {e}")
        sys.exit(1)

def write_content(content, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Contenu écrit avec succès dans le fichier : {file_path}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du contenu dans le fichier : {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    content = get_content(url)
    file_path = '/tmp/web_page'

    write_content(content, file_path)

if __name__ == "__main__":
    main()
