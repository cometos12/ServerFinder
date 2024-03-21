import socket
import os
import main

name = input("Podaj ip serwera:")
print (f"Ipv4: {socket.gethostbyname(name)}")

