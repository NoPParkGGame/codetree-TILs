n=int(input())

given_axis=[
    tuple(map(int, input().split()))
    for _ in range(n)
]

offset=100
max_axis=201

arr_axis=[
    [0 for _ in range(max_axis)]
    for _ in range(max_axis)
]

for idx, (x1,y1,x2,y2) in enumerate(given_axis, start=1):
    x1+=offset; y1+=offset; x2+=offset; y2+=offset
    for i in range(x1,x2):
        for j in range(y1,y2):
            if idx%2==1:
                arr_axis[i][j]='R'
            else:
                arr_axis[i][j]='B'

extent=0
for row in arr_axis:
    for elem in row:
        if elem=='B':
            extent+=1
print(extent)