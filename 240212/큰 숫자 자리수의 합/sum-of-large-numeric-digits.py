arr=list(map(int,input().split()))

def f(n):
    if n==0:
        return arr[0]
    
    return f(n-1) * arr[n]

def g(n):
    if n<10:
        return n
    return g(n//10) + n%10



print(g(f(len(arr)-1)))


'''


44253432 + 44253432 % 10
f(n//10) + n%10

'''