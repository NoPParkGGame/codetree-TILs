import sys
n= int(input())

rooms=[
    int(input())
    for _ in range(n)
]

min_dist= sys.maxsize

for i in range(n):
    dist=0

    for j in range(i+1, n+i):

        dist= dist + abs(j-i) * rooms[(i+j)%5]

    min_dist= min(min_dist, dist)

print(min_dist)