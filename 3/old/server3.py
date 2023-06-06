import socket

SERVER_NAME = 'OUR_MIGHTY_SERVER'
logFile = open('log.txt', 'a')
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
logFile.write('___Server started___\n')
conn, addr = sock.accept()
#print(addr[0])
username = conn.recv(1024).decode()
logFile.write('___User with name \'{}\' with IP-address {} is trying to connect___\n'.format(username, addr[0]))

ipaddrFoundFlag = False

cleintsFile = open('clients.txt', 'r')

welcomeText = ''
for line in cleintsFile:
    line = line.strip('\n')
    words = line.split(';')
    if words[0] == addr[0]:
        welcomeText += 'Hello, {}!'.format(words[1])
        ipaddrFoundFlag = True
        if username != words[1]:
                welcomeText += '\nWhy did you change your name?'
        break

if not ipaddrFoundFlag:
    cleintsFile = open('clients.txt', 'a')
    cleintsFile.write('\n' + addr[0] + ';' + username)
    cleintsFile.close()
    welcomeText += 'Hi!'

conn.send(welcomeText.encode())
logFile.write('{}: {}\n'.format(SERVER_NAME, welcomeText))

while True:
    dataBytes = conn.recv(1024)
    data = dataBytes.decode()
    if data == 'quit':
        logFile.write('___User closed connection___\n')
        break
    if data:
        print(username + ': ' + data)
        logFile.write(username + ': ' + data + '\n')

logFile.write('___Server off___\n')
logFile.close()
conn.close()
