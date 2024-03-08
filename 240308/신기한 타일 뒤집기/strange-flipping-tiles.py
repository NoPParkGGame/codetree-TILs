n= int(input())
given_dir=[
    input().split()
    for _ in range(n)
]
arr=[0] *(200*n+1)  # 전체 타일 선언
x0=100*n    # 시작 타일 선언
cnt_w, cnt_b= 0, 0  # 흰, 검 갯수 초기화
pre_x=x0    # 처음 시작하는 pre_x 타일은 x0

def dir_R(given_x):
    global pre_x
    for i in range(pre_x, pre_x+given_x):
        if arr[i]==0:
            arr[i]=[]
            arr[i].append('B')
        else:
            arr[i].append('B')
    pre_x= pre_x+given_x-1

def dir_L(given_x):
    global pre_x
    for i in range(pre_x-given_x+1 ,pre_x+1):
        if arr[i]==0:
            arr[i]=[]
            arr[i].append('W')
        else:
            arr[i].append('W')
    pre_x=pre_x-given_x+1


for x, direct in given_dir:
    x=int(x)
    if direct=='R':
        dir_R(x)
    else:
        dir_L(x)

for elem in arr:
    if elem!=0:
        if elem[-1]=='W':
            cnt_w+=1
        elif elem[-1]=='B':
            cnt_b+=1

print(cnt_w, cnt_b)



'''
  2 2 2
      p
1 1 1 1
0 0 0 0 0 0 0 0 
0 1 2 3 4

4 R
3 L




'''