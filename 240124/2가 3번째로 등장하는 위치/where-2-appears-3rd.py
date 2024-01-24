n=int(input())

arr=list(map(int,input().split()))

obj=2
cnt_2=0
cnt_arr=1
for i in range(n):
    if arr[i]==obj:
        cnt_2+=1
        if cnt_2==3:
            print(cnt_arr)
            break
    cnt_arr+=1