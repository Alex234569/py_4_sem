
import socket

sock = socket.socket()
username = input('Enter username: ')
password = input('Enter password: ')
port = input('Enter port(none for default): ')
if not port:
    port = 9090
else:
    port = int(port)
ipaddr = input('Enter IP-address(none for localhost): ')
if not ipaddr:
    ipaddr = 'localhost'

sock.connect((ipaddr, port))
sock.send((username + ';' + password).encode())

welcomeText = sock.recv(1024).decode()
print(welcomeText, end='')

while True:
    data = input('{}>'.format(username))
    sock.send(data.encode())
    if data == 'quit':
        break
    elif data == 'whoami' or data == 'time':
        answer = sock.recv(1024).decode()
        print('Server: {}'.format(answer))
    
sock.close()
