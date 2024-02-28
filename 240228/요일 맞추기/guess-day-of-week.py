m1, d1, m2, d2 = tuple(map(int, input().split()))

day_of_month=[0,31,28,31,30,31,30,31,31,30,31,30,31]

day_of_week=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
reversed_day_of_week=['Mon', 'Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue']

month, day =m1, d1

elapsed_day=0

indicator=False

while True:
    if m1==m2 and d1==d2:
        break
    
    elif (m1==m2 and d1>d2) or m1>m2:
        indicator=True

    if month==m2 and day==d2:
        break
    
    day+=1
    elapsed_day+=1

    if day>day_of_month[month]:
        month+=1
        day=1

while indicator==True:
    if month==m2 and day==d2:
        break
    
    day-=1
    elapsed_day-=1

    if day==1:
        month-=1
        day=day_of_month[month]

if elapsed_day>=0:
    print(day_of_week[elapsed_day&7])
else:
    print(reversed_day_of_week[abs(elapsed_day)%7])

'''
+0 +7월
+1 +8화
+2 +9수
+3 +10목
+4 +11금
+5 +12토
+6 +13일


즉, 7로 나누었을 때 나머지가 요일을 결정함

0 월
-1 일
-2 토
-3 금
-4 목
-5 수
-6 화

월일토금목수화





'''