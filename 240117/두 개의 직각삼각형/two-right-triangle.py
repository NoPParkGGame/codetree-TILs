n=int(input())

for i in range(n):
    for j in range(n-i):
        print('*',end='')
    for k in range(i*2):
        print(' ',end='')
    for l in range(n-i):
        print('*',end='')
    print()


'''
n   i   *   ''  *
3   0   3   0   3
3   1   2   2   2
3   2   1   4   1
'''