m=int(input())

for i in range(m):
    n=int(input())

    cnt=0
    while True:
        if n%2==0:
            n//=2
            cnt+=1
        elif n==1:
            print(cnt)
            break
        else:
            n=n*3+1
            cnt+=1