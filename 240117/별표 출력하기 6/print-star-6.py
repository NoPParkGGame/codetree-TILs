n=int(input())

for i in range(n):
    for _ in range(2*i):
        print(' ',end='')
    for j in range((n-(i+1))*2+1):
        print('*',end=' ')
    print()
for i in range(n-2,-1,-1):
    for _ in range(2*i):
        print(' ',end='')
    for j in range((n-(i+1))*2+1):
        print('*',end=' ')
    print() 
'''
n   i   ''  *   
3   0   0   5   2
3   1   2   3   1
3   2   4   1   0
'''