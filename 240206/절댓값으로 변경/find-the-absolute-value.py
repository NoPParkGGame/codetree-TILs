n = int(input())

arr= list(map(int, input().split()))

def abs_val(arr):
    for i in range(n):
        if arr[i]<0:
            arr[i]= -arr[i]
    return arr

for elem in abs_val(arr):
    print(elem, end=' ')