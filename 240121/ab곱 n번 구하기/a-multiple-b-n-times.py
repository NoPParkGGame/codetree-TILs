n=int(input())

for i in range(n):
    arr=input().split()
    a,b=int(arr[0]), int(arr[1])

    prod=1

    for j in range(a,b+1):
        prod*=j
    print(prod)