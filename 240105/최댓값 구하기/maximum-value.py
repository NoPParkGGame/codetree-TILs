num=input().split()
a,b,c=int(num[0]),int(num[1]),int(num[2])

if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)