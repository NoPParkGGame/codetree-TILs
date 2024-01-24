import sys
n=int(input())
arr=list(map(int,input().split()))

min_val=sys.maxsize

for elem in arr:
    if min_val>elem:
        min_val=elem
print(min_val,arr.count(min_val))