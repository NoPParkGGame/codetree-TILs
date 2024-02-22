n=int(input())
arr=[]
for _ in range(n):
    arr.append(input())
arr_sorted=sorted(arr)

for elem in arr_sorted:
    print(elem)