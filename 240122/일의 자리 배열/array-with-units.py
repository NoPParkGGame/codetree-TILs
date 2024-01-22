arr=list(map(int,input().split()))

for i in range(3,11):
    if arr[-1]+arr[-2]<10:
        arr.append(arr[-1]+arr[-2])
    else:
        arr.append(arr[-1]+arr[-2]-10)

for elem in arr:
    print(elem,end=' ')