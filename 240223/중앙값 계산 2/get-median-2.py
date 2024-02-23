n=int(input())

arr=list(map(int, input().split()))
sorted_arr=sorted(arr)

for i in range(len(arr)):
    if n<=2:
        print(arr[0])
        break
    elif i%2==0:
        print(sorted_arr[(i+1)//2], end=' ')




'''
y=(x+1)//2
'''