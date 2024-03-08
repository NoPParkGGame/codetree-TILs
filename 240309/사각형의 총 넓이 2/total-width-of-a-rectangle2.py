n=int(input())

given_arr=[
    list(map(int, input().split()))
    for _ in range(n)
]

arr_x=[0]*201
arr_y=[0]*201

for x1, y1, x2, y2 in given_arr:
    x1+=100; y1+=100; x2+=100; y2+=100;

    for i in range(x1, x2):
        arr_x[i]+=1
    for i in range(y1, y2):
        arr_y[i]+=1

while 0 in arr_x:
    arr_x.remove(0)
while 0 in arr_y:
    arr_y.remove(0)

whole_w=len(arr_x)*len(arr_y)

cnt_x=0
cnt_y=0
for elem in arr_x:
    if elem!=1:
        cnt_x+=1
for elem in arr_y:
    if elem!=1:
        cnt_y+=1
overlap_w=cnt_x*cnt_y

print(whole_w-overlap_w)