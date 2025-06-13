import socket
import re
import math

def sqrt_multiply(sqrt :str, mult :str) -> int:
    to_send = math.sqrt(int(sqrt))
    print(f"square root of first number : {to_send}")
    to_send *= int(mult)
    print(f"multiply by the second number : {to_send}")
    return (format(to_send, '.2f'))


client_socket = socket.socket()
client_socket.connect(("challenge01.root-me.org", 52002))

data = client_socket.recv(1024).decode() #data is printing correctly
number = re.findall(r'\d+', data)
print(f"{data}\n")

print(f"We then put the number in a list : \n{number}\n") #get number (in list)
#message is always the same syntax so we know what to send to function

value = sqrt_multiply(number[1], number[2])
print(f"We get the rounded value of : {value}")
client_socket.send((str(value) + "\n").encode())
print(f"\nSending the result...")
data = client_socket.recv(1024).decode()
print(f"We received the flag : \n{data}")
