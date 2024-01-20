n=int(input())
cnt=1
for i in range(n,0,-1):
    if cnt>9:
        cnt=1
    for j in range(n-i):
        print(' ',end=' ')
    for j in range(i):
        print(cnt,end=' ')
        cnt+=1
    print()

'''

i   ''
5   0
4   1
3   2
2   3
1   4
'''