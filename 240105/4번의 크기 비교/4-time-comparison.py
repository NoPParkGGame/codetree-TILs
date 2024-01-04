a=int(input()) #a= 3

arr=input().split() #arr=[1, 2, 3, 4]

n=0
while n<len(arr):
    arr[n]=int(arr[n])
    n+=1
b,c,d,e=arr[0],arr[1],arr[2],arr[3]
if a>b:
    print(1)
else:
    print(0)
if a>c:
    print(1)
else:
    print(0)
if a>d:
    print(1)
else:
    print(0)
if a>e:
    print(1)
else:
    print(0)