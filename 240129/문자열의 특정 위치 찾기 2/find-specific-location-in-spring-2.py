alph=input()
arr=["apple", "banana", "grape", "blueberry", "orange"]

num=0
for i in range(len(arr)):
    if alph==arr[i][2] or alph==arr[i][3]:
        print(arr[i])
        num+=1
print(num)