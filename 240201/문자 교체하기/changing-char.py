str_1, str_2= input().split()
str_1=list(str_1)
str_2=list(str_2)

str_2[0:2]=str_1[0:2]

print(''.join(str_2))