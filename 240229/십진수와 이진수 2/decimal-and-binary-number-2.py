binary=list(map(int,list(input())))

num=0

for i in range(len(binary)):
    num= num*2 + binary[i]

num*=17
digit=[]

while True:
    if num<2:
        digit.append(num)
        break
    digit.append(num%2)
    num//=2

for elem in digit[::-1]:
    print(elem, end='')