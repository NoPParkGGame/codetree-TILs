n, m= tuple(map(int, input().split()))

# n * m 형태의 0으로 된 리스트 생성
arr=[
    [0]*m
    for _ in range(n)
]
# 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3:위쪽
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
# 오른쪽 방향을 보고 시작
dir_num=0
# 초기값 지정
x, y=0, 0
# 범위 확인 함수 생성
def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m
arr[x][y]=1
# n*m 번 진행할 것이므로
for i in range(2, n*m +1):
    nx, ny = x+ dxs[dir_num], y + dys[dir_num]  # 가상 좌표 이동

    if not in_range(nx, ny) or arr[nx][ny]!=0:  # 범위에서 벗어나거나, 이미 간 곳이라면
        dir_num= (dir_num+1)%4  # 오른쪽으로 방향 회전
    
    x, y= x+ dxs[dir_num], y + dys[dir_num] # 실제 좌표 이동
    arr[x][y]=i

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()