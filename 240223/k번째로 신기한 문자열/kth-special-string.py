n, k ,T = input().split()
n, k = int(n), int(k)

arr=[]

for _ in range(n):
    string=input()

    if len(T)<=len(string):
        indicator=True
        for i in range(len(T)):
            if T[i] !=string[i]:
                indicator=False
    else:
        indicator=False
        
    if indicator==True:
        arr.append(string)

arr.sort()

print(arr[k-1])