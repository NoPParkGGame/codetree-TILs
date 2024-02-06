string=input()

def is_pal(string):
    if string==string[::-1]:
        return True
    return False

if is_pal(string):
    print('Yes')
else:
    print('No')