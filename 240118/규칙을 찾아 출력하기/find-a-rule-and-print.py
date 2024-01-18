n=int(input())


for i in range(n):
    for j in range(n):
        if n-1>j>=i>0:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()

'''
n=5

  0 1 2 3 4
0 * * * * *
1 *       *
2 * *     *
3 * * *   *
4 * * * * *

i   j
1   1
1   2
1   3
2   2
2   3
3   3


'''