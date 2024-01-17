n=int(input())
even=0
odd=1
for i in range(2*n-1):
    if i%2==0:
        for j in range(n-even):
            print('*',end=' ')
        even+=1
        print()
    else:
    
        for k in range(odd):
            print('*',end=' ')
        odd+=1
        print()
print('* '*n)

'''
n=4         i
* * * *     0   4
*                   1   1
* * *       2   3
* *                 3   2
* *         4   2
* * *               5   3
*           6   1
* * * *             7   4

*
* *
* * *
* * * *

'''