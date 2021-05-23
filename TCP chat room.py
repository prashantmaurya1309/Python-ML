import threading
import socket

host = '127.0.0.1'  #local host
port = 55555

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle(client):
    while True:
        try:
            msg= client.recv(1024)
            broadcast(msg)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast(f'{nickname} has left the chat room'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client,address = server.accept()
        print(f'connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname= client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'nickname of client is {nickname}')
        broadcast(f'{nickname} has joined the chat'.encode('ascii'))
        client.send(f'connected to server'.encode('ascii'))

        thread = threading.Thread(target=handle(),args=(client,))
        thread.start()

print('server is listening......')
receive()