#coding-utf-8

import socket
import threading
from xmlrpc import server

class ThreadedServer(threading.Thread):

    def __init__(self,client_socket, address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.address = address

    def run(self):
        print("Connexion de {}".format(self.address))
        print("En ecoute des messages...")

        data = self.client_socket.recv(1024)
        data = data.decode("utf-8")
        print("Message reçu : {}".format(data))

        self.client_socket.close()

#------------------------------------------------------------------------------
host, port = ("localhost", 5566)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
print("Le serveur est demarré sur le port {}".format(port))

while True:
    server_socket.listen(5)
    conn, address = server_socket.accept()
    print("Connexion acceptée de {}".format(address))
     
    thread = ThreadedServer(conn, address)
    thread.start()


conn.close()
server_socket.close()