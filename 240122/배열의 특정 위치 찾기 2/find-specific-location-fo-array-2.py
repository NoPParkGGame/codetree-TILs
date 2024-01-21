arr=list(map(int,input().split()))

even_sum=0
odd_sum=0
for elem in arr[::2]:
    even_sum+=elem

for elem in arr[1::2]:
    odd_sum+=elem
def minus(a,b):
    if a>=b:
        return a-b
    else:
        return b-a

print(minus(even_sum,odd_sum))