n=int(input())
cnt=1
max_val=n*n-(n-1)
for i in range(n):
    if i%2==0:
        for j in range(n):
            print(cnt,end=' ')
            cnt+=1
        print()
    else:
        for j in range(n):
            print(n*n-cnt+1,end=' ')
            cnt+=1
        print()