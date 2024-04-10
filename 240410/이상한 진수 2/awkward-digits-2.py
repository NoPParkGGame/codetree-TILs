import sys
binary= list(input())

max_val= -sys.maxsize

for i in range(len(binary)):
    binary[i]=int(binary[i])
    if binary[i]==1:
        binary[i]=0
    else:
        binary[i]=1
    n=0
    for elem in binary:
        n=n*2 + int(elem)

    max_val= max(max_val, n)

    if binary[i]==1:
        binary[i]=0
    else:
        binary[i]=1

print(max_val)