import socket
import struct

def receive_message(sock):
    msg_len = struct.unpack('!I', sock.recv(4))[0]
    message = sock.recv(msg_len).decode()
    return message

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 9999))
server_socket.listen()

print("Le serveur écoute sur :9999")

try:
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")

    client_hello = receive_message(client_socket)
    client_socket.sendall("Hello from server".encode())

    expr = receive_message(client_socket)
    print(f"Expression reçue du client : {expr}")

    result = eval(expr)
    client_socket.sendall(str(result).encode())

finally:
    client_socket.close()
    server_socket.close()
