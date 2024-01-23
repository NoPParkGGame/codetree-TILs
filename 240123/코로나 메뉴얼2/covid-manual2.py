grade_arr=['A','B','C','D']
count_arr=[]
comp_arr=[]
for i in range(3):
    arr=input().split()
    a,b=arr[0],int(arr[1])
    if a=='Y':
        if b>=37:
            comp_arr.append('A')
        else:
            comp_arr.append('C')
    else:
        if b>=37:
            comp_arr.append('B')
        else:
            comp_arr.append('D')    
for elem in grade_arr:
    cnt=0
    for elem2 in comp_arr:
        if elem==elem2:
            cnt+=1
    count_arr.append(cnt) 
if count_arr[0]>=2:
    count_arr.append('E')
for elem in count_arr:
    print(elem,end=' ')      
'''

'''