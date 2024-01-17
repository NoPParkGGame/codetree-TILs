n=int(input())

for i in range(n):
    for _ in range(n-(i+1)):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()
for i in range(n-2,-1,-1):
    for _ in range(n-(i+1)):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()    
'''
n   i   ''  *
3   0   2   1
3   1   1   3
3   2   0   5

'''