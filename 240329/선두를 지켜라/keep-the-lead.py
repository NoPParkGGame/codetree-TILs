n,m=tuple(map(int, input().split()))
dist_A=[0]
dist_B=[0]

def make_dist(w_num, dist_who):
    for i in range(w_num):
        vel, time= tuple(map(int, input().split()))
        for i in range(time):
            dist_who.append(vel+dist_who[-1])
            
make_dist(n, dist_A)
make_dist(m, dist_B)

arr_first=[
    dist_A[i]-dist_B[i]
    for i in range(len(dist_A))
]
while 0 in arr_first:
    arr_first.remove(0)

ans=0

for i in range(1, len(arr_first)):
    if arr_first[i]*arr_first[i-1]<0:
        ans+=1
print(ans)