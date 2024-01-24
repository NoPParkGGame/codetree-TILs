import sys
n=int(input())

arr=list(map(int,input().split()))

while len(arr)>1:
    max_val=-sys.maxsize
    for elem in arr:
        if max_val<elem:
            max_val=elem
    print(arr.index(max_val)+1,end=' ')
    arr=arr[:arr.index(max_val)]