# TCP - Back to school

This is a simple program that connect a client to a server.
Using a socket, with a TCP connection.

The goal of this exercise is to receive a string from a server,
take two numbers that is given in the string,
calculate the square root of the first one,
and multiply it by the second one,
round the result to two decimal places,
and we have 2 seconds to return the result to the server to get the flag password.


We first receive a string  like this: 

```bash
====================
 GO BACK TO COLLEGE
====================
You should tell me the answer of this math operation in less than 2 seconds !

Calculate the square root of 953 and multiply by 9946 =
```
We first need to extract the numbers in the string ( only the one we want)
Using a regular expresion it is very easy

```python
number = re.findall(r'\d+', data)
```
We will get all the digit of whatever size in a list called :```python 
number```

Then we will send the element needed in the list to a function

```python
def sqrt_multiply(sqrt :str, mult :str) -> int:
    to_send = math.sqrt(int(sqrt))
    print(f"square root of first number : {to_send}")
    to_send *= int(mult)
    print(f"multiply by the second number : {to_send}")
    return (format(to_send, '.2f'))
```

it will then return the number that we need.
after we simply need to send it back to the server and wait for the flag as a response

```python
client_socket.send((str(value) + "\n").encode())
```

( don't forget to receive from the server one more time )
thx to Amine for helping at the end !
