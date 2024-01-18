n=int(input())
cnt=1
if n%2==1:
    max_val=n*n
else:
    max_val=n*n-n+1
for i in range(n):
    if i%2==0:
        for j in range(n):
            print(cnt,end=' ')
            cnt+=1
        print()
    else:
        for j in range(n):
            print(max_val-cnt+1,end=' ')
            cnt+=1
        print()
        '''
    4 5 6
    6 5 4

    cnt+cnt+n-1
    5 6 7 8 
    8 7 6 5
    i=1 j=cnt

    16 15 14 13
    13 14 15 16
    i=3 j= cnt
    '''