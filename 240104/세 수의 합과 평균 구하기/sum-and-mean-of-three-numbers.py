num=input().split()

n=0
while n<len(num):
    num[n]=int(num[n])
    n+=1
print(sum(num))
print(sum(num)//len(num))