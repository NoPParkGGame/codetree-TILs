string=input()
control=list(input())

for elem in control:
    if elem=='L':
        string=string[1:]+string[0]
    else:
        string=string[-1]+string[:-1]
print(string)