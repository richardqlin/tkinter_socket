import socket

import threading

host = '0.0.0.0'

port = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(5)



clients_dict={}


def broadcast(message):
    for c in clients_dict:
        print(c)
        clients_dict[c].send(message)

def handle(client,name):
    global clients_dict
    while 1:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            client.close()
            del clients_dict[name]
            break


def receive():
    while 1:
        client, address = s.accept()
        data = client.recv(1024)
        clients_dict[data] = client
        broadcast(data+ ' connected to the server '.encode('utf-8'))
        thread = threading.Thread(target=handle, args = (client,data,))
        thread.start()

receive()
print('sever run')
