arr=input().split()
n=0
while n<len(arr):
    arr[n]=int(arr[n])
    n+=1
sum=sum(arr)
ave=sum//len(arr)
print(sum)
print(ave)
print(sum-ave)