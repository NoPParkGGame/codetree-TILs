a, b= input().split()

sum_val=0
leng_a=0
leng_b=0
for elem in a:
    if elem.isdigit():
        leng_a+=1
    else:
        break
for elem in b:
    if elem.isdigit():
        leng_b+=1
    else:
        break

sum_val+=int(a[0:leng_a])
sum_val+=int(b[0:leng_b])
print(sum_val)