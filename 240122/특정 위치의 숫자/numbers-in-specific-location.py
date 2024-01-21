arr=list(map(int,input().split()))
sum_val=0
for i in range(len(arr)):
    n=i
    if n==2 or n==4 or n==9:
        sum_val+=arr[n]
print(sum_val)