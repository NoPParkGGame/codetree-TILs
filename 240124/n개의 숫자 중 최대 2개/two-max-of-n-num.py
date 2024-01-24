import sys

n=int(input())

arr=list(map(int,input().split()))

max_val=-sys.maxsize

sec_arr=[]

for elem in arr:
    if max_val<elem:
        max_val=elem
sec_val=max_val

if arr.count(max_val)<2:
    arr.remove(max_val)
    sec_val=-sys.maxsize
    for elem in arr:
        if sec_val<elem:
            sec_val=elem

print(max_val, sec_val)