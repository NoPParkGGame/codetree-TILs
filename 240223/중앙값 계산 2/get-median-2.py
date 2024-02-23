n=int(input())

arr=list(map(int, input().split()))
new_arr=[]

for i in range(n):
    new_arr.append(arr[i])
    if i%2==0:
        new_arr.sort()
        print(new_arr[i//2], end=' ')