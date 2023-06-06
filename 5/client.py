import socket
import pickle
import cryptocode


HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = 7, 5, 3
A = g ** a % p
sock.send(pickle.dumps((p, g, A)))
B = pickle.loads(sock.recv(1024))
K = B ** a % p
key = str(K)
msgEncrypted = pickle.loads(sock.recv(1024))
print('Encrypted message:', msgEncrypted)
msg = cryptocode.decrypt(msgEncrypted, key)
print('Decrypted message:', msg)

sock.close()
