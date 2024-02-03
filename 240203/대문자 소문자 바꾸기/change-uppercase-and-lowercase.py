string=input()

for elem in string:
    if ord('A')<= ord(elem) <ord('Z'):
        print(elem.lower(), end='')
    if ord('a')<= ord(elem) <ord('z'):
        print(elem.upper(), end='')