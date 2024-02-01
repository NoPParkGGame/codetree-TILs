string=list(input())
f_string=str(string[0])
s_string=str(string[1])
for i in range(len(string)):
    if string[i]==f_string:
        string[i]=s_string
    elif string[i]==s_string:
        string[i]=f_string
print(''.join(string))