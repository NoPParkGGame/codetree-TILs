day_of_months=[0,31,28,31,30,31,30,31,31,30,31,30,31]

m1, d1, m2, d2= tuple(map(int, input().split()))

month, day= m1, d1
elapsed_day=0

while True:
    day+=1
    elapsed_day+=1    
    
    if month==m2 and day==d2:
        break


    if day>day_of_months[month]:
        month+=1
        day=0
print(elapsed_day)