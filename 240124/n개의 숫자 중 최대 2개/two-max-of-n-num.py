import sys

n=int(input())

arr=list(map(int,input().split()))

max_val=-sys.maxsize

for elem in arr:
    if max_val<elem:
        max_val=elem
sec_max_val=max_val-1
if arr.count(max_val)<2:
    while True:
        if sec_max_val not in arr:
            sec_max_val-=1
        else:
            break
else:
    sec_max_val=max_val
print(max_val, sec_max_val)