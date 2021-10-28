# messenger
===========

This project is intended for demonstration for a job interview in Veeame Software company.

It is a simple system for client-server communication.
The server keeps open ports 8000 and 8001, at startup the client choose an identifier and connects to the server on port 8000, sends him identifier and recieves unique code.
After that client connects to the server on port 8001 and sends identifier, message and code obtained on the previous steps. If the code does not match its unique identifier, the server returns an error message to the client. If the code is correct, the server writes the received message to the log.
The server supports the ability to work simultaneously with at least 50 clients.
To implement the interaction between the server and the client of the system is used sockets with TCP protocol.


```
MIT License
 
Copyright (c) 2017 Open DevOps Community
 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
