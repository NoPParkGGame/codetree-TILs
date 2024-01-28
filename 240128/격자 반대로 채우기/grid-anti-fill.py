n=int(input())

arr=[
    [0 for _ in range(n)]
    for _ in range(n)
]
num=1
for j in range(n-1,-1,-1):
    if j%2==0:
        for i in range(n):
            arr[i][j]=num
            num+=1
    else:
        for i in range(n-1,-1,-1):
            arr[i][j]=num
            num+=1

for row in arr:
    for elem in row:
        print(elem,end=' ')
    print()


'''
3   3
2   3
1   3
0   3

0   2  
1   2
2   2
3   2

3   1
2   1
1   1
0   1

0   0
1   0
2   0
3   0




'''