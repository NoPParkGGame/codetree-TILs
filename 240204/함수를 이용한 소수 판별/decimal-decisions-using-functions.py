def add_prime(n):
    for i in range(2, n-1):
        if n%i==0:
            return False
    return True

a, b =tuple(map(int, input().split()))
sum_val=0
for i in range(a, b+1):
    if add_prime(i) and i!=1:
        sum_val+=i

print(sum_val)