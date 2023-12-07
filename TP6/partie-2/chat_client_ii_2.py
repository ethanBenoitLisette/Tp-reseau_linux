import socket

def main():
    host = '127.0.0.1'
    port = 8888

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        client_socket.sendall(b'Hello')

        data = client_socket.recv(1024)

    print(f"Réponse du serveur : {data.decode()}")

if __name__ == "__main__":
    main()
