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

    expr_len = len(expr)

    s.sendall(struct.pack('!I', expr_len))

    s.sendall(expr.encode())

    s_data = s.recv(1024)
    print(s_data.decode())

finally:
    s.close()
