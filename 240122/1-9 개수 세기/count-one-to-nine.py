n=int(input())
arr=list(map(int,input().split()))
cnt_arr=[0]*10
for elem in arr:
    cnt_arr[elem]+=1

for elem in cnt_arr[1::]:
    print(elem)