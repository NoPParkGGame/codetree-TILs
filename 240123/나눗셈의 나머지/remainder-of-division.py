arr=list(map(int,input().split()))
a,b=arr[0],arr[1]
count_arr=[0]*10
rest_arr=[]
while a>1:
    rest_arr.append(a%b)
    a//=b

for i in range(0,10):
    for elem in rest_arr:
        if i==elem:
            count_arr[i]+=1
sum_val=0
for elem in count_arr:
    sum_val+=elem**2
print(sum_val)