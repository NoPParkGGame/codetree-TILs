n= int(input())

arr=[
    input().split()
    for _ in range(n)
]
# 방향을 숫자로 바꿔주는 딕셔너리 생성
mapper={
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}
# 초기 좌표 설정
x,y= 0, 0
# dx, dy 생성
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
cnt=0
indicator=False
for direct, dist in arr:
    dist= int(dist)
    dir_num=mapper[direct]  # 방향 지정

    for i in range(dist):
        x, y= x+ dxs[dir_num], y+ dys[dir_num] # 방향으로 dist 만큼 이동
        cnt+=1
        if x==0 and y==0:
            indicator=True
            print(cnt)
            break

    if indicator:
        break
if not indicator:
    print(-1)