n=int(input())

arr=[
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    arr[i][0]=1

for i in range(1,n):
    for j in range(1,n):
        if i==j:
            arr[i][j]=1
        arr[i][j]=arr[i-1][j]+arr[i-1][j-1]


for row in arr:
    for elem in row:
        if elem==0:
            continue
        else:
            print(elem,end=' ')
    print()