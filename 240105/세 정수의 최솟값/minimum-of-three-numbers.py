N=input().split()

a, b, c=int(N[0]), int(N[1]), int(N[2])

if a<=b and a<=c:
    print(a)
elif b<=c and b<=a:
    print(b)
elif c<=a and c<=b:
    print(c)