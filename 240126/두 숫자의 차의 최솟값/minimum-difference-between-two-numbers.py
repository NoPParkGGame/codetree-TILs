import sys
n=int(input())

arr=list(map(int,input().split()))

min_val=sys.maxsize

for i in range(len(arr)):
    for j in range(1,len(arr)-(i+1)):
        if arr[i+j]-arr[i]<min_val:
            min_val=arr[i+j]-arr[i]

print(min_val)

'''
0   1234
1   123
2   12



'''