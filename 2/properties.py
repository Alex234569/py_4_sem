import os
import shutil

def create_directory(currentPath, name):
    path = os.path.join(currentPath, name)
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print('Directory already exists')

def delete_directory(currentPath, name):
    path = os.path.join(currentPath, name)
    if os.path.exists(path):
        os.rmdir(path)
    else:
        print('Directory does not exist')

def create_file(currentPath, name):
    filename = os.path.join(currentPath, name)
    if not os.path.exists(filename):
        open(filename, 'a').close()
    else:
        print('File already exists')

def write_file(currentPath, name, words):
    filename = os.path.join(currentPath, name)
    if not os.path.exists(filename):
        print('New file created')
    file = open(filename, 'a')
    text = ''
    for word in words:
        text += str(word) + ' '
    file.write(text)
    file.close()

def read_file(currentPath, name):
    filename = os.path.join(currentPath, name)
    if os.path.exists(filename):
        file = open(filename, 'r')
        text = file.read()
        file.close()
        print(text)
    else:
        print('File does not exist')

def delete_file(currentPath, name):
    filename = os.path.join(currentPath, name)
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print('File does not exist')

def copy_file(currentPath, name, destination):
    sourcePath = os.path.join(currentPath, name)
    destinationPath = os.path.join(rootDirectory, destination)
    if os.path.exists(sourcePath) and os.path.exists(destinationPath):
        shutil.copy(sourcePath, destinationPath)
    else:
        print('Invalid path')

def move_file(currentPath, name, destination):
    sourcePath = os.path.join(currentPath, name)
    destination = os.path.join(rootDirectory, destination)
    destinationPath = os.path.join(destination, name)
    if os.path.exists(sourcePath) and os.path.exists(destination):
        os.replace(sourcePath, destinationPath)
    else:
        print('Invalid path')

def rename_file(currentPath, name, newName):
    oldPath = os.path.join(currentPath, name)
    newPath = os.path.join(currentPath, newName)
    if os.path.exists(oldPath):
        os.rename(oldPath, newPath)
    else:
        print('Invalid path')


rootDirectory = os.path.dirname(os.path.abspath(__file__))
dirName = 'root'
rootDirectory = os.path.join(rootDirectory, dirName)
if not os.path.exists(rootDirectory):
    os.mkdir(rootDirectory)
