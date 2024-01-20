n=int(input())

for i in range(n):
    for _ in range(i):
        print(' ',end=' ')
    for j in range(n-i,0,-1):
        print(j,end=' ')
    print()

'''

3 2 1
  2 1
    1

i   j   ''
0   3   0
1   2   1
2   1   2


'''