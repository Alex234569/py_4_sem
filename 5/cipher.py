import cryptocode


text = 'Hello, world!'
key = str(1)
encodedText = cryptocode.encrypt(text, key)
print(encodedText)
print(cryptocode.decrypt(encodedText, key))