a=input()
b=input()

arr=[]

arr.append(a.split())
arr.append(b.split())

for word in arr:
    for elem in word:
        print(elem, end='')