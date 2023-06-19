import socket
from time import sleep

count  = 4

HOST = "192.168.193.170"

PORT = 39000

sendMessage = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")