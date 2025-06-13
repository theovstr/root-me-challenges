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

we should then calculate the square root of 953,

```python
number = re.findall(r'\d+', data)
```
