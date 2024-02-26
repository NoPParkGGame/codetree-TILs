a, b, c, d= tuple(map(int, input().split()))

hours, mins = a, b
elpased_time=0

while True:
    if hours==c and mins==d:
        break
    
    mins+=1
    elpased_time+=1

    if mins==60:
        hours+=1
        mins=0
print(elpased_time)