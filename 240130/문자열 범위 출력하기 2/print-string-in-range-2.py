word=input()
n=int(input())
cnt=0

for elem in word[::-1]:
    if len(word)<11:
        print(elem,end='')
    else:
        print(elem,end='')
        cnt+=1
        if cnt>11:
            break