arr=input().split()
n=0
for i in range(0,len(arr)):
   arr[n]=int(arr[n])
   n+=1 
print(sum(arr),sum(arr)/len(arr))