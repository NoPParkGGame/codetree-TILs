arr=[
    input()
    for _ in range(10)
]
alph=input()

for elem in arr:
    if elem[-1]==alph:
        print(elem)