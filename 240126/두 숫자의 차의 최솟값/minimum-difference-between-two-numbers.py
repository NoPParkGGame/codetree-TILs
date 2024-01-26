import sys
n=int(input())

arr=list(map(int,input().split()))

min_val=sys.maxsize

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]-arr[i]<min_val:
            min_val=arr[j]-arr[i]

print(min_val)



'''
len(arr)==5
i   j
0   1  
0   2
0   3
0   4

1   2
1   3
1   4

2   3  
3   4

'''