n, m= tuple(map(int, input().split()))
# N*N격자, M번 색칠
# 0으로 이루어진 격자 생성
arr=[
    [0 for _ in range(n)]
    for _ in range(n)
]
# 행렬 dx, dy 생성
dxs, dys= [0,1,0,-1], [1,0,-1,0]
# 격자 안에 있는지 확인하는 함수 생성
def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

for _ in range(m):
    x, y= tuple(map(int, input().split()))
    x-=1; y-=1
    arr[x][y]=1
    cnt=0
    for i in range(4):
        nx, ny= x+dxs[i], y +dys[i]
        if in_range(nx, ny) and arr[nx][ny]==1:
            cnt+=1
    if cnt==3:
        print(1)
    else:
        print(0)