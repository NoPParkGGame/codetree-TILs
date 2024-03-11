length=8

n= int(input())

offset=100
max_axis=201

arr_axis=[
    [0 for _ in range(max_axis)]
    for _ in range(max_axis)
]

given_arr=[
    tuple(map(int, input().split()))
    for _ in range(n)
]

for x1,y1 in given_arr:
    x1+=offset; y1+=offset
    x2=x1+length; y2=y1+length
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr_axis[i][j]=1
extent=0

for row in arr_axis:
    for elem in row:
        if elem==1:
            extent+=1

print(extent)