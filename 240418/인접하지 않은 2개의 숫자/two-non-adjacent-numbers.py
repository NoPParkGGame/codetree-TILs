import sys
n=int(input())
nums=list(map(int, input().split()))

max_val= -sys.maxsize

for i in range(n):
    for j in range(i+2, n):
        sum_val= nums[i] + nums[j]
        max_val=max(max_val, sum_val)
print(max_val)