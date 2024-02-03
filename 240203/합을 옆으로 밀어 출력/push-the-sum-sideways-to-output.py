n=int(input())
sum_val=0
for _ in range(n):
    num=int(input())
    sum_val+=num

print(str(sum_val)[1:]+str(sum_val)[0])