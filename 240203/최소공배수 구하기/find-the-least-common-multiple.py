def min_com(n, m):
    cnt=0
    arr=[]
    prod_val=1
    for i in range(1, min(n, m)+1):
        if m%i==0 and n%i==0:
            arr.append(i)
            m//=i; n//=i
    arr.append(m)
    arr.append(n)
    for elem in arr:
        prod_val*=elem
    print(prod_val)
n, m = tuple(map(int, input().split()))

min_com(n, m)