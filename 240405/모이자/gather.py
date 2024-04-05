import sys
n= int(input())

arr= list(map(int, input().split()))
# 최솟값 임의 설정
min_val=sys.maxsize

for i in range(n):
    sum_dist=0  

    for j in range(n):
        sum_dist= sum_dist+ abs(i-j) * arr[j]

    min_val= min(min_val, sum_dist)

print(min_val)