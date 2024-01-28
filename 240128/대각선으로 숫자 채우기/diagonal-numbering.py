n,m =tuple(map(int,input().split()))

arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt=0
num=1

while num<=m*n:
    for i in range(cnt+1):
        for j in range(cnt+1):
            if i+j==cnt and i<n and j<m:
                arr[i][j]=num
                num+=1
    cnt+=1

for row in arr:
    for elem in row:
        print(elem,end=' ')
    print()


'''
0 0

0 1
1 0

0 2
1 1
2 0

1 2
2 1

2 2
'''