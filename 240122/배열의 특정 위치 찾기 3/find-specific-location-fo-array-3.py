arr=list(map(int,input().split()))

new_arr=[]

for elem in arr:
    if elem==0:
        break
    else:
        new_arr.append(elem)
new_arr.append(0)
print(sum(new_arr[-4:-1]))