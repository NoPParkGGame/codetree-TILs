import sys

n= int(input())

rooms=[int(input()) for _ in range(n)]
min_val= sys.maxsize

for _ in range(n):
    dist=0
    for i in range(n):
        dist= dist+ i*rooms[i]
    min_val=min(min_val, dist)
    rooms= rooms[1:] + rooms[:1]

print(min_val)