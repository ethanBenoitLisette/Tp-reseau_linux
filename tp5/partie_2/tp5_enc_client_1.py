import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.3.17', 9999))

expression = input("Entrez une expression arithmétique (ex. 3 + 3) : ")

try:
    operands, operator = expression.split()
    
    operand1 = int(operands[0])
    operand2 = int(operands[2])
    valid_operators = ['+', '-', '*']
    
    if operator not in valid_operators:
        raise ValueError("Opérateur invalide")

    if not(0 <= operand1 < 2**16) or not(0 <= operand2 < 2**16):
        raise ValueError("Les nombres doivent être inférieurs à 4294967295 (2^32 - 1)")

except (ValueError, IndexError):
    print("Saisie invalide. Assurez-vous d'entrer une expression arithmétique simple.")
    s.close()
    exit(1)

operand1_bytes = operand1.to_bytes(2, byteorder='big')
operand2_bytes = operand2.to_bytes(2, byteorder='big')

message = operand1_bytes + operator.encode() + operand2_bytes + b'\x00'

s.send(len(message).to_bytes(1, byteorder='big'))

s.send(message)

s_data = s.recv(1024)
print(s_data.decode())

s.close()
