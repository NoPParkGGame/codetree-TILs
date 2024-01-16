n=int(input())  #n=5

for i in range(n): # i는 0 , 1 , 2 , 3 , 4
    for j in range((i*2)+1):
        print('*',end='')        
    print()

'''
    i=0 j=1
    i=1 j=3
    i=2 j=5

    j=i*2+1
'''