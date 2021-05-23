


from vidstream import StreamingServer
import threading

reciver = StreamingServer('192.168.56.1', 9999)

t = threading.Thread(target=reciver.start_server)
t.start()

while input("") != 'STOP':
    continue

reciver.stop_server()