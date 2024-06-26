n, m= tuple(map(int, input().split()))

arr=[
    [0]*m
    for _ in range(n)
]

dxs, dys= [0,1,0,-1], [1,0,-1,0]
dir_num=0
x,y=0, 0

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m
    
alph=65
arr[x][y]=chr(alph)

for i in range(1, m*n):
    nx, ny= x+dxs[dir_num], y+ dys[dir_num]

    if not in_range(nx, ny) or arr[nx][ny]!=0:
        dir_num= (dir_num+1)%4
    
    x, y= x+dxs[dir_num], y+ dys[dir_num]

    if alph>=90:
        alph=64
    alph+=1
    arr[x][y]=chr(alph)

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()