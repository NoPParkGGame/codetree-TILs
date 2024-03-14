n=int(input())

arr=[
    int(input())
    for _ in range(n)
]
arr=arr+['a']
arr_cnt=[]

cnt=1
for i in range(1, n+1):
    if arr[i] == arr[i-1]:
        cnt+=1
    else:
        arr_cnt.append(cnt)
        cnt=1

print(max(arr_cnt))