n=int(input())

sum_val=0
for i in range(1,n+1):
    if n%i==0 and n!=i:
        sum_val+=i

if n==sum_val:
    print('P')
else:
    print('N')