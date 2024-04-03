arr=list(input())

dir_num=3
dxs, dys= [1,0,-1,0], [0,-1,0,1]
x, y=0, 0

ans=-1
for cur_time, elem in enumerate(arr, start=1):
    if x==0 and y==0 and cur_time!=1:
        break
    if elem=='R':
        dir_num= (dir_num+1)%4
    elif elem=='L':
        dir_num= (dir_num+3)%4
    else:
        x, y= x+dxs[dir_num], y+dys[dir_num]
    ans=cur_time

print(ans)