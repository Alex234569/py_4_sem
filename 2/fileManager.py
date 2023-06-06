from properties import *

currentDirectory = rootDirectory
rootLen = len(rootDirectory)
directoryDepth = 0
command = input(currentDirectory[rootLen:] + '> ')

while command != 'quit':
    words = list(command.split(' '))
    wordsLen = len(words)
    if words[0] == 'changedir':
        if wordsLen == 2:
            newPath = os.path.join(currentDirectory, words[1])
            if os.path.exists(newPath):
                currentDirectory = newPath
                directoryDepth += 1
            else:
                print('This directory does not exist')
        else:
            print('Invalid number of arguments')
    elif words[0] == 'levelup':
        if wordsLen == 1:
            if directoryDepth:
                currentDirectory = os.path.dirname(currentDirectory)
                directoryDepth -= 1
            else:
                print('You cannot leave root directory')
        else:
            print('Invalid number of arguments')
    elif words[0] == 'makedir':
        if wordsLen == 2:
            create_directory(currentDirectory, words[1])
        else:
            print('Invalid number of arguments')
    elif words[0] == 'deldir':
        if wordsLen == 2:
            delete_directory(currentDirectory, words[1])
        else:
            print('Invalid number of arguments')
    elif words[0] == 'makefile':
        if wordsLen == 2:
            create_file(currentDirectory, words[1])
        else:
            print('Invalid number of arguments')
    elif words[0] == 'writefile':
        if wordsLen > 2:
            write_file(currentDirectory, words[1], words[2:])
        else:
            print('Invalid number of arguments')
    elif words[0] == 'readfile':
        if wordsLen == 2:
            read_file(currentDirectory, words[1])
        else:
            print('Invalid number of arguments')
    elif words[0] == 'delfile':
        if wordsLen == 2:
            delete_file(currentDirectory, words[1])
    elif words[0] == 'copyfile':
        if wordsLen == 3:
            copy_file(currentDirectory, words[1], words[2])
        else:
            print('Invalid number of arguments')
    elif words[0] == 'movefile':
        if wordsLen == 3:
            move_file(currentDirectory, words[1], words[2])
    elif words[0] == 'renamefile':
        if wordsLen == 3:
            rename_file(currentDirectory, words[1], words[2])
        else:
            print('Invalid number of arguments')
    else:
        print('Incorrect command')
    command = input(currentDirectory[rootLen:] + '> ')

print('Goodbye!')
