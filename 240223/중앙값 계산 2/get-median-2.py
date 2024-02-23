n=int(input())

arr=list(map(int, input().split()))
new_arr=[]

for i in range(len(arr)):
    new_arr.append(arr[i])
    if i%2==0:
        new_arr.sort()
        print(new_arr[(i+1)//2], end=' ')