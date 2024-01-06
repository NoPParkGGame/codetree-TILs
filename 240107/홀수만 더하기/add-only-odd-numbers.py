n=int(input())
sum_val=0
for _ in range(n):
    nums=int(input())
    if nums%2==1 and nums%3==0:
        sum_val+=nums

print(sum_val)