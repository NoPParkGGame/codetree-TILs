arr=input().split()
a,b=int(arr[0]),int(arr[1])


for i in range(1,a+1):
    for j in range(1,b+1):
        print(i*j,end=' ')
    print()

'''
   1 2 3 4 5

1 /1 2 3 4 5
2 /2 4 6 8 10
3 /3 6 9 12 15
4 /4 8 12 16 20


'''