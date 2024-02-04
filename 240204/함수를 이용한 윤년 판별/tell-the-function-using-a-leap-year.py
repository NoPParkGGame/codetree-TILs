def is_feb_29(y):
    if y%4!=0:
        return False
    elif y%4==0 and y%100==0:
        return False
    elif (y%4!=0 and y%100!=0) and (y%400!=0):
        return True
    else:
        return False

y=int(input())

if is_feb_29(y):
    print('true')
else:
    print('false')