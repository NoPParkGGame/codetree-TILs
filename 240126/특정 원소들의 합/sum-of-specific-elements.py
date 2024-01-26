arr=[
    list(map(int,input().split()))
    for _ in range(4)
]
sum_val=0
for i in range(4):
    for j in range(i+1):
        sum_val+=arr[i][j]

print(sum_val)

'''
i   j
0   0

1   0
1   1

2   0
2   1
2   2

3   0  
3   1
3   2
3   3
'''