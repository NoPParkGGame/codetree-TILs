n=int(input())
cnt=1
for i in range(n):
    if i+cnt>9:
        cnt=-1
    for j in range(n):
        if i>j:
            print(' ',end=' ')
        else:
            print(i+cnt,end=' ')
            cnt+=1
    cnt-=1

    print()