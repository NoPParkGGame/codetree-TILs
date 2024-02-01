string=list(input())
string_1=string[0]
string_2=string[1]

for i in range(len(string)):
    if string[i]==string_2:
        string[i]=string_1
print(''.join(string))