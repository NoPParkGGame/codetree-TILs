n=int(input())

cnt=n
for i in range(1,n+1):  #i=1
    for j in range(n-i+1):    #j=n-i=5-1=4 +1
        print(f'{i} * {j+1} = {i*(j+1)}',end='')
        if j<n-i:
            print(end=' / ')
    print()

'''
i   j   n
1   5   5
2   4   5
3   3   5

'''