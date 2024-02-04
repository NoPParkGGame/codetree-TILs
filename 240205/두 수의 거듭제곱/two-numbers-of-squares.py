a, b = tuple(map(int, input().split()))

def multi_num(a, b):
    prod_val=1
    for _ in range(b):
        prod_val*=a
    return prod_val
print(multi_num(a, b))