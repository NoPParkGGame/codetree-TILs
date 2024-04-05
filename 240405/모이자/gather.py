import sys
n= int(input())

arr= list(map(int, input().split()))
# 최솟값 임의 설정
min_val=sys.maxsize

# 이동 거리를 구하는 함수 생성
def dist_val(i, j):
    if i!=j:
        return abs(i-j)
    return 0

for i in range(n):
    sum_dist=0  
    arrive=arr[i]   # 차례로 집결지를 바꿔보기

    for j in range(n):
        sum_dist= sum_dist+ (dist_val(i, j) * arr[j])

    min_val= min(min_val, sum_dist)

print(min_val)