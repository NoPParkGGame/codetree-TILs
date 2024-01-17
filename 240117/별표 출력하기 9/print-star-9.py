n=int(input())

for i in range(n-1,-1,-1):
    for j in range(i*2):
        print(' ',end='')
    for j in range((n-i-1)*2+1):
        print('*',end=' ')
    print()

'''
n   i   I    ''  *
3   0   2    4   1   
3   1   1    2   3
3   2   0    0   5


'''