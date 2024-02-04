def get_add(a, b):
    return a+b
def get_minus(a, b):
    return max(a, b)- min(a, b)
def get_div(a, b):
    return max(a, b)/min(a, b)
def get_mult(a, b):
    return a*b

a, c, b = tuple(input().split())
a, b= int(a), int(b)

if c=='+':
    print(a, c, b,'=', get_add(a, b))
elif c=='-':
    print(a, c, b,'=', get_minus(a, b))
elif c=='/':
    print(a, c, b,'=', get_div(a, b))
elif c=='*':
    print(a, c, b,'=', get_mult(a, b))