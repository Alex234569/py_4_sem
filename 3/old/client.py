import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    dataBytes = conn.recv(1024)
    data = dataBytes.decode()
    if data == 'quit':
        break
    data = data.upper()
    dataBytes = data.encode()
    conn.send(dataBytes)

conn.close()
