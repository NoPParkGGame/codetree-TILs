def add_total(n):
    sum_val=0
    for  i in range(1, n+1):
        sum_val+=i
    
    return sum_val//10

N=int(input())

answer=add_total(N)

print(answer)