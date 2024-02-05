def is_leap_year(year):
    if year%4 != 0:
        return False
    elif year%100 != 0:
        return True
    elif year%400==0:
        return True
    return False

def get_day_of_month(year, month, day):
    if month==2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month == 1 or month == 3 or month == 5 or month== 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        return 30
    
def is_exist_day(year, month, day):
    if 1 <= month <= 12 and get_day_of_month(year, month, day):
        return True
    return False

def get_season(year, month, day):
    if is_exist_day(year, month, day):
        if 3 <= month <= 5:
            return 'Spring'
        if 6 <= month<= 8:
            return 'Summer'
        if 9 <= month <=11:
            return 'Fall'
        else:
            return 'Winter'
    else:
        return -1

Y, M, D = tuple(map(int, input().split()))

print(get_season(Y, M, D))