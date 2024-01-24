n=int(input())

arr=list(map(int,input().split()))

obj=2
cnt=0
for i in range(n):
    if arr[i]==obj:
        cnt+=1
        if cnt==3:
            print(arr[i]+1)
            break