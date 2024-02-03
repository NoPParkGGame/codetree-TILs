string=input()

for elem in string:
    if ord('A')<= ord(elem) <ord('Z'):
        print(elem.lower(), end='')
    else:
        print(elem.upper(), end='')