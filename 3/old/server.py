import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
message = 'hello, world!'
messageBytes = message.encode()
sock.send(messageBytes)

dataBytes = sock.recv(1024)
data = dataBytes.decode()
sock.close()

print(data)
