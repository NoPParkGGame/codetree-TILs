n, m, k= tuple(map(int, input().split()))

students=[0]+[
    k
    for i in range(n)
]

minus=[
    int(input())
    for _ in range(m)
]

for num in minus:
    students[num]-=1
ans=-1

for i in range(1, n):
    if students[i]==0:
        ans=i
        break
print(ans)