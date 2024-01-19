n=int(input())
cnt=1
for i in range(n):
    if i%2==0:
        for j in range(n):
            print(cnt,end=' ')
            cnt+=1
    else:
        for j in range(n-1,-1,-1):
            print(j+cnt,end=' ')
            
        cnt+=1*n
    print()

'''
i/j
   0 1 2 3

0 /1 2 3 4
1 /8 7 6 5
2 /9 10 11 12
3 /16 15 14 13

'''

''