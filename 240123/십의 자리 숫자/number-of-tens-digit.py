arr=list(map(int,input().split()))
teen_arr=[]
for elem in arr:
    if elem==0:
        break
    else:
        teen_arr.append(elem//10)

count_arr=[i for i in range(1,10)]

for counter in count_arr:
    cnt=0
    for subj in teen_arr:
        if counter==subj:
            cnt+=1
    print(counter,'-',cnt)