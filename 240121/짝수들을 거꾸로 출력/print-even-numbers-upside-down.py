n=int(input())

arr=list(map(int,input().split()))

for elem in arr[::-1]:
    if elem%2==0:
        print(elem,end=' ')