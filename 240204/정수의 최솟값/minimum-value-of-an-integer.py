def get_min(a, b, c):
    import sys
    min_val=sys.maxsize
    arr=[a, b, c]
    for elem in arr:
        if min_val>elem:
            min_val=elem
    return min_val

a, b, c= tuple(map(int, input().split()))

print(get_min(a, b, c))