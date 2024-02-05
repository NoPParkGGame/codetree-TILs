M, D = tuple(map(int, input().split()))

def is_MD_exist(month, day):
    if month == 2:
        if 1 <= day <= 28:
            return True
    else:
        if month<8:
            if month%2 != 0 and 1 <= day <= 31:
                return True
            else:
                if 1 <= day <= 30:
                    return True
        else:
            if month%2 == 0 and 1 <= day <= 31:
                return True
            else:
                if 1 <= day <= 30:
                    return True
    return False

if is_MD_exist(M, D):
    print('Yes')
else:
    print('No')
         




# 31일 : 1, 3, 5, 7,    8, 10, 12

# 30일 : 4, 6,   9, 11