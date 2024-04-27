import sys
n= int(input())

max_val= -sys.maxsize
ans=-1
arr=[
    input()
    for _ in range(n)
]

for i in range(n):
    while len(arr[i])<4:
        arr[i]= '0' + arr[i]

def is_carry(a, b, c):
    if int(a[0]) + int(b[0]) + int(c[0])>10:
        return True

    if int(a[1]) + int(b[1]) + int(c[1])>10:
        return True

    if int(a[2]) + int(b[2]) + int(c[2])>10:
        return True

    if int(a[3]) + int(b[3]) + int(c[3])>10:
        return True

    return False

def sum_all(a, b, c):
    a=int(a); b=int(b); c=int(c)
    return a+b+c

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            if not is_carry(arr[i],arr[j],arr[k]):
                total_val = sum_all(arr[i], arr[j], arr[k])

                max_val= max(max_val, total_val)
                ans=max_val

print(ans)