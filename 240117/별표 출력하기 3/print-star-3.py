n=int(input())

for i in range(n-1,-1,-1):
    for j in range((n-(i+1))*2):
        print(' ',end='')

    for _ in range(i*2+1):
        print('*',end=' ')
    print()

'''
    2    0   5
    1    1   3
    0    2   1

n    j    i     i+1     ?
3    0    2     3       0   
3    1    1     2       2
3    2    0     1       4
    '''