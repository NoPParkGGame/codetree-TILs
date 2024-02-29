n=int(input())

segment=[
    tuple(map(int, input().split()))
    for _ in range(n)
]

arr=[0]*201 

for a, b in segment:
    for i in range(a, b):
        arr[i]+=1

print(max(arr))