n=int(input())

def all_sum(n):
    if n==0:
        return 0
    return all_sum(n-1) + n

print(all_sum(n))