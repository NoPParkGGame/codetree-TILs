n, k = tuple(map(int, input().split()))

arr=[0]*(n+1)

for _ in range(k):
    
    a, b= tuple(map(int, input().split()))

    for i in range(a, b+1):
        arr[i]+=1

print(max(arr))