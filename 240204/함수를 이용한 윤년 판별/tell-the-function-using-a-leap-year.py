def is_feb_29(y):
    if y%4!=0:
        return False
    if y%4==0 and y%100==0:
        return False
    if (y%4!=0 and y%100!=0) or (y%400!=0):
        return False
    return True

y=int(input())

if is_feb_29(y):
    print('true')
else:
    print('false')