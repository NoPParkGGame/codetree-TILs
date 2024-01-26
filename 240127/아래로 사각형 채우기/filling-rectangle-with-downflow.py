n=int(input())


arr=[
    [0 for _ in range(n)]
    for _ in range(n)
]

num=1
for i in range(n):
    n1=num
    n2=num
    if i%2==0:
        for j in range(n): 
            arr[i][j]=n1
            n1+=n
    else:
        for j in range(n):
            arr[i][j]=n2
            n2+=n
    num+=1
for row in arr:
    for elem in row:
        print(elem,end=' ')
    print()