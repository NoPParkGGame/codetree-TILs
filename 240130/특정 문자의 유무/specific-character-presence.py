s=input()

exisit_ee=False
exisit_ab=False

for i in range(len(s)-1):
    if s[i:i+2]=='ee':
        exisit_ee=True
    if s[i:i+2]=='ab':
        exisit_ab=True
if exisit_ee==True:
    print('Yes')
else:
    print('No')
if exisit_ab==True:
    print('Yes',end=' ')
else:
    print('No')