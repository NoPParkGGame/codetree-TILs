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
print(move_A)
print(move_B)