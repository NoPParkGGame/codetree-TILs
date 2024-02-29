n, b = tuple(map(int, input().split()))

digit=[]

while True:
    if n<b:
        digit.append(n)
        break
    digit.append(n%b)
    n//=b

digit.reverse()

for elem in digit:
    print(elem, end='')