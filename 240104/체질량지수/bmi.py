info=input().split()
# info=[178, 88]
hei=int(info[0])
#hei= 178cm   -> 1.78m
wei=int(info[1])
#wei= 88
hei2=hei/100
bmi=wei/(hei2**2)

print(int(bmi))
if bmi>=25:
    print('Obesity')