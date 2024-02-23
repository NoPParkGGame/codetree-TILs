n, k ,T = input().split()
n, k = int(n), int(k)

arr=[]

for _ in range(n):
    string=input()

    indicator=True

    if len(T)<=len(string):
        for i in range(len(T)):
            if T[i] !=string[i]:
                indicator=False

    if indicator==True:
        arr.append(string)

arr.sort()

print(arr[k-1])