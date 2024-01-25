import sys
n=int(input())

arr=list(map(int,input().split()))

max_val=-sys.maxsize

for i in range(len(arr)):
    for j in range(len(arr)-i):
        profit=arr[i+j]-arr[i]
        if profit>max_val:
            max_val=profit

if max_val==-sys.maxsize:
    print(0)
else:
    print(max_val)