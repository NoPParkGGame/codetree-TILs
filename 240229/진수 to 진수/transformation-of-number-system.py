a, b = tuple(map(int, input().split())) # a진수 와 b진수

a_num=list(map(int, input()))

num=0

for i in range(len(a_num)):
    num= num* a +a_num[i]

digit=[]

while True:
    if num<b:
        digit.append(num)
        break
    digit.append(num%b)
    num//=b

for elem in digit[::-1]:
    print(elem, end='')