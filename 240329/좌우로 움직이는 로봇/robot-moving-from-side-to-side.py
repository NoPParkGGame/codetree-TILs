n, m =tuple(map(int, input().split()))

move_A=[0]
move_B=[0]
def distance(move_who, num):
    cur=0
    for _ in range(num):
        dist, drt=input().split()
        dist=int(dist)
        for _ in range(dist):
            if drt=='R':
                cur+=1
                move_who.append(cur)
            else:
                cur-=1
                move_who.append(cur)
distance(move_A, n)
distance(move_B, m)

ans=0
total_time=max(len(move_A), len(move_B))    # A 와 B 의 총 이동 시간이 다른 경우도 계산해줘야 함.

if total_time==len(move_A): # 만약 B가 먼저 멈췄다면, 마지막 위치를 A가 추가로 움직이는 만큼 갱신해줘야함.
    while len(move_B)<total_time:
        move_B.append(move_B[-1])

elif total_time==len(move_B):   # 그 반대의 경우도 갱신
    while len(move_A)<total_time:
        move_A.append(move_A[-1])

for i in range(1, total_time):
    if move_A[i]==move_B[i] and move_A[i-1] != move_B[i-1]:
        ans+=1
print(ans)