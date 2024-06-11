import socket
from colorama import Fore
import threading
import time


def ping_ip(ip_address):
    # Loop pinging
    while True:
        try:
            # ping command
            socket.inet_aton(ip_address)
            print(f"{Fore.GREEN}Ping successful{Fore.RESET}")
        except socket.error:
            print(f"{Fore.RED}Ping failed{Fore.RESET}")


# Get user input for IP
ip_address = input("Enter the IP address to ping: ")
print("\n")


# Spam threads for ping function
for x in range(1000):
    thread = threading.Thread(target=ping_ip(ip_address))
    thread.start()
