string=list(input())

while len(string)>1:
    num=int(input())
    if num>=len(string):
        string.pop(-1)
    else:
        string.pop(num)
    print(''.join(string))