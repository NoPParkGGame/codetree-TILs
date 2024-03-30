n= int(input())

x, y= 0, 0
dx, dy= [1, 0, -1, 0], [0, -1, 0, 1]
dir_to_num=['E','S','W','N']
for _ in range(n):
    direct, distance=input().split()    # 이동 방향과, 거리 입력
    distance=int(distance)
    x, y = x+dx[dir_to_num.index(direct)]*distance, y+ dy[dir_to_num.index(direct)]*distance

print(x, y)