arr=input().split()
arr2=input().split()
arr3=input().split()
a1 , a2 = arr[0], int(arr[1])
b1 , b2 = arr2[0], int(arr2[1])
c1 , c2 = arr3[0], int(arr3[1])

if a1=='Y' and a2>=37:
    if (b1=='Y' and b2>=37) or (c1=='Y' and c2>=37):
        print('E')
    else:
        print('N')
else:
    if (b1=='Y' and b2>=37) and (c1=='Y' and c2>=37):
        print('E')
    else:
        print('N')