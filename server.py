__author__ = 'Christo'

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp
sock.bind(("127.0.0.1", 8000))
sock.listen(2)
(client, (ip, port)) = sock.accept() # accept is a blocking statement. will be waiting for connection
client.send("Welcome to Python Server")
rec = client.recv(2012)   # recv is a blocking statement, until a connection is re
while(1):
    if client:
        print client
        print ip
        print port
        print rec





