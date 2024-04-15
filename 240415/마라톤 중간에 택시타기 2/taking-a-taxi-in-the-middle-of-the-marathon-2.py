import sys
n= int(input())

check=[
    tuple(map(int, input().split()))
    for _ in range(n)
]
min_dist= sys.maxsize

for i in range(1, n-1):
    new_check=[]
    dist_x=0
    dist_y=0
    for elem in check:
        if elem!=check[i]:  # new_check = [0 0, 11 -1, 10 0]
            new_check.append(elem)

    for j in range(len(new_check)-1):
        dist_x= dist_x + abs(new_check[j+1][0] - new_check[j][0])
        dist_y= dist_y + abs(new_check[j+1][1] - new_check[j][1])


    total_dist= dist_x + dist_y
    
    min_dist= min(min_dist, total_dist)
    
print(min_dist)