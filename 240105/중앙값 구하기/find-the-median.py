nums=input().split()
a, b, c=int(nums[0]), int(nums[1]), int(nums[2])

if a>b:
    if b>c:
        print(b)
    elif a>c: # a>b and c>b -> a>c>b
        print(c)
    else:
        print(a)
else: #a<b
    if b<c: #a<b<C
        print(b)
    elif a>c: #b>c and b>a -> b>a>c
        print(a)
    else:
        print(c)