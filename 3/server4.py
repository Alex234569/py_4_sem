from datetime import datetime
import socket


log = open('log.txt', 'a')
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
log.write('{} Server started\n'.format(datetime.now()))
conn, addr = sock.accept()
log.write('{} Connection attempt from IP {}\n'.format(datetime.now(), addr[0]))
username, password = (conn.recv(1024).decode()).split(';')
log.write('{} User \"{}\" authentication attempt\n'.format(datetime.now(), username))

welcomeText = ''
auth = False
userFound = False
users = open('users.txt')
for line in users:
    line = line.strip('\n')
    words = line.split(';')
    if words[0] == username:
        userFound = True
        welcomeText += 'Hello, {}!\n'.format(username)
        if words[1] == password:
            auth = True
            break
        else:
            welcomeText += 'Wrong password!\n'
            break

if not userFound:
    welcomeText += 'Sorry, we do not know you\n'
    log.write('{} Unknown user\n'.format(datetime.now()))

if auth:
    log.write('{} User \"{}\" successfully logged in\n'.format(datetime.now(), username))
    conn.send(welcomeText.encode())
    log.write('{} Server message:\n'.format(datetime.now()))
    log.write(welcomeText)
    while True:
        data = conn.recv(1024).decode()
        print('{} {}: {}'.format(datetime.now(), username, data))
        log.write('{} User \"{}\" message:\n'.format(datetime.now(), username))
        log.write(data + '\n')
        if data == 'quit':
            log.write('{} User \"{}\" closed connection\n'.format(datetime.now(), username))
            break
        elif data == 'time':
            message = str(datetime.now())
            conn.send(message.encode())
            log.write('{} Server message:\n'.format(datetime.now()))
            log.write(message + '\n')
        elif data == 'whoami':
            message = username
            conn.send(message.encode())
            log.write('{} Server message:\n'.format(datetime.now()))
            log.write(message + '\n')
else:
    log.write('{} Authentication attempt failed\n'.format(datetime.now()))
    conn.send(welcomeText.encode())
    log.write('{} Server message:\n'.format(datetime.now()))
    log.write(welcomeText)


log.write('{} Server closed\n'.format(datetime.now()))
log.close()
conn.close()