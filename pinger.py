import socket
from colorama import Fore
import threading
import time


def ping_ip(ip_address):
    while True:
        try:
            socket.inet_aton(ip_address)
            print(f"{Fore.GREEN}Ping successful{Fore.RESET}")
        except socket.error:
            print(f"{Fore.RED}Ping failed{Fore.RESET}")


ip_address = input("Enter the IP address to ping: ")
print("\n")


for x in range(1000):
    thread = threading.Thread(target=ping_ip(ip_address))
    thread.start()
