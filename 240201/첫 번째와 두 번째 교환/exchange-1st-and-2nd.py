string=list(input())

for elem in string:
    if elem==string[0]:
        elem=string[1]
    elif elem==string[1]:
        elem=string[0]

print(''.join(string))