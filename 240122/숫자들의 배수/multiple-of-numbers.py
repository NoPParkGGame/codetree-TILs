n=int(input())
cnt=1
mult_cnt=0
arr=[]
while True:
    if n*cnt%5==0:
        mult_cnt+=1
    if mult_cnt>=2:
        arr.append(n*cnt)
        break
    arr.append(n*cnt)
    cnt+=1        
for elem in arr:
    print(elem,end=' ')