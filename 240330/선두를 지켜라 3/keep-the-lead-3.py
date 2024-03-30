n, m= tuple(map(int, input().split()))

move_A=[0]; move_B=[0]

def make_move(move_who, num):
    for _ in range(num):
        vel, time= tuple(map(int, input().split()))
        for _ in range(time):
            move_who.append(vel+move_who[-1])

make_move(move_A, n); make_move(move_B, m)

leader=''; ans=1

for i in range(1, len(move_A)):
    if move_A[i]>move_B[i]:
        if leader=='B' or leader=='All':
            ans+=1
        leader='A'
    elif move_A[i]<move_B[i]:
        if leader=='A' or leader=='All':
            ans+=1
        leader='B'
    else:
        if leader=='A' or leader=='B':
            ans+=1
        leader='All'
print(ans)