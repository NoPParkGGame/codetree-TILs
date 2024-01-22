n=int(input())
arr=[1]
arr.append(n)

for elem in arr:
    arr.append(arr[-1]+arr[-2])
    if arr[-1]+arr[-2]>100:
        arr.append(arr[-1]+arr[-2])
        break
for elem in arr:
    print(elem,end=' ')