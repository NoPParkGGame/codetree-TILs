arr=list(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y =0, 0
dir_num=3

for elem in arr:
    if elem=='R':
        dir_num= (dir_num+1)%4
    elif elem=='L':
        dir_num= (dir_num -1 +4)%4
    elif elem=='F':
        x, y= x+ dx[dir_num], y+ dy[dir_num]
print(x, y)