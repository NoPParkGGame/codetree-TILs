string=input()
sum_val=0
for elem in string:
    if elem.isdigit():
        sum_val+=int(elem)

print(sum_val)