from sys import argv
from os import system

if system(f"ping {argv[1]}") == 0:
    print("UP !")
else :
    print("DOWN !")
