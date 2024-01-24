import sys
n=int(input())

arr=list(map(int,input().split()))

max_val=-sys.maxsize

for elem in arr:
    if arr.count(elem)<2:
        if max_val<elem:
            max_val=elem

if max_val==-sys.maxsize:
    print(-1)
else:
    print(max_val)