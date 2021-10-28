# messenger

<h2>Simple system for client-server communication.</h2>
The server keeps open ports 8000 and 8001, at startup the client choose an identifier and connects to the server on port 8000, sends him identifier and recieves unique code.
After that client connects to the server on port 8001 and sends identifier, message and code obtained on the previous steps. If the code does not match its unique identifier, the server returns an error message to the client. If the code is correct, the server writes the received message to the log.
The server supports the ability to work simultaneously with at least 50 clients.
To implement the interaction between the server and the client of the system is used sockets with TCP protocol.
