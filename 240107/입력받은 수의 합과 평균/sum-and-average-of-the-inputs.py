n=int(input())
sum_val=0

for _ in range(n):
    nums=int(input())
    sum_val+=nums
print(f'{sum_val} {sum_val/n:.1f}')