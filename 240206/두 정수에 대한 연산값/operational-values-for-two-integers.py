a, b = tuple(map(int, input().split()))

def trans(a, b):
    if a > b:
        a+=25
        b*=2
    else:
        a*=2
        b+=25
    return a, b

for elem in trans(a, b):
    print(elem, end=' ')