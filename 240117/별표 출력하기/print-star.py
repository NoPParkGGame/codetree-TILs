n=int(input())
m=n-1
for i in range(n):
    for _ in range(i+1):
        print('*',end=' ')
    print()
for i in range(m):
    for _ in range(m-i):
        print('*',end=' ')
    print()