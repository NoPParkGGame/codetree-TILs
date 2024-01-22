dice_arr=list(map(int,input().split()))

cnt_arr=[0]*7

for elem in dice_arr:
    cnt_arr[elem]+=1

for i in range(1,7):
    print(f'{i} - {cnt_arr[i]}')