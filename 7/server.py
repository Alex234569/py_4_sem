import socket
import os


def process(req):
    words = req.split(' ')
    wordsLen = len(words)
    if words[0] == 'touch':
        if wordsLen == 2:
            return create_file(rootDirectory, words[1])
        else:
            return 'Invalid number of arguments'
    elif words[0] == 'writefile':
        if wordsLen > 2:
            return write_file(rootDirectory, words[1], words[2:])
        else:
            return 'Invalid number of arguments'
    elif words[0] == 'readfile':
        if wordsLen == 2:
            return read_file(rootDirectory, words[1])
        else:
            return 'Invalid number of arguments'
    elif words[0] == 'delfile':
        if wordsLen == 2:
            return delete_file(rootDirectory, words[1])
        else:
            return 'Invalid number of arguments'
    elif words[0] == 'quit':
        return 'Goodbye!'
    return 'Invalid command'

def create_file(path, name):
    filename = os.path.join(path, name)
    if not os.path.exists(filename):
        open(filename, 'a').close()
        return 'Successfully created file'
    else:
        return 'File already exists'

def write_file(path, name, words):
    filename = os.path.join(path, name)
    file = open(filename, 'a')
    text = ''
    for word in words:
        text += str(word) + ' '
    file.write(text)
    file.close()
    return 'Successfully added text'

def read_file(path, name):
    filename = os.path.join(path, name)
    if os.path.exists(filename):
        file = open(filename, 'r')
        text = file.read()
        file.close()
        return text
    else:
        return 'File does not exist'
    
def delete_file(path, name):
    filename = os.path.join(path, name)
    if os.path.exists(filename):
        os.remove(filename)
        return 'Successfully deleted file'
    else:
        return 'File does not exist'

rootDirectory = os.path.dirname(os.path.abspath(__file__))
dirName = 'root'
rootDirectory = os.path.join(rootDirectory, dirName)
if not os.path.exists(rootDirectory): os.mkdir(rootDirectory)

sock = socket.socket()
sock.bind(('', 6666))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    request = conn.recv(1024).decode()
    print('Client:', request)
    response = process(request)
    conn.send(response.encode())
    if request == 'quit': break

conn.close()