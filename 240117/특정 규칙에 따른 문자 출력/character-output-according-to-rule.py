n=int(input())

for i in range(n):
    for j in range(n-(i+1)):
        print(' ',end=' ')
    for k in range(i+1):
        print('@',end=' ')
    print()
for i in range(n-2,-1,-1):
    for k in range(i+1):
        print('@',end=' ')
    print()


'''    
n   i   ''  @
3   0   2   1
3   1   1   2
3   2   0   3

n+1 - 2i
4 - 0
4 - 2
4 - 4
'''