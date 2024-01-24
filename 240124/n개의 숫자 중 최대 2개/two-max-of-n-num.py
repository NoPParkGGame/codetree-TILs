import sys

n=int(input())

arr=list(map(int,input().split()))

max_val=-sys.maxsize

for elem in arr:
    if max_val<elem:
        max_val=elem
sec_val=max_val
for i in range(max_val):
    sec_val-=1
    if sec_val in arr:
        break


print(max_val, sec_val)