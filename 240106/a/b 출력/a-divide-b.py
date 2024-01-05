arr=input().split()

a, b = int(arr[0]),int(arr[1]) # a=3, b=5

print(f'{a//b}.',end='')

a%=b

for _ in range(20):
    a*=10
    print(a//b,end='')
    a%=b