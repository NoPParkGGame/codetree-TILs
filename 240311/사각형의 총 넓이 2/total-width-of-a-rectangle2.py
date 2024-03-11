n=int(input())

given_input=[
    list(map(int, input().split()))
    for _ in range(n)
]

arr=[
    [0 for _ in range(201)]
    for _ in range(201)
] 

offset=100

for x1, y1, x2, y2 in given_input:
    x1+=offset; y1+=offset; 
    x2+=offset; y2+=offset
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j]+=1
extent=0

for i in range(201):
    for j in range(201):
        if arr[i][j]!=0:
            extent+=1

print(extent)

'''

(0, 1)  ->  (100, 101) 
(4, 5)  ->  (104, 105)  

extent = 16

'''