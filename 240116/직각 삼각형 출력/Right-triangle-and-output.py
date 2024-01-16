n=int(input())  #n=5

for i in range(n): # i는 0 , 1 , 2 , 3 , 4
    for j in range(i+1,n+1,2):    #j는 1, 3, 5
        print('*',end='')
    print()