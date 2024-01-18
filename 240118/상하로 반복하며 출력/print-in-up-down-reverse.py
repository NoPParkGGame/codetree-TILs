n=int(input())


for i in range(n):
    for j in range(n):
        if j%2==0:
            print(i+1,end='')
        else:
            print(n-i,end='')
    print()

'''
   01234

0 /15151
1 /24242
2 /33333
3 /42424
4 /51515

'''