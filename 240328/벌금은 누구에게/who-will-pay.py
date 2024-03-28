n, m, k= tuple(map(int, input().split()))

students=[
    k
    for i in range(n)
]

minus=[
    int(input())
    for _ in range(m)
]

for num in minus:
    students[num-1]-=1
ans=-1

for i in range(n):
    if students[i]==0:
        ans=i+1
        break
print(ans)