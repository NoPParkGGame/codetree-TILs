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
    for i in range(4):
        if int(a[i]) + int(b[i]) + int(c[i])>=10:
            return True
    return False

def sum_all(a, b, c):

    return int(a)+int(b)+int(c)

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            if not is_carry(arr[i],arr[j],arr[k]):
                total_val = sum_all(arr[i], arr[j], arr[k])
                max_val= max(max_val, total_val)
                ans=max_val

print(ans)