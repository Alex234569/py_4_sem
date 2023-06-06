import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = input()
    dataBytes = data.encode()
    conn.send(dataBytes)
    if data == 'quit':
        break
    
conn.close()
