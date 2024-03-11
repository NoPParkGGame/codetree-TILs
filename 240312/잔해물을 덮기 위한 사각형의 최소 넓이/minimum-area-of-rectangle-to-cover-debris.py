n=2
given_arr=[
    tuple(map(int, input().split()))
    for _ in range(n)
]
offset=1000
max_axis=2001

arr_axis=[
    [0 for _ in range(max_axis)]
    for _ in range(max_axis)
]

for idx, (x1,y1,x2,y2) in enumerate(given_arr, start=1):
    x1+=offset; x2+=offset
    y1+=offset; y2+=offset
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr_axis[i][j]=idx

arr_x=[]
arr_y=[]

for i in range(max_axis):
    for j in range(max_axis):
        if arr_axis[i][j]==1:
            arr_x.append(i)
            arr_y.append(j)

width=max(arr_x) - min(arr_x) + 1
height=max(arr_y) - min(arr_y) + 1

print(width * height)