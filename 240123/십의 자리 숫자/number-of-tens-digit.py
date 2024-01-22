arr=list(map(int,input().split()))
new_arr=[elem//10 for elem in arr]

cnt_arr=[]
for i in range(1,10):
    cnt_arr.append(i)
res_arr=[]
for i in range(len(cnt_arr)):
    cnt=0
    for j in range(len(new_arr)):
        if cnt_arr[i]==new_arr[j]:
            cnt+=1
    print(f'{cnt_arr[i]} - {cnt}')