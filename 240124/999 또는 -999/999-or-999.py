import sys
arr=list(map(int,input().split()))

min_val=sys.maxsize
max_val=-sys.maxsize

for elem in arr:
    if elem==-999 or elem==999:
        break
    else:
        if min_val>elem:
            min_val=elem
        elif max_val<elem:
            max_val=elem
print(max_val,min_val)