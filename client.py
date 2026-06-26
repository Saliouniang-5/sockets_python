#coding-utf-8

import socket
from xmlrpc import client

host, port = ("localhost", 5566)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    client_socket.connect((host, port))
    print("Client connecté au serveur {} sur le port {}".format(host, port))

    data = "Bonjour Mouride, Namoone Nalla!!!"
    data = data.encode("utf-8")
    client_socket.sendall(data)

except ConnectionRefusedError:
    print("Connexion au serveur impossible")
finally:
    client_socket.close()