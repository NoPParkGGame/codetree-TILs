n, m = tuple(map(int, input().split()))

def swap(a, b):
    a, b = b, a
    return (a, b) 

for elem in swap(n, m):
    print(elem, end=' ')