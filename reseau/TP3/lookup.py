from socket import gethostbyname
from sys import argv

print(gethostbyname(f"{argv[1]}"))
