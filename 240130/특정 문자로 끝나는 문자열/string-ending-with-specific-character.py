arr=[
    input()
    for _ in range(10)
]
alph=input()

num=0
for elem in arr:
    if elem[-1]==alph:
        print(elem)
        num+=1
if num==0:
    print)'None'