import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    dataBytes = sock.recv(1024)
    data = dataBytes.decode()
    if data == 'quit':
        break
    if data:
        print(data)
    
sock.close()
