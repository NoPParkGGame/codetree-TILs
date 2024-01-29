n, m = tuple(map(int,input().split()))

placed=[
    [0 for _ in range(10)]
    for _ in range(10)
]
num=1
for _ in range(m):
    r, c = tuple(map(int,input().split()))
    placed[r][c]=num
    num+=1

for i in range(1,n+1):
    for j in range(1,n+1):
        print(placed[i][j],end=' ')
    print()