main_str = input()
part_str = input()

leng_m = len(main_str)
leng_p = len(part_str)



def is_part():
    for i in range(leng_m - leng_p +1):
        if main_str[i:i+leng_p] == part_str:
            return i
    return -1

print(is_part())