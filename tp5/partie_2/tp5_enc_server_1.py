import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9999))
sock.listen()
client, client_addr = sock.accept()

while True:
    header = client.recv(4)
    if not header:
        break

    msg_len = int.from_bytes(header, byteorder='big')

    chunks = []
    bytes_received = 0

    while bytes_received < msg_len:
        chunk = client.recv(min(msg_len - bytes_received, 1024))
        if not chunk:
            raise RuntimeError('Invalid chunk received bro')

        chunks.append(chunk)
        bytes_received += len(chunk)

    message_received = b"".join(chunks).decode('utf-8')
    print(f"Received from client {message_received}")

client.close()
sock.close()
