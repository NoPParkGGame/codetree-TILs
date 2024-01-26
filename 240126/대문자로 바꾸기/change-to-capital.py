n=5

arr_dim_2=[
    input().split()
    for _ in range(n)
]

for elem in arr_dim_2:
    for elem2 in elem:
        print(chr(ord(elem2)-32),end=' ')
    print()

'''
A=65
a=97
-32

'''