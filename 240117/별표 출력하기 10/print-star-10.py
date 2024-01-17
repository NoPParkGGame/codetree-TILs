n=int(input())
cnt=0
for i in range(2*n):
    if i%2==0:
        for j in range(i//2+1):
            print('*',end=' ')
        print()
    else:
        for k in range(n-cnt):
            print('*',end=' ')
        print()
        cnt+=1