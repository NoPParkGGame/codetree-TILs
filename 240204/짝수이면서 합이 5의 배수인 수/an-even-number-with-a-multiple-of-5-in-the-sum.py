def even_five(N):
    return N%2==0 and ((N%10) + (N//10))%5==0


n=int(input())

if even_five(n):
    print('Yes')
else:
    print('No')

'''

32
3 + 2

32 % 10 = 2
32 // 10 = 3

'''