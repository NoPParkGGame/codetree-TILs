n=int(input())

for cur_n in range(1,n+1):
    div_cnt=0
    for div_n in range(1,cur_n+1):
        if cur_n%div_n==0:
            div_cnt+=1
    if div_cnt==2:
        print(cur_n,end=' ')