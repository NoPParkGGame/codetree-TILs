n=int(input())

for i in range(n):
    for j in range(n):
        if i==0:
            print('*',end=' ')
        elif j%2==1 and i<=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


'''
i/j
  0 1 2 3 4 5
0 * * * * * *
1   *   *   *
2       *   *
3       *   *
4           *
5           *

i   j



'''