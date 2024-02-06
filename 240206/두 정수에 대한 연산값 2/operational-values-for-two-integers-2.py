a, b = tuple(map(int, input().split()))

def trans(a, b):
    if a > b:
        b+=10
        a*=2
    else:
        a+=10
        b*=2
    return a, b

a, b = trans(a, b)

print(a, b)