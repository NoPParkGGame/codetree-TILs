n, m= tuple(map(int, input().split()))
#리스트 생성
arr=[
    [0] * m
    for _ in range(n)
]
# dx. dy 생성
dxs, dys= [0,1,0,-1], [1,0,-1,0]
dir_num=1
# 격자 위치 확인 함수 생성
def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m
x,y=0, 0
arr[x][y]=1

for i in range(2, m*n +1):
    nx, ny= x+dxs[dir_num], y+dys[dir_num]  # 가상이동 진행

    if not in_range(nx, ny) or arr[nx][ny]!=0:
        dir_num= (dir_num+3)%4
    
    x, y= x+dxs[dir_num], y+dys[dir_num]
    arr[x][y]=i

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()