n, m= tuple(map(int, input().split()))

move_A=[
    input().split()
    for _ in range(n)
]   #A값 입력
move_B=[
    input().split()
    for _ in range(m)
]   #값 입력
arr_A=[0]*1001
arr_B=[0]*1001


def start(move_who, arr_who):   #이동경과를 기록하는 함수 작성
    pre_x=1
    for drt, num in move_who:
        num=int(num)
        if drt=='R':
            for i in range(pre_x, pre_x+num):
                arr_who[i]=arr_who[i-1]+1
        
        if drt=='L':
            for i in range(pre_x, pre_x+num):
                arr_who[i]=arr_who[i-1]-1
        pre_x=i+1

start(move_A, arr_A)
start(move_B, arr_B)    #각 함수 적용

meet=False
for i in range(1, len(arr_A)):
    if arr_A[i]==arr_B[i] and (abs(arr_A[i-1])-abs(arr_A[i]))<2:
        print(i)
        meet=True
        break

if meet==False:
    print(-1)