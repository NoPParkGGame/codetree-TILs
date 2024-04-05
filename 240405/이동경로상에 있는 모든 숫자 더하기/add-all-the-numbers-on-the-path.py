n, order= tuple(map(int, input().split()))

arr_order=list(input())

arr=[
    list(map(int, input().split()))
    for _ in range(n)
]

dir_num=3
dxs, dys= [0,1,0,-1], [1,0,-1,0]
x, y= n//2, n//2
ans=arr[x][y]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

for elem in arr_order:
    if elem=='R':
        dir_num= (dir_num+1)%4  # turn right
    elif elem=='L':
        dir_num= (dir_num+3)%4  # turn left
    else:   # elem=='F'
        nx, ny= x+ dxs[dir_num], y+ dys[dir_num]
        if not in_range(nx, ny):
            pass
        else:
            x, y= x+ dxs[dir_num], y+ dys[dir_num]
            ans+=arr[x][y]
print(ans)