n= int(input())

given_input=[
    input().split()
    for _ in range(n)
]

arr=[0]*(200*n+1)
x0= 100*n
pre_x= x0

def dir_R(input_x):
    global pre_x
    for i in range(pre_x, pre_x + input_x):
        if arr[i]==0:
            arr[i]=[]
            arr[i].append('B')
        else:
            arr[i].append('B')
    pre_x = pre_x + input_x - 1

def dir_L(input_x):
    global pre_x
    for i in range(pre_x - input_x+1, pre_x+1):
        if arr[i]==0:
            arr[i]=[]
            arr[i].append('W')
        else:
            arr[i].append('W')
    pre_x= pre_x - input_x+1

for x, direct in given_input:
    x= int(x)
    if direct=='R':
        dir_R(x)
    else:
        dir_L(x)
    
cnt_w=0
cnt_b=0
cnt_g=0

def w_or_b(elem):
    cnt_elem_w=0
    cnt_elem_b=0
    for elem2 in elem:
        if elem2=='W':
            cnt_elem_w+=1
        elif elem2=='B':
            cnt_elem_b+=1
    if cnt_elem_b>=2 and cnt_elem_w>=2:
        return 'gray'
    return 

for elem in arr:
    if elem!=0:
        if len(elem)>=4:
            if w_or_b(elem)=='gray':
                cnt_g+=1
            else:
                if elem[-1]=='W':
                    cnt_w+=1
                elif elem[-1]=='B':
                    cnt_b+=1       
        if len(elem)<4:
            if elem[-1]=='W':
                cnt_w+=1
            elif elem[-1]=='B':
                cnt_b+=1
print(cnt_w, cnt_b, cnt_g)