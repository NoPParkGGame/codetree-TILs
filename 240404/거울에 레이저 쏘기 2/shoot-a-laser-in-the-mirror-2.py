n= int(input())
# 빈 리스트 생성
# 거울 배열 정보 입력
mirror=[
    list(input())
    for _ in range(n)
]
# dx, dy 리스트 생성
dxs, dys= [0,1,0,-1], [1,0,-1,0]
# 레이저 쏘는 위치 입력
laser=int(input())
# 같은 반사각을 지닌 시작 숫자들 끼리 리스트 생성
length=[]  # 수직 리스트 생성
for i in range(1, n+1):
    length.append(i)
for i in range(3*n-(n-1), 3*n +1):
    length.append(i)

width=[]    # 수평 리스트 생성
for i in range(1, 4*n +1):
    if i not in length:
        width.append(i)
# 현재 바라보는 방향을 0으로 가정하고 시작
dir_num=0

# 숫자를 arr 내의 좌표로 치환해주는 함수 생성
def make_axis(laser_start):
    global dir_num  # 방향 변수 전언변수로 선언
    if laser_start in length:   # 수직 리스트에 들어간다면, 방향 판단 변수는 그대로 수직
        if length.index(laser_start)>=len(length)//2:   # 만약 시작점이 아래에서 위로 시작한다면,
            dir_num=3   # 방향 변수는 북쪽을 향함
            laser_start= (1+3*n)- laser_start   # 9는 1로, 8은 2로, 7은 3으로 바꿔주는 수식
            (x, y)= (n-1, laser_start-1) 
            return x, y
        else:   # 시작점이 위에서 아래로 시작한다면
            dir_num=1   # 방향변수는 남쪽을 향함
            (x,y)= (0, laser_start-1)   
            return x, y
    if laser_start in width:    # 수평 리스트에 들어간다면
        if width.index(laser_start)>=len(width)//2: #만약 시작점이 왼쪽에서 오른쪽으로 시작한다면,
            dir_num=0 # 방향 변수는 오른쪽을 향함
            laser_start= (n*5+1) - laser_start  # 12는 4로, 11은 5로, 10은 6으로 바꿔주는 수식
            (x, y)= (laser_start-(n+1), 0)
            return x, y
        else:   # 시작점이 오른쪽에서 왼쪽으로 시작한다면
            dir_num= 2  # 방향 변수는 왼쪽을 향함
            (x, y)= (laser_start-(n+1), n-1)
            return x, y
# x, y의 초기 좌표를 설정해줌
x, y= make_axis(laser)
# 좌표 내에 있는지 확인하는 함수 생성
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n
ans=1
# 레이저가 좌표 밖으로 나갈 때 까지 무한 반복
while True:
    if dir_num==1 or dir_num==3:    # 뱡향이 수직일 때, 
        if mirror[x][y]=='\\':  # \ 모양의 거울과 만난다면, 
            dir_num= (dir_num+3)%4  # 방향은 왼쪽으로 꺾임
        else:   # / 모양의 거울과 만난다면
            dir_num= (dir_num+1)%4  #방향은 오른쪽으로 꺾임

    elif dir_num==0 or dir_num==2:   # 방향이 수평일 때,
        if mirror[x][y]=='\\': # \모양의 거울과 만난다면
            dir_num= (dir_num+1)%4  #방향은 오른쪽으로 꺾임
        else:   # / 모양의 거울과 만난다면
            dir_num= (dir_num+3)%4  # 방향은 왼쪽으로 꺾임
    nx, ny= x+ dxs[dir_num], y+ dys[dir_num]    # nx, ny 먼저 가상 이동
    if not in_range(nx, ny):    # 만약 좌표 밖으로 벗어난다면
        break       #반복문 종료
    x, y= x+ dxs[dir_num], y+ dys[dir_num]
    ans+=1

print(ans)


'''
    수직
    1  2  3  4      range(1, n)
16              5
15              6   수평
14              7
13              8
    12 11 10 9      range(3n, 3n-(n-1), -1)

range(1,n) 그리고 range(3n-(n-1), 3n) [수직]은 같은 입사각 반사각을 가짐.
: / 오른쪽, \ 왼쪽


range(n+1, 2n) 그리고 range(4n-(n-1) , 4n) [수평]은 같은 반사각을 가짐
: / 왼쪽, \ 오른쪽


   3
2     0
   1
'''