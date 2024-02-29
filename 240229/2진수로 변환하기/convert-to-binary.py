num=int(input())

digit=[]

while True:
    if num<2:
        digit.append(num)
        break
    
    digit.append(num%2)
    num//=2

digit.reverse()

for elem in digit:
    print(elem, end='')