n=int(input())
cnt=0
for i in range(n,0,-1):
    for j in range(n-i+1):
        print(i+cnt,end=' ')
        cnt+=1
    cnt=0
    print()
'''
   0 1 2 3 4

5 /5
4 /4 5
3 /3 4 5
2 /2 3 4 5
1 /1 2 3 4 5


'''