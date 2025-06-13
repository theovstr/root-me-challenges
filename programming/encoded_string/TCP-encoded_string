import socket
import re
import math
import base64

client_socket = socket.socket()
client_socket.connect(("challenge01.root-me.org", 52023))

data = client_socket.recv(1024).decode() #data is printing correctly
first = re.search(r"'([^']*)'", data).group(1)
first = base64.b64decode(first)
print(f"{data}\n")
print(f"decoded base64 : {first.decode('utf-8')}")

client_socket.send((first.decode('utf-8') + '\n').encode())
print("Sending decoded string to server...\n")
data = client_socket.recv(1024).decode() #data is printing correctly
print(f"We get the flag : \n{data}", end="")
