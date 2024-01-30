string=input()

even_string=''

for elem in string[1::2]:
    even_string+=elem

print(even_string[::-1])