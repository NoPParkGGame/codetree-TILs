n=int(input())

arr=[
    [0 for _ in range(n)]
    for _ in range(n)
]
num=1
for j in range(n-1,-1,-1):
    if (j%2==0 and n%2==0) or (j%2!=0 and n%2!=0) :
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
n이 4일 때
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

4   4
3   4
2   4
1   4
0   4





'''