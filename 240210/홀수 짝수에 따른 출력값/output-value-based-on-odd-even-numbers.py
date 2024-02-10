N= int(input())

def f(n):
    if n %2 == 0:
        if n == 2:
            return n
        return n + f(n-2)
    else:
        if n == 1:
            return n
        return n + f(n-2)
    
print(f(N))