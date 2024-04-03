n= int(input())
# 빈 리스트 생성
arr=[
    [0] *n
    for _ in range(n)
]
# 거울 배열 정보 입력
mirror=[
    list(input())
    for _ in range(n)
]
# 레이저 쏘는 위치 입력
laser=int(input())
# 같은 반사각을 지닌 시작 숫자들 끼리 리스트 생성
length=[]  # 수직
for i in range(1, n+1):
    length.append(i)
for i in range(3*n-(n-1), 3*n +1):
    length.append(i)

width=[]    # 수평
for i in range(1, 4*n +1):
    if i not in length:
        width.append(i)
# 숫자를 arr 내의 좌표로 치환해주는 함수 생성
def make_axis(laser_start):
    if laser_start in length:   # 수직 리스트에 들어간다면,
        if length.index(laser_start)>=len(length)//2:   # 만약 시작점이 아래에서 시작한다면,
            laser_start= (1+3*n)- laser_start   # 9는 1로, 8은 2로, 7은 3으로 바꿔주는 수식
            (x, y)= (n-1, laser_start-1) 
            return x, y
        else:
            (x,y)= (0, laser_start-1)   # 그렇지 않다면 바로 변환
            return x, y
    if laser_start in width:    # 수평 리스트에 들어간다면
        if width.index(laser_start)>=len(width)//2: #만약 시작점이 왼쪽에서 시작한다면,
            laser_start= (n*5+1) - laser_start




print(make_axis(laser))



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
'''