day, hour, minute= tuple(map(int, input().split()))

d, h, m=11, 11, 11
elpd_m=0
while True:

    if day*24*60 + hour*60 + minute < 16511:
        elpd_m=-1
        break

    if d==day and h==hour and m==minute:
        break
    
    m+=1
    elpd_m+=1

    if m==60:
        h+=1
        m=0

    if h==24:
        d+=1
        h=0

print(elpd_m)