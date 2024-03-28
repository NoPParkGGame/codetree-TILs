n, m, k= tuple(map(int, input().split()))

students=[0]+[
    k
    for i in range(n)
]
ans=-1
for _ in range(m):
    minus=int(input())
    students[minus]-=1
    if students[minus]==0:
        ans=minus
        break
print(ans)