string_A=input()
string_B=input()
num1=""
num2=""
for elem in string_A:
    if elem.isdigit():
        num1=num1+elem

for elem in string_B:
    if elem.isdigit():
        num2=num2+elem

print(int(num1)+int(num2))