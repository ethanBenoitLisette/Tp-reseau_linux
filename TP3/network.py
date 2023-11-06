from psutil import net_if_addrs
from sys import argv
from os import system
from socket import gethostbyname

if argv[1] == "lookup":
    print(gethostbyname(f"{argv[2]}"))
    
if argv[1] == "ping":
    if system(f"ping {argv[2]}") == 0:
        print("UP !")
    else :
        print("DOWN !")
if argv[1] == "ip":
    def get_own_ip_addresses():
        own_ip_addresse = []

        for interface, addrs in net_if_addrs().items():
            for addr in addrs:
                if addr.family == 2 and not addr.address.startswith("127.") and not addr.address.startswith("169.254.") and not addr.address.startswith("10.1.") and not addr.address.startswith("192.168."):
                    own_ip_addresse.append((interface, addr.address))

        return own_ip_addresse

    if __name__ == "__main__":
        own_ips = get_own_ip_addresses()
        
        if own_ips:
            for interface, ip in own_ips:
                print(f" {ip}")
        else:
            print("No own IP addresses found.")
if argv[1] != "lookup" and argv[1] != "ip" and argv[1] != "ping" :
    print(f"{argv[1]} is not a valid command. Déso.")
