import subprocess
from colorama import Fore
import threading
import time


def ping_ip(ip_address):
    while True:
        try:
            subprocess.check_output(['ping', '-c', '4', ip_address])
            print(f"{Fore.GREEN}Ping request success.{Fore.RESET}")
            time.sleep(1)
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Ping request failed.{Fore.RESET}")
            time.sleep(1)


ip_address = input("Enter the IP address to ping: ")
print("\n")


for x in range(1000):
    thread = threading.Thread(target=ping_ip(ip_address))
    thread.start()
