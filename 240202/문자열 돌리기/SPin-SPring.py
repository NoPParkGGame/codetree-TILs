string=input()
num=1
print(string)
while num<=len(string):
    string=string[-1]+ string[:-1]
    print(string)
    num+=1