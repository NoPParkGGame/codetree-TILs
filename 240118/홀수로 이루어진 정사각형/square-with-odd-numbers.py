n=int(input())
for i in range(n):
    for j in range(n):
        j+=i
        print((j+1)*2+9,end=' ')
        
    print()



'''
   1  2  3  4

1 /11 13 15 17
2 /13 15 17 19
3 /15 17 19 21
4 /17 19 21 23

'''