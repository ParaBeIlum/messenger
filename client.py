import socket
import errno
import sys
import json


SERVER_PORTS = [8000, 8001]


def connect_server(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    return client_socket


while True:
    identifier = input("Enter your unique identifier: ")
    code_getting_socket = connect_server(sys.argv[1], SERVER_PORTS[0])
    data = identifier.encode()
    code_getting_socket.send(data)
    server_response = code_getting_socket.recv(1024)
    if server_response:
        print(server_response.decode())
        break
    else:
        print("Choose another identifier. This one is taken!")
code_getting_socket.close()
identifier = input("Enter your identifier: ")
code = input("Enter your verification code: ")
message = input("Enter your message: ")
data = json.dumps({"identifier": identifier, "code": code, "message": message})
message_sending_socket = connect_server(sys.argv[1], SERVER_PORTS[1])
message_sending_socket.send(data.encode())
try:
    response = message_sending_socket.recv(1024)
    if not len(response):
        print("Connection closed by the server.")
        sys.exit()
    print(response.decode())
except IOError as e:
    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
        print(f"Reading error: {str(e)}.")
        sys.exit()
except Exception as e:
    print(f"Reading error: {str(e)}.")
    sys.exit()
