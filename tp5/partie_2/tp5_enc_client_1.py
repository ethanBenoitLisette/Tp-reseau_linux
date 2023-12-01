import socket
import struct

def send_message(sock, message):
    msg_len = len(message)

    sock.sendall(struct.pack('!I', msg_len))

    sock.sendall(message.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.3.17', 9999))

try:
    send_message(s, 'Hello')

    data = s.recv(1024)
    print(data.decode())

    expr = input("Expression arithmétique (format: x op y): ")

    numbers = [int(n) for n in expr.split() if n.isdigit()]
    if any(num > 4294967295 for num in numbers):
        raise ValueError("Les nombres dans l'expression ne doivent pas dépasser 4294967295")

    allowed_operations = set(['+', '-', '*'])
    operations = [op for op in expr.split() if op in allowed_operations]
    if len(operations) != 1:
        raise ValueError("L'expression doit contenir une opération parmi '+', '-', '*'")

    send_message(s, expr)

    s_data = s.recv(1024)
    print(s_data.decode())

finally:
    s.close()
