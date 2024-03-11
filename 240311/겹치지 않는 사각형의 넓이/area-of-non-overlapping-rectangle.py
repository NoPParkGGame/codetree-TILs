given_arr=[
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split()))
]
offset=1000
max_axis=2001

arr_axis=[
    [0 for _ in range(max_axis)]
    for _ in range(max_axis)
]
num_square=0

for square in given_arr:
    num_square+=1; x1,y1,x2,y2=square
    x1+=offset; y1+=offset;
    x2+=offset; y2+=offset;  
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr_axis[i][j]=num_square
    
extent=0
for i in range(max_axis):
    for j in range(max_axis):
        if arr_axis[i][j]!=0 and arr_axis[i][j]!=3:
            extent+=1
print(extent)