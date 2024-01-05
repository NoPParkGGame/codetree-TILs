n=int(input())

if n==2:
    print('28')
else:
    if (n<8 and n%2==1) or (n>=8 and n%2==0):
        print(31)
    else:
        print(30)
# 31일: 1,3,5,7,8,10,12