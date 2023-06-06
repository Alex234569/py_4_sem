import socket

sock = socket.socket()

hostName = input('Enter your name(none for default): ')
if not hostName:
    hostName = 'defaultUser'
port = input('Enter port(none for default): ')
if not port:
    port = 9090
else:
    port = int(port)
ipaddr = input('Enter IP-address(none for localhost): ')
if not ipaddr:
    ipaddr = 'localhost'

sock.connect((ipaddr, port))
sock.send(hostName.encode())
welcomeText = sock.recv(1024).decode()
print(welcomeText)

while True:
    data = input('{}>'.format(hostName))
    dataBytes = data.encode()
    sock.send(dataBytes)
    if data == 'quit':
        break
    
sock.close()
