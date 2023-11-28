import socket

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.3.17', 9999))

# Récupération d'une expression arithmétique simple
expression = input("Entrez une expression arithmétique (ex. 3 + 3) : ")

# Contrôler la saisie utilisateur
try:
    # Diviser l'expression en opérandes et opérateur
    operands, operator = expression.split()
    
    # Vérifier que les opérandes sont des nombres et que l'opérateur est valide
    operand1 = int(operands[0])
    operand2 = int(operands[2])
    valid_operators = ['+', '-', '*']
    
    if operator not in valid_operators:
        raise ValueError("Opérateur invalide")

    # Vérifier que les opérandes sont dans la plage autorisée
    if not(0 <= operand1 < 2**16) or not(0 <= operand2 < 2**16):
        raise ValueError("Les nombres doivent être inférieurs à 4294967295 (2^32 - 1)")

except (ValueError, IndexError):
    print("Saisie invalide. Assurez-vous d'entrer une expression arithmétique simple.")
    s.close()
    exit(1)

# Convertir les opérandes en bytes
operand1_bytes = operand1.to_bytes(2, byteorder='big')
operand2_bytes = operand2.to_bytes(2, byteorder='big')

# Créer le message avec en-tête et séquence de fin
message = operand1_bytes + operator.encode() + operand2_bytes + b'\x00'

# Envoyer la taille du message
s.send(len(message).to_bytes(1, byteorder='big'))

# Envoyer le message sur le réseau
s.send(message)

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())

# Fermer la connexion
s.close()
