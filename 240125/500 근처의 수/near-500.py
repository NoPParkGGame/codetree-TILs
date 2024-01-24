import sys
arr=list(map(int,input().split()))

max_val=-sys.maxsize
min_val=sys.maxsize

for elem in arr:
    if max_val<elem<500:
        max_val=elem
    if min_val>elem>500:
        min_val=elem
print(max_val,min_val)