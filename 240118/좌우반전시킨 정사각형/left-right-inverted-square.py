n=int(input())
cnt=1
for i in range(1,n+1):
    cnt=0
    cnt+=i
    for j in range(1,n+1):
        if j==1:
            print(4*i,end=' ')
        else:
            print(4*i-cnt,end=' ')
            cnt+=i

    print()
'''
   1 2 3 4

1 /4 3 2 1
2 /8 6 4 2
3 /12 9 6 3
4 /16 12 8 4



'''