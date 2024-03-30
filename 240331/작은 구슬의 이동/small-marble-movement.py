num, time= tuple(map(int, input().split()))
#n행, 움직이는 시간 입력
row, col, direction = input().split()
#행, 열, 방향 입력
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]   # 0, 1, 2, 3
x, y= int(row), int(col) # 처음 위치 갱신

mapper={
    'U': 2,
    'D': 1,
    'R': 0,
    'L': 3
}   # 각 방향들을 숫자로 전환

def in_range(x, y):
    return 0<x and x<num and 0<y and y<num    # 해당 격자 내에 있는지 확인

cur_time=0
dir_num=mapper[direction]
while cur_time<time:   #현재 시간이 주어진 시간이 될때 까지 계속
    nx, ny= x + dx[dir_num], y+dy[dir_num]  # 먼저 nx, ny가 격자내에 있는지 확인
    
    if not in_range(nx, ny):    # 격자 내에 없다면
        dir_num= 3 - dir_num    # 방향 전환
        cur_time+=1 # 방향 전환 시 1초 소요
    
    x, y = x + dx[dir_num], y+dy[dir_num]
    cur_time+=1 # 이동 후 1초 소요

print(x, y)

'''
  1
3   0
  2

'''