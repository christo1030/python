

__author__ = ''

import socket
import thread
import time

BUFFER_SIZE = 20  # Normally 1024, but we want fast response
TCP_IP = '0.0.0.0'
TCP_PORT = 51000
def StartListening():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(5)
    while 1:
        (conn, addr) = s.accept()
        print 'Connection address:', addr
        #ct = client_thread(conn,addr)
        #'ct.run()
        try:
            thread.start_new_thread(client_thread,(conn,addr))
        except:
            print "Thread not created"

def client_thread(conn, addr):
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    while 1:

        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
        conn.send(data)  # echo
    conn.close()

if __name__ =='__main__':
    StartListening()
