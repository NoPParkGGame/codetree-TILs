'''
피보나치 수열의 점화식 -> An = An-1 + An-2

'''

N=int(input())

def f(x):
    if x==1 or x==2:
        return 1
    
    return f(x-1) + f(x-2 )

print(f(N))