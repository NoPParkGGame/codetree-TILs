string_A = input()

def is_various(string):
    cnt=1
    for i in range(len(string)):
        if string[0] != string[i]:
            cnt+=1
    if cnt>1:
        return True
    return False

if is_various(string_A):
    print('Yes')
else:
    print('No')