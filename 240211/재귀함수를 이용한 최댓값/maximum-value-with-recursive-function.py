import sys
n = int(input())

arr= list(map(int, input().split()))
arr.append(-sys.maxsize)

def f(n):
    if n==1:
        return arr[0] if arr[0]>arr[1] else arr[1]
    
    cached=int(f(n-1))

    if cached > arr[n]:
        return cached

    return arr[n]

print(f(n))