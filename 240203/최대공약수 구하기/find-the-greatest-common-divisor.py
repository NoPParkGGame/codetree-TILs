def max_com(n, m):
    for i in range(1, m):
        if n%i==0 and m%i==0:
            value=i
    print(value)

n, m = tuple(map(int, input().split()))

max_com(n, m)