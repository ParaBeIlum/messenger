import socket
import select
import logging
import pathlib
import json
import os
import uuid
from sys import argv
from datetime import datetime

MAX_CONNECTIONS = 51
SERVER_IP = argv[1]
SERVER_PORTS = [8000, 8001]
inputs = []
servers = []
clients = {}


def initialize_logger():
    """
    Initializes a logger and generates a log file in ./logs.
    Returns
    -------
    logging.Logger
        Used for writing logs of varying levels to the console and log file.
    -------
    """
    path = pathlib.Path(os.path.join(os.getcwd(), "logs"))
    path.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger('Server')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    fh = logging.FileHandler(
        filename=f'logs/{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}_server.log'
    )
    ch.setLevel(logging.INFO)
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '[%(asctime)s] - %(levelname)s - %(message)s'
    )

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


def generate_id(string):
    """
    Generates uuid
    """
    return uuid.uuid5(uuid.NAMESPACE_DNS, string)


def get_server_socket(port):
    """
    Starts the socket server

    Parameters
    ----------
    port : int
        server socket port
    Returns
    -------
    server : object
        socket server
    -------
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((SERVER_IP, port))
    server.listen(MAX_CONNECTIONS)
    return server


def handle_sockets():
    """
    Handles server sockets behavior
    """
    readable, _, exceptional = select.select(inputs, [], inputs)
    for sock in readable:
        if sock in servers:
            client_socket, client_address = sock.accept()
            logger.info(f"New connection from {client_address}.")
            client_socket.setblocking(0)
            data = client_socket.recv(1024).decode()
            if not data:
                continue
            if sock == servers[0]:
                if data in clients:
                    client_socket.send(''.encode())
                else:
                    uid = str(generate_id(data))
                    encoded = uid.encode()
                    client_socket.send(encoded)
                    clients[data] = uid
                    logger.info(f"Registered new user with identifier <{data}>")
            else:
                data_json = json.loads(data)
                identifier = data_json['identifier']
                code = data_json['code']
                mess = data_json['message']
                if identifier in clients and clients[identifier] == code:
                    message = "Your message saved to log."
                    client_socket.send(message.encode())
                    logger.info(f"MESSAGE - {identifier} >>> {mess}")
                else:
                    message = "Error detected. Check your identifier and code."
                    client_socket.send(message.encode())
                    logger.error("Wrong identifier - code pair.")
        continue


if __name__ == '__main__':
    logger = initialize_logger()
    for port in SERVER_PORTS:
        server_socket = get_server_socket(port)
        inputs.append(server_socket)
        servers.append(server_socket)
        logger.info(f"Server started on {SERVER_IP}:{port}")
    try:
        while True:
            handle_sockets()
    except Exception as e:
        logger.error(e)
    except KeyboardInterrupt:
        logger.warning("Keyboard interrupt detected!")
