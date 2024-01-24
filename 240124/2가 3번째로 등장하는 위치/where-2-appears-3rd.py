n=int(input())

arr=list(map(int,input().split()))

obj=2
cnt=0
for elem in arr:
    if elem==obj:
        cnt+=1
        if cnt==3:
            print(arr[elem]+1)
            break